#!/usr/bin/env python3
"""Build the concept pages from TOML data, and check them.

The library has two halves. The numbered chapters are lessons: one question,
programs in six languages, output held to an answer key. `11_Concepts/` is the
other half: the vocabulary those lessons use, laid out as an ontology (what is a
kind of what), a schema (what prevents, causes, uses, or is confused with what),
and one short page per concept that says what it is called in each language and
where to read more. Those pages are cross-reference stubs, not lessons, and they
are generated so that the cross-references cannot drift: a link from A to B is
written once, in data, and appears on both pages.

    python3 tools/build_concepts.py            # write every generated page
    python3 tools/build_concepts.py --check    # write nothing; fail on bad data or drift (CI)
    python3 tools/build_concepts.py --links    # also fetch every external URL (network; not CI)

Data
----
    11_Concepts/<category>/concepts.toml   a [category] table and one [[concept]] per concept
    11_Concepts/abbreviations.toml         [[abbreviation]] entries
    10_Resources/books.toml                [[book]] entries, referenced from concepts by id

A concept (every field but slug, title and summary is optional):

    [[concept]]
    slug = "deadlock"                    # folder name and permanent URL
    title = "Deadlock"
    summary = "..."                      # one sentence, in our own words
    aliases = ["deadly embrace"]
    chapter = 3                          # the numbered chapter that holds (or will hold) its lessons
    is_a = ["liveness_failure"]          # relations: see RELATIONS below; the inverse
    prevented_by = ["lock_ordering"]     #   spellings (kinds, used_by, prevented_by,
    contrasts = ["livelock"]             #   caused_by) may be written on either page
    lessons = ["01_Threads/who_waits_when_main_returns"]      # folders in this library
    pages = [["Go: All goroutines are asleep", "https://..."]] # sibling-library pages
    books = [["cox_buday_concurrency_in_go", "ch. 1, 'Deadlocks, Livelocks, and Starvation'"]]
    notes = [["Deadlock in general", "https://docs.google.com/..."]]
    reference = [["Wikipedia: Deadlock", "https://en.wikipedia.org/wiki/..."]]
    [concept.languages]                  # Markdown; links to official documentation
    rust = "..."
    go = "..."

Each generated page has a generated part and a hand-written part. On a concept,
category, books or abbreviations page the generated part is everything above the
HAND marker line; below it is yours and is kept. On the two overview pages
(`11_Concepts/README.md`, `11_Concepts/schema/README.md`) the generated part is
between `<!-- concepts:NAME -->` and `<!-- /concepts:NAME -->`.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONCEPTS = REPO / "11_Concepts"
RESOURCES = REPO / "10_Resources"
BOOKS_TOML = RESOURCES / "books.toml"
ABBR_TOML = CONCEPTS / "abbreviations.toml"
MARK = "↗"

HAND = "<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->"

LANGS = [
    ("rust", "Rust"), ("go", "Go"), ("c", "C"), ("cpp", "C++"), ("java", "Java"),
    ("python", "Python"), ("csharp", "C#"), ("javascript", "JavaScript"),
    ("kotlin", "Kotlin"), ("swift", "Swift"), ("elixir_erlang", "Erlang and Elixir"),
    ("haskell", "Haskell"), ("os", "The operating system"), ("other", "Elsewhere"),
]
LANG_KEYS = {k for k, _ in LANGS}

# The numbered chapters; a concept's `chapter` names the one that holds its lessons.
CHAPTERS = {
    1: "Threads", 2: "Shared state", 3: "When locks go wrong", 4: "Waiting for each other",
    5: "Message passing", 6: "Async", 7: "Parallelism", 8: "Processes", 9: "Testing and tools",
}

# key: (label on the page it is written from, label on the other page,
#       inverse spelling, symmetric?, label on a diagram edge or None to leave it off)
RELATIONS = {
    "is_a": ("Is a kind of", "Kinds", "kinds", False, "is a"),
    "uses": ("Is built on", "Is used by", "used_by", False, "uses"),
    "prevents": ("Helps prevent", "Is prevented by", "prevented_by", False, "prevents"),
    "causes": ("Can lead to", "Can be caused by", "caused_by", False, "can cause"),
    "alternative": ("An alternative to", "An alternative to", None, True, "or"),
    "contrasts": ("Often confused with", "Often confused with", None, True, "vs"),
    "related": ("See also", "See also", None, True, None),
}
INVERSE = {v[2]: k for k, v in RELATIONS.items() if v[2]}
# The order the relation lines appear in on a page.
RELATION_ORDER = [
    ("is_a", True), ("is_a", False), ("uses", True), ("uses", False),
    ("prevents", True), ("prevents", False), ("causes", True), ("causes", False),
    ("alternative", True), ("contrasts", True), ("related", True),
]

CONCEPT_KEYS = {
    "slug", "title", "summary", "aliases", "chapter", "status", "lessons", "pages",
    "books", "notes", "reference", "languages",
} | set(RELATIONS) | set(INVERSE)

FOCUS = [
    ("general", "General and cross-language"), ("rust", "Rust"), ("go", "Go"), ("c", "C"),
    ("cpp", "C++"), ("java", "Java"), ("csharp_dotnet", "C# and .NET"), ("python", "Python"),
    ("haskell", "Haskell"), ("elixir_erlang", "Erlang and Elixir"),
    ("scala_jvm_functional", "Scala and functional programming"), ("javascript", "JavaScript"),
    ("swift", "Swift"), ("other", "Other languages"),
]
FOCUS_KEYS = {k for k, _ in FOCUS}

LINK = re.compile(r"(?<!!)\[([^\]\[]+)\]\((\S+?)\)")


class DataError(Exception):
    pass


# --- loading -----------------------------------------------------------------


def load_toml(path: Path) -> dict:
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as e:
        raise DataError(f"{path.relative_to(REPO)}: {e}") from None


def load() -> dict:
    problems: list[str] = []
    categories: list[dict] = []
    concepts: dict[str, dict] = {}
    for path in sorted(CONCEPTS.glob("*/concepts.toml")):
        data = load_toml(path)
        head = data.get("category") or {}
        if "title" not in head:
            problems.append(f"{path.relative_to(REPO)}: no [category] title")
            continue
        cat = {
            "slug": path.parent.name, "title": head["title"], "order": head.get("order", 99),
            "blurb": head.get("blurb", ""), "slugs": [],
        }
        categories.append(cat)
        for entry in data.get("concept", []):
            slug = entry.get("slug", "?")
            where = f"{path.relative_to(REPO)}: {slug}"
            for key in ("slug", "title", "summary"):
                if not entry.get(key):
                    problems.append(f"{where}: missing {key}")
            unknown = set(entry) - CONCEPT_KEYS
            if unknown:
                problems.append(f"{where}: unknown field(s) {sorted(unknown)}")
            if not re.fullmatch(r"[a-z0-9_]+", slug):
                problems.append(f"{where}: slug must be lower_snake_case")
            if slug in concepts:
                problems.append(f"{where}: duplicate slug (also in {concepts[slug]['category']})")
                continue
            for lang in entry.get("languages", {}):
                if lang not in LANG_KEYS:
                    problems.append(f"{where}: unknown language key {lang!r}")
            for lang, text in entry.get("languages", {}).items():
                if "|" in text.replace("\\|", ""):
                    problems.append(f"{where}: languages.{lang} contains a bare | (breaks the table)")
            if "chapter" in entry and entry["chapter"] not in CHAPTERS:
                problems.append(f"{where}: chapter {entry['chapter']} is not one of {sorted(CHAPTERS)}")
            entry["category"] = cat["slug"]
            concepts[slug] = entry
            cat["slugs"].append(slug)
    categories.sort(key=lambda c: (c["order"], c["slug"]))

    books = {}
    if BOOKS_TOML.exists():
        for b in load_toml(BOOKS_TOML).get("book", []):
            if b.get("id") in books:
                problems.append(f"books.toml: duplicate id {b.get('id')}")
            if b.get("focus") not in FOCUS_KEYS:
                problems.append(f"books.toml: {b.get('id')}: focus {b.get('focus')!r} not in {sorted(FOCUS_KEYS)}")
            books[b.get("id")] = b

    abbreviations = load_toml(ABBR_TOML).get("abbreviation", []) if ABBR_TOML.exists() else []

    # Book references live in their own file, so the table-of-contents survey and
    # the per-category data can be edited independently.
    refs_path = CONCEPTS / "book_refs.toml"
    if refs_path.exists():
        for ref in load_toml(refs_path).get("ref", []):
            if ref.get("concept") not in concepts:
                problems.append(f"book_refs.toml: unknown concept {ref.get('concept')!r}")
                continue
            concepts[ref["concept"]].setdefault("books", []).append([ref.get("book"), ref.get("where", "")])

    edges: set[tuple[str, str, str]] = set()
    for slug, c in concepts.items():
        where = f"{c['category']}/{slug}"
        for key in list(RELATIONS) + list(INVERSE):
            for target in c.get(key, []):
                if target not in concepts:
                    problems.append(f"{where}: {key} names unknown concept {target!r}")
                    continue
                if target == slug:
                    problems.append(f"{where}: {key} names itself")
                    continue
                rel = INVERSE.get(key, key)
                a, b = (target, slug) if key in INVERSE else (slug, target)
                if RELATIONS[rel][3]:
                    a, b = sorted((a, b))
                edges.add((a, rel, b))
        for folder in c.get("lessons", []):
            if not (REPO / folder / "README.md").exists():
                problems.append(f"{where}: lesson {folder!r} has no README.md")
        for book_id, _ in c.get("books", []):
            if book_id not in books:
                problems.append(f"{where}: unknown book id {book_id!r}")
        for field in ("pages", "notes", "reference"):
            for pair in c.get(field, []):
                if len(pair) != 2 or not str(pair[1]).startswith("http"):
                    problems.append(f"{where}: {field} entries are [label, https-url]: {pair!r}")
    for a in abbreviations:
        if a.get("concept") and a["concept"] not in concepts:
            problems.append(f"abbreviations.toml: {a.get('abbr')}: unknown concept {a['concept']!r}")
        if not str(a.get("source", "")).startswith("http"):
            problems.append(f"abbreviations.toml: {a.get('abbr')}: needs a source URL")

    if problems:
        raise DataError("\n".join(problems))
    return {"categories": categories, "concepts": concepts, "edges": sorted(edges),
            "books": books, "abbreviations": abbreviations}


# --- paths and links ---------------------------------------------------------


def concept_page(d: dict, slug: str) -> Path:
    return CONCEPTS / d["concepts"][slug]["category"] / slug / "README.md"


def category_page(slug: str) -> Path:
    return CONCEPTS / slug / "README.md"


def books_page(focus: str) -> Path:
    return RESOURCES / f"books_{focus}" / "README.md"


def rel(page: Path, target: Path) -> str:
    return os.path.relpath(target, page.parent)


def external(text: str) -> str:
    """Give every external link in `text` its ↗, as the link-style gate requires."""
    def fix(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://")) and not label.rstrip().endswith(MARK):
            label = f"{label.rstrip()} {MARK}"
        return f"[{label}]({href})"
    return LINK.sub(fix, text)


def ext(label: str, url: str) -> str:
    return f"[{label} {MARK}]({url})"


def clink(d: dict, page: Path, slug: str) -> str:
    return f"[{d['concepts'][slug]['title']}]({rel(page, concept_page(d, slug))})"


def h1_of(readme: Path) -> str:
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return readme.parent.name


def mermaid_id(slug: str) -> str:
    return "n_" + slug


def mermaid_label(text: str) -> str:
    return text.replace('"', "#quot;").replace("`", "")


# --- rendering ---------------------------------------------------------------


def neighbours(d: dict, slug: str) -> dict[tuple[str, bool], list[str]]:
    out: dict[tuple[str, bool], list[str]] = defaultdict(list)
    for a, rel_, b in d["edges"]:
        symmetric = RELATIONS[rel_][3]
        if a == slug:
            out[(rel_, True)].append(b)
        elif b == slug:
            out[(rel_, True if symmetric else False)].append(a)
    for key in out:
        out[key].sort(key=lambda s: d["concepts"][s]["title"].lower())
    return out


def mermaid(d: dict, edges: list[tuple[str, str, str]], focus: set[str], center: str | None = None) -> list[str]:
    drawn = [(a, r, b) for a, r, b in edges if RELATIONS[r][4]]
    if not drawn:
        return []
    nodes = sorted({x for a, _, b in drawn for x in (a, b)}, key=lambda s: d["concepts"][s]["title"].lower())
    lines = ["```mermaid", "flowchart LR"]
    for n in nodes:
        lines.append(f'  {mermaid_id(n)}["{mermaid_label(d["concepts"][n]["title"])}"]')
    for a, r, b in drawn:
        arrow = "---" if RELATIONS[r][3] else "-->"
        lines.append(f"  {mermaid_id(a)} {arrow}|{RELATIONS[r][4]}| {mermaid_id(b)}")
    outside = [n for n in nodes if n not in focus]
    if center:
        lines.append(f"  classDef center stroke-width:3px")
        lines.append(f"  class {mermaid_id(center)} center")
    if outside:
        lines.append("  classDef outside stroke-dasharray: 4 3")
        lines.append(f"  class {','.join(mermaid_id(n) for n in outside)} outside")
    lines.append("```")
    return lines


def chapter_text(page: Path, number: int) -> str:
    title = CHAPTERS[number]
    folders = sorted(REPO.glob(f"{number:02d}_*/README.md"))
    if folders:
        return f"**Lessons:** [chapter {number:02d}, {title}]({rel(page, folders[0])})"
    return f"**Lessons:** chapter {number:02d}, {title} *(planned)*"


def render_concept(d: dict, slug: str) -> str:
    c = d["concepts"][slug]
    page = concept_page(d, slug)
    cat = next(x for x in d["categories"] if x["slug"] == c["category"])
    meta = [f"**Category:** [{cat['title']}]({rel(page, category_page(cat['slug']))})",
            f"**Status:** {c.get('status', 'stub')}"]
    if "chapter" in c:
        meta.append(chapter_text(page, c["chapter"]))
    out = [f"# {c['title']}", "", " · ".join(meta), "", f"**One line:** {external(c['summary'])}", ""]
    if c.get("aliases"):
        out += [f"Also called: {', '.join(c['aliases'])}.", ""]

    near = neighbours(d, slug)
    if near:
        out += ["## How it connects", ""]
        mine = [(a, r, b) for a, r, b in d["edges"] if slug in (a, b)]
        out += mermaid(d, mine, {slug}, center=slug) + [""]
        for rel_, forward in RELATION_ORDER:
            targets = near.get((rel_, forward))
            if targets:
                label = RELATIONS[rel_][0 if forward else 1]
                out.append(f"- **{label}:** " + ", ".join(clink(d, page, t) for t in targets))
        out.append("")

    langs = c.get("languages", {})
    if langs:
        out += ["## In each language", "", "| | |", "|---|---|"]
        for key, name in LANGS:
            if key in langs:
                out.append(f"| {name} | {external(langs[key])} |")
        out.append("")

    more: list[str] = []
    for folder in c.get("lessons", []):
        readme = REPO / folder / "README.md"
        more.append(f"- **In this library:** [{h1_of(readme).replace('`', '')}]({rel(page, readme)})")
    for label, url in c.get("pages", []):
        more.append(f"- **In a sibling library:** {ext(label, url)}")
    for book_id, where in c.get("books", []):
        b = d["books"][book_id]
        authors = ", ".join(b.get("authors", []))
        more.append(f"- **In the books:** [*{b['title']}*]({rel(page, books_page(b['focus']))}#{book_id}), {authors} — {where}")
    for label, url in c.get("notes", []):
        more.append(f"- **Notes:** {ext(label, url)}")
    for label, url in c.get("reference", []):
        more.append(f"- **Reference:** {ext(label, url)}")
    if more:
        out += ["## Where to read more", ""] + more + [""]
    return "\n".join(out)


def tree(d: dict, page: Path, slugs: list[str]) -> list[str]:
    """Concepts in a category as a nested list: a concept sits under what it is a kind of."""
    inside = set(slugs)
    parent: dict[str, str] = {}
    for a, r, b in d["edges"]:
        if r == "is_a" and a in inside and b in inside and a not in parent:
            parent[a] = b
    kids: dict[str | None, list[str]] = defaultdict(list)
    for s in slugs:
        kids[parent.get(s)].append(s)
    lines: list[str] = []

    def walk(node: str | None, depth: int) -> None:
        for s in kids.get(node, []):
            c = d["concepts"][s]
            lines.append(f"{'    ' * depth}- {clink(d, page, s)} — {external(c['summary'])}")
            walk(s, depth + 1)
    walk(None, 0)
    return lines


def render_category(d: dict, cat: dict) -> str:
    page = category_page(cat["slug"])
    out = [f"# {cat['title']}", "", cat["blurb"], "", f"[All categories](../README.md) · [How they connect](../schema/README.md)", ""]
    out += tree(d, page, cat["slugs"]) + [""]
    inner = [(a, r, b) for a, r, b in d["edges"] if a in cat["slugs"] and b in cat["slugs"]]
    diagram = mermaid(d, inner, set(cat["slugs"]))
    if diagram:
        out += ["## Inside this category", ""] + diagram + [""]
    return "\n".join(out)


def render_ontology(d: dict) -> str:
    page = CONCEPTS / "README.md"
    out = []
    for cat in d["categories"]:
        out += [f"## [{cat['title']}]({rel(page, category_page(cat['slug']))})", "", cat["blurb"], ""]
        out += tree(d, page, cat["slugs"]) + [""]
    return "\n".join(out)


def render_schema(d: dict) -> str:
    page = CONCEPTS / "schema" / "README.md"
    cat_of = {s: c["category"] for s, c in d["concepts"].items()}
    titles = {c["slug"]: c["title"] for c in d["categories"]}
    out = ["## The relations", "", "| Relation | Read it as | On the other page |", "|---|---|---|"]
    for key, (fwd, inv, _, symmetric, _) in RELATIONS.items():
        out.append(f"| `{key}` | A — *{fwd.lower()}* — B | " + ("the same, both ways" if symmetric else f"B — *{inv.lower()}* — A") + " |")
    out += ["", "## Between categories", "",
            "Each arrow counts the connections from concepts in one category to concepts in another.", "",
            "```mermaid", "flowchart LR"]
    for cat in d["categories"]:
        out.append(f'  c_{cat["slug"]}["{mermaid_label(cat["title"])}"]')
    counts: dict[tuple[str, str], int] = defaultdict(int)
    for a, r, b in d["edges"]:
        if r != "related" and cat_of[a] != cat_of[b]:
            counts[(cat_of[a], cat_of[b])] += 1
    for (x, y), n in sorted(counts.items()):
        out.append(f"  c_{x} -->|{n}| c_{y}")
    out += ["```", ""]
    for cat in d["categories"]:
        touching = [(a, r, b) for a, r, b in d["edges"] if (cat_of[a] == cat["slug"] or cat_of[b] == cat["slug"]) and r != "related"]
        diagram = mermaid(d, touching, set(cat["slugs"]))
        if diagram:
            out += [f"## {titles[cat['slug']]}", "",
                    "Dashed boxes belong to other categories.", ""] + diagram + [""]
    out += ["## Every connection", "", "| Concept | Relation | Concept |", "|---|---|---|"]
    for a, r, b in d["edges"]:
        out.append(f"| {clink(d, page, a)} | {RELATIONS[r][0].lower()} | {clink(d, page, b)} |")
    out.append("")
    return "\n".join(out)


def render_abbreviations(d: dict) -> str:
    page = CONCEPTS / "abbreviations" / "README.md"
    out = ["# Abbreviations", "",
           "The short forms that turn up in concurrency books and documentation. Each has a source; an abbreviation we could not find a source for is left out rather than guessed at.", "",
           "| Short form | Stands for | Concept | Source |", "|---|---|---|---|"]
    for a in sorted(d["abbreviations"], key=lambda x: x["abbr"].lower()):
        concept = clink(d, page, a["concept"]) if a.get("concept") else ""
        out.append(f"| {a['abbr']} | {external(a['expansion'])} | {concept} | {ext('source', a['source'])} |")
    out.append("")
    return "\n".join(out)


def render_keywords(d: dict) -> str:
    """Every concept title and alias, alphabetically, pointing at its concept page."""
    page = CONCEPTS / "keywords" / "README.md"
    cat_title = {c["slug"]: c["title"] for c in d["categories"]}
    rows = []
    for slug, c in d["concepts"].items():
        rows.append((c["title"], slug, ""))
        for alias in c.get("aliases", []):
            rows.append((alias, slug, c["title"]))
    rows.sort(key=lambda r: (r[0].lower().lstrip("`"), r[1]))
    out = ["# Keywords", "",
           f"Every name a concept goes by — {len(d['concepts'])} titles and {len(rows) - len(d['concepts'])} aliases, "
           "one row each — pointing at the concept's page, which has the definition, the diagram of what it connects to, "
           "its name in each language and the lessons that measure it. The [abbreviations](../abbreviations/README.md) page "
           "has the short forms; this page has the words.", "",
           "| Keyword | Concept | Category |", "|---|---|---|"]
    for word, slug, canonical in rows:
        c = d["concepts"][slug]
        target = clink(d, page, slug) if not canonical else f"{clink(d, page, slug)}"
        cat = f"[{cat_title[c['category']]}](../{c['category']}/README.md)"
        label = external(word) if canonical else f"**{external(word)}**"
        out.append(f"| {label} | {target} | {cat} |")
    out.append("")
    return "\n".join(out)


def render_books_index(d: dict) -> str:
    page = RESOURCES / "README.md"
    rows = ["| Focus | Books | On the shelf | Whole-book concurrency titles |", "|---|---|---|---|"]
    for focus, title in FOCUS:
        books = [b for b in d["books"].values() if b["focus"] == focus]
        if books:
            shelf = sum(1 for b in books if b.get("on_shelf"))
            dedicated = sum(1 for b in books if b.get("dedicated"))
            rows.append(f"| [{title}]({rel(page, books_page(focus))}) | {len(books)} | {shelf} | {dedicated} |")
    return "\n".join(rows)


def render_books(d: dict, focus: str, title: str) -> str:
    page = books_page(focus)
    cited: dict[str, list[str]] = defaultdict(list)
    for slug, c in d["concepts"].items():
        for book_id, _ in c.get("books", []):
            cited[book_id].append(slug)
    books = sorted((b for b in d["books"].values() if b["focus"] == focus),
                   key=lambda b: (not b.get("dedicated", False), -int(b.get("year") or 0), b["title"]))
    out = [f"# Concurrency books — {title}", "",
           "[All book lists](../README.md#books) · [Concepts](../../11_Concepts/README.md)", ""]
    for b in books:
        heading = f"*{b['title']}*" + (f": {b['subtitle']}" if b.get("subtitle") else "")
        out += [f'<a id="{b["id"]}"></a>', "", f"## {heading}", ""]
        facts = [", ".join(b.get("authors", []))]
        edition = str(b.get("edition") or "")
        if edition and "edition" not in edition.lower() and "draft" not in edition.lower():
            edition += " edition"
        facts += [x for x in (edition, b.get("publisher"), str(b["year"]) if b.get("year") else "") if x]
        out.append(" · ".join(f for f in facts if f) + ("  " if True else ""))
        links = []
        if b.get("free_url"):
            links.append(ext("read it free", b["free_url"]))
        if b.get("publisher_url"):
            links.append(ext("publisher", b["publisher_url"]))
        if b.get("code_repo"):
            links.append(ext("example code", b["code_repo"]))
        flags = ["dedicated to concurrency" if b.get("dedicated") else "a concurrency chapter in a broader book"]
        if b.get("on_shelf"):
            flags.append("on the shelf")
        out += [" · ".join(flags + links), ""]
        if b.get("chapters"):
            label = "Chapters" if b.get("dedicated") else "The concurrency chapters"
            out += ['<details markdown="1">', f"<summary>{label}</summary>", ""]
            # "1. Title" inside a bullet would render as a nested ordered list; bold the number instead.
            for ch in b["chapters"]:
                m = re.match(r"^(\w{1,4})\.\s+(.*)$", ch)
                out.append(f"- **{m.group(1)}** {m.group(2)}" if m else f"- {ch}")
            out += ["", "</details>", ""]
        if cited.get(b["id"]):
            names = sorted(cited[b["id"]], key=lambda s: d["concepts"][s]["title"].lower())
            out += ["Cited on: " + ", ".join(clink(d, page, s) for s in names), ""]
    return "\n".join(out)


# --- writing -----------------------------------------------------------------


def with_hand(generated: str, path: Path) -> str:
    """The generated part, the HAND marker, and whatever was already written below it."""
    kept = ""
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if HAND in old:
            kept = old.split(HAND, 1)[1]
    return generated.rstrip("\n") + "\n\n" + HAND + (kept if kept else "\n")


def with_block(generated: str, path: Path, name: str) -> str:
    old = path.read_text(encoding="utf-8")
    pattern = re.compile(rf"(<!-- concepts:{name} -->\n).*?(<!-- /concepts:{name} -->)", re.DOTALL)
    if not pattern.search(old):
        raise DataError(f"{path.relative_to(REPO)}: no <!-- concepts:{name} --> block")
    return pattern.sub(lambda m: m.group(1) + "\n" + generated.strip("\n") + "\n\n" + m.group(2), old)


def planned(d: dict) -> dict[Path, str]:
    files: dict[Path, str] = {}
    for slug in d["concepts"]:
        path = concept_page(d, slug)
        files[path] = with_hand(render_concept(d, slug), path)
    for cat in d["categories"]:
        path = category_page(cat["slug"])
        files[path] = with_hand(render_category(d, cat), path)
    for name, render, path in (
        ("ontology", render_ontology, CONCEPTS / "README.md"),
        ("schema", render_schema, CONCEPTS / "schema" / "README.md"),
    ):
        if path.exists():
            files[path] = with_block(render(d), path, name)
    index = RESOURCES / "README.md"
    if d["books"] and index.exists() and "<!-- concepts:books -->" in index.read_text(encoding="utf-8"):
        files[index] = with_block(render_books_index(d), index, "books")
    if d["abbreviations"]:
        path = CONCEPTS / "abbreviations" / "README.md"
        files[path] = with_hand(render_abbreviations(d), path)
    path = CONCEPTS / "keywords" / "README.md"
    files[path] = with_hand(render_keywords(d), path)
    for focus, title in FOCUS:
        if any(b["focus"] == focus for b in d["books"].values()):
            path = books_page(focus)
            files[path] = with_hand(render_books(d, focus, title), path)
    return files


def stale_pages(d: dict, files: dict[Path, str]) -> list[Path]:
    """Generated pages whose concept, category or book list no longer exists."""
    stale = []
    for readme in CONCEPTS.glob("*/*/README.md"):
        text = readme.read_text(encoding="utf-8")
        if HAND in text and readme not in files:
            stale.append(readme)
    for readme in RESOURCES.glob("books_*/README.md"):
        if HAND in readme.read_text(encoding="utf-8") and readme not in files:
            stale.append(readme)
    return stale


def check_links(d: dict) -> list[str]:
    urls: set[str] = set()
    for c in d["concepts"].values():
        for field in ("pages", "notes", "reference"):
            urls.update(u for _, u in c.get(field, []))
        for text in list(c.get("languages", {}).values()) + [c["summary"]]:
            urls.update(m.group(2) for m in LINK.finditer(text) if m.group(2).startswith("http"))
    for b in d["books"].values():
        urls.update(u for u in (b.get("free_url"), b.get("publisher_url"), b.get("code_repo")) if u)
    urls.update(a["source"] for a in d["abbreviations"])
    bad = []
    for url in sorted(urls):
        if "docs.google.com" in url:
            continue  # private notes: a login page is the expected answer
        done = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-L", "--max-time", "25", "-A", "Mozilla/5.0", "-w", "%{http_code}", url],
            capture_output=True, text=True)
        code = done.stdout.strip()
        if code not in {"200"}:
            bad.append(f"{code or 'no answer'}  {url}")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="write nothing; fail on bad data or drift")
    ap.add_argument("--links", action="store_true", help="also fetch every external URL (network)")
    ap.add_argument("--validate", action="store_true",
                    help="check the data and render in memory; write nothing, ignore drift")
    args = ap.parse_args()
    try:
        d = load()
        files = planned(d)
    except DataError as e:
        print(f"concept data problems:\n{e}")
        return 1
    if args.validate:
        bad_links = check_links(d) if args.links else []
        for line in bad_links:
            print(f"  link      {line}")
        print(f"data ok: {len(d['concepts'])} concepts, {len(d['edges'])} connections, "
              f"{len(files)} pages would be written.")
        return 1 if bad_links else 0

    drift = [p for p, text in files.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    stale = stale_pages(d, files)
    if args.check:
        for p in drift:
            print(f"  stale     {p.relative_to(REPO)}")
        for p in stale:
            print(f"  orphan    {p.relative_to(REPO)} (its data entry is gone)")
    else:
        for p in drift:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(files[p], encoding="utf-8")
            print(f"  wrote     {p.relative_to(REPO)}")
        for p in stale:
            print(f"  orphan    {p.relative_to(REPO)} — delete it, or restore its data entry")

    bad_links = check_links(d) if args.links else []
    for line in bad_links:
        print(f"  link      {line}")

    print(f"\n{len(d['concepts'])} concepts in {len(d['categories'])} categories, "
          f"{len(d['edges'])} connections, {len(d['books'])} books, {len(d['abbreviations'])} abbreviations.")
    if args.check and (drift or stale):
        print("Generated pages are out of date — run python3 tools/build_concepts.py")
        return 1
    if stale or bad_links:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
