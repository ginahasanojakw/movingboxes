# === Stage 6: Текстовый поиск ===
# Project: MovingBoxes
import re


def build_search_pattern(text, needle, count=0):
    pattern = re.compile(
        r"(?i)\b" + re.escape(needle) + r"\b",
        re.IGNORECASE,
    )

    def repl(match):
        if count > 0 and count <= len(matched):
            matched[0] = match
            return "\033[1;33m" + match.group(0) + "\033[0m"
        return match.group(0)

    matched = []
    return pattern.sub(repl, text), matched


def find_boxes(needle, boxes):
    results = []
    for box in boxes:
        lines = []
        for field in ("number", "room", "weight", "fragile"):
            value = getattr(box, field, "")
            highlighted, hits = build_search_pattern(str(value), needle)
            lines.append(highlighted)
            results.extend(hits)
        if any("MATCH" in line for line in lines):
            results.append("\n".join(lines))
    return results


if __name__ == "__main__":
    boxes = [
        Box(
            number="A1",
            room="Kitchen",
            weight="12.5 kg",
            fragile="Glass vases",
        ),
        Box(
            number="B2",
            room="Bedroom",
            weight="8.0 kg",
            fragile="Porcelain set",
        ),
        Box(
            number="C3",
            room="Living Room",
            weight="15.2 kg",
            fragile="Books",
        ),
    ]

    query = input("Search: ").strip().lower()
    if not query:
        print("Nothing to search.")
    else:
        for result in find_boxes(query, boxes):
            print(result)
