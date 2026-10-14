"""Regenerate index.json from articles/*.md front matter.

index.json is the one file consuming sites fetch (from
raw.githubusercontent.com, which is not rate-limited the way the REST API
is): every article's metadata, newest first. The index workflow runs this on
each push that touches articles/; running it by hand is always safe.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def front_matter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    meta = {}
    for line in text[3:end].split("\n"):
        k = line.find(":")
        if k == -1:
            continue
        v = line[k + 1 :].strip()
        if v.startswith('"') and v.endswith('"'):
            v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        meta[line[:k].strip()] = v
    return meta


def main():
    rows = []
    for f in sorted((ROOT / "articles").glob("*.md")):
        if f.name.startswith("_"):
            continue
        meta = front_matter(f.read_text())
        if not meta or "title" not in meta or "date" not in meta:
            raise SystemExit(f"{f.name}: missing or malformed front matter")
        rows.append(
            dict(
                slug=meta.get("slug", f.stem),
                title=meta["title"],
                stand=meta.get("stand", ""),
                lane=meta.get("lane", ""),
                laneTag=meta.get("laneTag", ""),
                date=meta["date"],
                minutes=int(meta.get("minutes", 5)),
                sites=meta.get("sites", "both"),
                canonical=meta.get("canonical", "skala"),
                featured=meta.get("featured", "false") == "true",
                order=int(meta.get("order", 999)),
            )
        )
    rows.sort(key=lambda r: (r["date"], r["order"]), reverse=True)
    (ROOT / "index.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(f"index.json: {len(rows)} articles")


if __name__ == "__main__":
    main()
