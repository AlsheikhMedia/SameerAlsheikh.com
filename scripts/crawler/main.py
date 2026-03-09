"""
Crawl sameeralsheikh.com to extract all poems with metadata.

Usage:
    python main.py              # Crawl all poems
    python main.py --limit 5    # Crawl first 5 poems (for testing)
"""

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from parser import parse_verses

BASE_URL = "https://sameeralsheikh.com"
SITEMAP_URL = f"{BASE_URL}/wp-sitemap-posts-post-1.xml"
OUTPUT_FILE = Path(__file__).parent / "poems.json"

# Arabic month names → month numbers
ARABIC_MONTHS = {
    "يناير": 1, "فبراير": 2, "مارس": 3, "أبريل": 4,
    "مايو": 5, "يونيو": 6, "يوليو": 7, "أغسطس": 8,
    "سبتمبر": 9, "أكتوبر": 10, "نوفمبر": 11, "ديسمبر": 12,
}

# Category Arabic → slug mapping
CATEGORY_SLUGS = {
    "روحية": "ruhiya",
    "وجدانية": "wijdaniya",
    "قصائد غزل": "ghazal",
    "غزل": "ghazal",
    "مدح": "madh",
    "رثاء": "ritha",
    "هجاء": "hija",
    "وطنية": "wataniya",
}


def fetch_poem_urls() -> list[str]:
    """Fetch all poem URLs from the WordPress sitemap."""
    resp = requests.get(SITEMAP_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, "lxml-xml")
    urls = [loc.text.strip() for loc in soup.find_all("loc")]
    return urls


def parse_arabic_date(date_str: str) -> str:
    """Convert 'يونيو 26, 2012' → '2012-06-26'."""
    match = re.match(r"(\S+)\s+(\d+),\s+(\d{4})", date_str.strip())
    if not match:
        return ""
    month_name, day, year = match.groups()
    month = ARABIC_MONTHS.get(month_name, 0)
    if not month:
        return ""
    return f"{year}-{month:02d}-{int(day):02d}"


def url_to_slug(url: str, title: str) -> str:
    """Derive a URL-safe slug from the poem URL or title."""
    path = url.rstrip("/").split("/")[-1]
    # URL-decode Arabic slugs
    decoded = unquote(path)
    # If it's a numeric path, use a transliterated version of the title
    if decoded.isdigit():
        # Use Arabic title as slug (kebab-case with Arabic chars)
        slug = re.sub(r"[^\w\s-]", "", title, flags=re.UNICODE)
        slug = re.sub(r"\s+", "-", slug.strip())
        return slug if slug else decoded
    # Clean up decorative characters from slug
    decoded = re.sub(r"[ـ]+", "", decoded)  # Remove tatweel/kashida
    return decoded


def crawl_poem(url: str) -> dict | None:
    """Fetch and parse a single poem page."""
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  ERROR fetching {url}: {e}")
        return None

    html = resp.text
    soup = BeautifulSoup(html, "lxml")

    # Title
    title_el = soup.find("h1", class_="entry-title")
    if not title_el:
        print(f"  SKIP {url}: no title found")
        return None
    title = title_el.get_text().strip()

    # Date
    date_el = soup.find("span", class_="entry-date")
    date_str = ""
    if date_el:
        date_str = parse_arabic_date(date_el.get_text().strip())

    # Category
    category_ar = ""
    category_slug = ""
    # Category is in entry-utility div, inside <a rel="category tag">
    utility_div = soup.find("div", class_="entry-utility")
    if utility_div:
        cat_link = utility_div.find("a", rel="category tag")
        if cat_link:
            category_ar = cat_link.get_text().strip()
            category_slug = CATEGORY_SLUGS.get(category_ar, "")

    if not category_slug:
        # Fallback: check post classes for category
        post_div = soup.find("div", class_=re.compile(r"^post-\d+"))
        if post_div:
            classes = post_div.get("class", [])
            for cls in classes:
                if cls.startswith("category-"):
                    pass  # numeric category ID, not helpful
        if not category_slug:
            print(f"  WARNING: unknown category '{category_ar}' for {title}")
            category_slug = "other"

    # Poem content
    entry_content = soup.find("div", class_="entry-content")
    if not entry_content:
        print(f"  SKIP {url}: no entry-content found")
        return None

    verses = parse_verses(str(entry_content), title=title)
    if not verses:
        print(f"  WARNING: no verses parsed for {title}")
        return None

    # Slug
    slug = url_to_slug(url, title)

    return {
        "slug": slug,
        "title": title,
        "category": category_slug,
        "categoryAr": category_ar,
        "date": date_str,
        "verses": verses,
        "sourceUrl": url,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="Max poems to crawl (0=all)")
    args = ap.parse_args()

    print("Fetching sitemap...")
    urls = fetch_poem_urls()
    print(f"Found {len(urls)} poem URLs")

    if args.limit:
        urls = urls[: args.limit]
        print(f"Limiting to {args.limit} poems")

    poems = []
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Crawling: {unquote(url.split('/')[-2])}")
        poem = crawl_poem(url)
        if poem:
            poems.append(poem)
        # Be polite
        time.sleep(0.5)

    # Sort by date (oldest first)
    poems.sort(key=lambda p: p.get("date", ""))

    OUTPUT_FILE.write_text(json.dumps(poems, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nDone! Wrote {len(poems)} poems to {OUTPUT_FILE}")

    # Summary
    cats = {}
    for p in poems:
        cats[p["categoryAr"]] = cats.get(p["categoryAr"], 0) + 1
    print("\nCategory breakdown:")
    for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
