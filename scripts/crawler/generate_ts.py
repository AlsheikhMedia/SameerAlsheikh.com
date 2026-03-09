"""
Generate src/data/poems.ts from crawled poems.json.

Reads poems.json (output of main.py) and produces the TypeScript data file
that the Astro site consumes.
"""

import json
import re
from pathlib import Path

POEMS_JSON = Path(__file__).parent / "poems.json"
OUTPUT_TS = Path(__file__).parent.parent.parent / "src" / "data" / "poems.ts"

# Category slug → Arabic name (matching the 7 live site categories)
CATEGORIES = {
    "ruhiya": "روحية",
    "wijdaniya": "وجدانية",
    "ghazal": "غزل",
    "madh": "مدح",
    "ritha": "رثاء",
    "hija": "هجاء",
    "wataniya": "وطنية",
}


def escape_ts_string(s: str) -> str:
    """Escape a string for use in TypeScript single-quoted strings."""
    s = s.replace("\\", "\\\\")
    s = s.replace("'", "\\'")
    s = s.replace("\n", "\\n")
    return s


def generate():
    with open(POEMS_JSON, "r", encoding="utf-8") as f:
        poems = json.load(f)

    # Track which categories have had their first poem marked as featured
    featured_cats = set()

    lines = []
    lines.append("export interface Poem {")
    lines.append("\tslug: string;")
    lines.append("\ttitle: string;")
    lines.append("\tcategory: string;")
    lines.append("\tdate?: string;")
    lines.append("\tfeatured?: boolean;")
    lines.append("\tverses: { sadr: string; ajz: string }[];")
    lines.append("}")
    lines.append("")

    # Categories map
    lines.append("export const categories: Record<string, string> = {")
    for slug, ar_name in CATEGORIES.items():
        lines.append(f"\t{slug}: '{ar_name}',")
    lines.append("};")
    lines.append("")

    # Poems array
    lines.append("export const poems: Poem[] = [")

    for poem in poems:
        cat = poem["category"]
        is_featured = cat not in featured_cats
        if is_featured:
            featured_cats.add(cat)

        title = escape_ts_string(poem["title"])
        slug = escape_ts_string(poem["slug"])
        date = poem.get("date", "")

        lines.append("\t{")
        lines.append(f"\t\tslug: '{slug}',")
        lines.append(f"\t\ttitle: '{title}',")
        lines.append(f"\t\tcategory: '{cat}',")
        if date:
            lines.append(f"\t\tdate: '{date}',")
        if is_featured:
            lines.append(f"\t\tfeatured: true,")
        lines.append(f"\t\tverses: [")

        for verse in poem["verses"]:
            sadr = escape_ts_string(verse["sadr"])
            ajz = escape_ts_string(verse["ajz"])
            lines.append(f"\t\t\t{{ sadr: '{sadr}', ajz: '{ajz}' }},")

        lines.append(f"\t\t],")
        lines.append("\t},")

    lines.append("];")
    lines.append("")

    # Exports
    lines.append("export const featuredPoems = poems.filter(p => p.featured);")
    lines.append("")

    # Bio text (preserved from original)
    lines.append("export const bioText = `سمير الشيخ حسين شاعرٌ عربيٌّ من مواليد عام ١٩٥١، نشأ في بيئةٍ عربيةٍ أصيلةٍ تشرَّبَ منها حبَّ اللغة والأدب. بدأ نظمَ الشعرِ في سنٍّ مبكرةٍ مُتأثراً بعمالقة الشعر العربي الكلاسيكي، من المتنبي إلى أحمد شوقي.")
    lines.append("")
    lines.append("على مدى أكثر من خمسين عاماً، أثرى المشهدَ الشعريَّ العربيَّ بأكثر من ثلاثمئة قصيدة تتنوَّعُ بين الغزل والحكمة والوطنيات والرثاء. تتميَّزُ قصائدُه بجزالة اللفظ وعُمق المعنى وصدق العاطفة، مع التزامٍ راسخٍ بأوزان الخليل بن أحمد وبحور الشعر العربي الأصيل.`;")
    lines.append("")

    output = "\n".join(lines)
    OUTPUT_TS.write_text(output, encoding="utf-8")
    print(f"Generated {OUTPUT_TS}")
    print(f"  {len(poems)} poems")
    print(f"  {len(featured_cats)} featured (one per category)")
    print(f"  Categories: {', '.join(sorted(featured_cats))}")


if __name__ == "__main__":
    generate()
