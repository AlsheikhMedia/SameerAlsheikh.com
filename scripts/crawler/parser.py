"""
Verse parser for sameeralsheikh.com poems.

Five HTML formats found on the site:

Format A — Div-based (margin-left/margin-right divs inside a table td):
  Each sadr has margin-left, each ajz has margin-right.

Format B — Table with 2 TDs per row:
  Each <tr> has two <td> cells: first=sadr, second=ajz.

Format C — Single-column table (free verse):
  Each <tr> has one <td> with colspan. Each row = one line.

Format D — Single TD with br-separated spans (free verse):
  One <td> containing <span>...<br><span>... lines.

Format E — Paragraph-based (free verse):
  Poem text in <p> and <h1> tags.

Free verse poems store each line as sadr with empty ajz.
"""

import re
from bs4 import BeautifulSoup, NavigableString, Tag


def parse_verses(entry_content_html: str, title: str = "") -> list[dict[str, str]]:
    """Parse poem HTML into list of {sadr, ajz} verse dicts."""
    soup = BeautifulSoup(entry_content_html, "lxml")

    # Try Format A: div-based with margin-left/margin-right
    verses = _try_div_format(soup, title=title)
    if verses:
        return verses

    # Try Format B: table with 2 TDs per row
    verses = _try_table_2col_format(soup)
    if verses:
        return verses

    # Try Format D: single td with br-separated content (before single-col table)
    verses = _try_single_td_br(soup)
    if verses:
        return verses

    # Try Format C: single-column table (one td per row with colspan)
    verses = _try_table_single_col(soup)
    if verses:
        return verses

    # Try Format E: paragraph-based (free verse)
    verses = _try_paragraph_format(soup)
    if verses:
        return verses

    return []


def _try_div_format(soup: BeautifulSoup, title: str = "") -> list[dict[str, str]]:
    """Format A: divs with margin-left (sadr) and margin-right (ajz)."""
    td = soup.find("td", attrs={"valign": "top"})
    container = td if td else soup

    divs = container.find_all("div", style=True)

    sadr_lines = []
    ajz_lines = []

    for div in divs:
        style = div.get("style", "")
        has_ml = "margin-left" in style
        has_mr = "margin-right" in style

        if not has_ml and not has_mr:
            continue

        text = _clean_div_text(div)
        if not text:
            continue

        # Skip stanza separators
        if re.match(r"^\s*\*\s+\*\s+\*\s*$", text):
            continue

        if has_ml and not has_mr:
            sadr_lines.append(text)
        elif has_mr and not has_ml:
            ajz_lines.append(text)

    if not sadr_lines:
        return []

    # Skip title line if repeated as first sadr
    if title and sadr_lines and sadr_lines[0] == title:
        sadr_lines = sadr_lines[1:]

    return _pair_lines(sadr_lines, ajz_lines)


def _try_table_2col_format(soup: BeautifulSoup) -> list[dict[str, str]]:
    """Format B: each <tr> has exactly two <td> cells = sadr + ajz."""
    tables = soup.find_all("table")
    for table in tables:
        rows = table.find_all("tr")
        two_col_rows = 0
        for row in rows:
            cells = row.find_all("td")
            if len(cells) == 2:
                two_col_rows += 1

        # Only use this format if most rows have 2 columns
        if two_col_rows < 2:
            continue

        verses = []
        for row in rows:
            cells = row.find_all("td")
            if len(cells) == 2:
                sadr = _clean_cell_text(cells[0])
                ajz = _clean_cell_text(cells[1])
                if sadr or ajz:
                    verses.append({"sadr": sadr, "ajz": ajz})
        if verses:
            return verses
    return []


def _try_table_single_col(soup: BeautifulSoup) -> list[dict[str, str]]:
    """Format C: single-column table, each row has one td (often with colspan).
    Free verse — each line is sadr with empty ajz."""
    tables = soup.find_all("table")
    for table in tables:
        rows = table.find_all("tr")
        verses = []
        is_first_row = True
        for row in rows:
            cells = row.find_all("td")
            if len(cells) == 1:
                text = _clean_cell_text(cells[0])
                if not text:
                    continue
                # Skip the title row (usually first row)
                if is_first_row:
                    is_first_row = False
                    continue
                verses.append({"sadr": text, "ajz": ""})
            elif len(cells) == 3:
                # colspan=3 in a single-column layout
                # Check if all cells are the same (it's actually one cell spanning)
                texts = [_clean_cell_text(c) for c in cells]
                combined = " ".join(t for t in texts if t).strip()
                if not combined:
                    continue
                if is_first_row:
                    is_first_row = False
                    continue
                verses.append({"sadr": combined, "ajz": ""})
        if verses:
            return verses
    return []


def _try_single_td_br(soup: BeautifulSoup) -> list[dict[str, str]]:
    """Format D: a single td with br-separated spans/text lines."""
    td = soup.find("td", attrs={"valign": "top"})
    if not td:
        return []

    # Check if it has divs with margins (that's Format A)
    if td.find("div", style=lambda s: s and "margin-left" in s):
        return []

    # Get text split by <br> tags
    lines = _extract_br_lines(td)
    if not lines:
        return []

    # Free verse: each line is sadr
    return [{"sadr": line, "ajz": ""} for line in lines]


def _try_paragraph_format(soup: BeautifulSoup) -> list[dict[str, str]]:
    """Format E: free verse in <p> and <h1> tags."""
    lines = []
    for el in soup.find_all(["p", "h1", "h2", "h3"]):
        text = _normalize_arabic(el.get_text())
        if text and len(text) > 1:
            lines.append(text)

    if not lines:
        return []

    # Pair consecutive lines as sadr/ajz
    verses = []
    for i in range(0, len(lines), 2):
        sadr = lines[i]
        ajz = lines[i + 1] if i + 1 < len(lines) else ""
        verses.append({"sadr": sadr, "ajz": ajz})

    return verses


def _extract_br_lines(element: Tag) -> list[str]:
    """Extract lines from an element that uses <br> as line separators."""
    # Replace <br> with a unique separator, then split
    html_str = str(element)
    html_str = re.sub(r"<br\s*/?>", "\n", html_str)
    temp_soup = BeautifulSoup(html_str, "lxml")

    # Replace hidden spans with a space (to avoid concatenating adjacent text)
    for span in list(temp_soup.find_all("span", style=True)):
        try:
            style = (span.attrs or {}).get("style", "") or ""
        except Exception:
            continue
        if "visibility: hidden" in style or "visibility:hidden" in style:
            span.replace_with(" ")

    text = temp_soup.get_text()
    lines = []
    for line in text.split("\n"):
        clean = _normalize_arabic(line)
        if clean and len(clean) > 1:
            lines.append(clean)
    return lines


def _normalize_arabic(text: str) -> str:
    """Strip decorative tatweels (kashida) and normalize whitespace."""
    text = text.replace("\u0640", "")  # Remove tatweel ـ
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _pair_lines(sadr_lines: list[str], ajz_lines: list[str]) -> list[dict[str, str]]:
    """Pair sadr and ajz line lists into verse dicts."""
    verses = []
    max_len = max(len(sadr_lines), len(ajz_lines))
    for i in range(max_len):
        sadr = sadr_lines[i] if i < len(sadr_lines) else ""
        ajz = ajz_lines[i] if i < len(ajz_lines) else ""
        if sadr or ajz:
            verses.append({"sadr": sadr, "ajz": ajz})
    return verses


def _clean_div_text(div: Tag) -> str:
    """Extract clean text from a verse div, removing hidden spans and markers."""
    div = BeautifulSoup(str(div), "lxml").find("div")
    if not div:
        return ""

    # Replace hidden spans with space, remove acrostic markers
    for span in list(div.find_all("span", style=True)):
        try:
            style = (span.attrs or {}).get("style", "") or ""
        except Exception:
            continue
        if "visibility: hidden" in style or "visibility:hidden" in style:
            span.replace_with(" ")
        elif "background-color" in style and ("ff0000" in style.lower()):
            span.decompose()

    text = div.get_text()

    # Remove standalone acrostic markers like ( أ )
    text = re.sub(r"^\s*\(\s*\S\s*\)\s*", "", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Remove leading single letter (acrostic remainder like "ز   زرعٌ")
    text = re.sub(r"^(\S)\s{2,}", "", text)

    return _normalize_arabic(text)


def _clean_cell_text(cell: Tag) -> str:
    """Extract clean text from a table cell."""
    # Replace hidden spans with space
    cell_copy = BeautifulSoup(str(cell), "lxml")
    for span in list(cell_copy.find_all("span", style=True)):
        try:
            style = (span.attrs or {}).get("style", "") or ""
        except Exception:
            continue
        if "visibility: hidden" in style or "visibility:hidden" in style:
            span.replace_with(" ")

    text = cell_copy.get_text()
    return _normalize_arabic(text)
