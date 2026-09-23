"""Build-time fixes that would otherwise cost a pinned plugin dependency.

Three jobs, all about the sidebar. This file is the Ruby text library's (which
is the C library's without its TAB check), with its own reading order:

1. **Clean chapter labels.** MkDocs derives a section label from the folder name
   on disk, so `01_Strings_Carry_an_Encoding/` reads as "01 Strings Carry An
   Encoding". The numeric prefix exists to set reading order in a file listing;
   it should not be visible in the nav. Only *prefixed* folders are relabelled
   from their name — a lesson folder takes its README's own H1 (job 3).

2. **Order the sections.** `NAV_ORDER` states the intended reading order per
   folder, keyed by folder path, listing children by their on-disk name.

3. **Label lessons from their H1.** Left alone, MkDocs titles a lesson folder
   from its name, so `w_is_ascii_b_is_not` reads "W is ascii b is not" — and
   `mkdocs build --strict` passes either way. A lesson folder takes its README's
   H1 instead, backticks dropped. `LABEL_OVERRIDES` holds the exceptions: an H1
   too long for a sidebar.

Why order here rather than by renaming files: a filename is a permanent URL.
Renumbering `03_` to `04_` to insert a chapter would move every page after it
and break any link anyone saved. Ordering is presentation, so it belongs in the
presentation layer. Unlisted pages keep their alphabetical slot at the bottom.

One structural note that is easy to get wrong: the top-level object MkDocs hands
`on_nav` is a `Navigation`, whose children live on `.items`. Only `Section` has
`.children`. A hook that reaches for `.children` at the top level silently does
nothing at all — the build still succeeds, and the sidebar is simply never
touched.
"""

from __future__ import annotations

import re

PREFIX = re.compile(r"^(\d+)[_-]")

# Words the naive title-caser gets wrong.
FIXUPS = {
    "Vs": "vs",
    "And": "and",
    "Or": "or",
    "The": "the",
    "To": "to",
    "A": "a",
    "An": "an",
    "In": "in",
    "Of": "of",
}

# Lesson folders whose sidebar label is deliberately not their H1. Keyed by
# on-disk folder name. An entry naming a folder that no longer exists is a
# silent no-op, which tools/check_nav_chain.py reports.
LABEL_OVERRIDES: dict[str, str] = {}

# Reading order per folder path. Children named by on-disk name; anything not
# listed sorts alphabetically after the listed ones.
NAV_ORDER: dict[str, list[str]] = {
    "": [
        "index.md",
        "00_Start_Here",
        "01_Threads",
        "02_Shared_State",
        "03_When_Locks_Go_Wrong",
        "04_Waiting_For_Each_Other",
        "05_Message_Passing",
        "06_Async",
        "07_Parallelism",
        "08_Processes",
        "09_Testing_and_Tools",
        "11_Concepts",
        "10_Resources",
    ],
    # The edges of a thread's life. The end of the program comes first because
    # it is the question a first threaded program raises; then the value a
    # thread hands back, and the failure that travels the same way.
    "01_Threads": [
        "README.md",
        "who_waits_when_main_returns",
        "getting_a_result_back",
        "lending_a_local_to_a_thread",
        "a_failure_nobody_is_waiting_for",
        "how_many_threads_can_you_start",
        "a_variable_per_thread",
        "reusing_threads_in_a_pool",
        "a_goroutine_is_not_a_thread",
        "sleep_and_yield",
    ],
    # The smallest shared state there is: a total that handlers add to. First
    # how an addition is lost, then the ways to keep it, then the same bug in a
    # database, and last what besides timing can change a sum.
    "02_Shared_State": [
        "README.md",
        "the_lost_update",
        "keeping_every_update",
        "the_lost_update_in_a_database",
        "when_order_changes_a_sum",
        "data_race_or_race_condition",
        "two_values_that_must_change_together",
        "readers_and_writers",
        "a_torn_read",
        "check_then_act",
        "the_aba_problem",
        "what_may_cross_a_thread_boundary",
        "reordering_and_the_memory_model",
    ],
    # Using more cores to finish sooner. First the split itself: private partial
    # sums, and the two ways of combining them.
    "07_Parallelism": [
        "README.md",
        "splitting_a_sum_across_workers",
        "cpu_bound_speedup",
        "the_gil_and_free_threaded_python",
        "amdahls_law",
        "false_sharing",
        "data_parallel_or_task_parallel",
        "a_parallel_iterator",
        "fork_join",
        "map_and_reduce",
        "how_many_workers",
    ],
    "03_When_Locks_Go_Wrong": [
        "README.md",
        "two_locks_in_different_orders",
        "a_lock_taken_twice",
        "the_forgotten_unlock",
        "a_panic_while_holding_the_lock",
        "livelock",
        "starvation_and_fairness",
        "priority_inversion",
        "a_spinlock_on_one_core",
        "detecting_a_deadlock",
    ],
    "04_Waiting_For_Each_Other": [
        "README.md",
        "waiting_for_a_condition",
        "the_lost_wakeup",
        "a_semaphore_counts_permits",
        "a_barrier_and_a_latch",
        "run_exactly_once",
        "a_monitor_bundles_lock_and_condition",
        "the_bounded_buffer",
        "the_dining_philosophers",
        "waiting_with_a_timeout",
    ],
    "05_Message_Passing": [
        "README.md",
        "sending_a_value_moves_it",
        "an_unbuffered_send_waits",
        "a_bounded_queue_pushes_back",
        "closing_a_channel",
        "waiting_on_several_channels",
        "a_pipeline_of_stages",
        "fan_out_fan_in",
        "a_worker_pool",
        "one_owner_receives_the_numbers",
        "publish_and_subscribe",
    ],
    "06_Async": [
        "README.md",
        "what_an_event_loop_does",
        "a_future_is_a_value_not_yet_there",
        "async_and_await",
        "blocking_the_event_loop",
        "a_callback_and_its_state",
        "cancelling_an_async_task",
        "a_timeout_on_an_await",
        "function_coloring",
        "a_task_nobody_awaits",
        "an_async_stream",
        "who_runs_the_tasks",
        "io_multiplexing_under_the_loop",
        "the_ui_thread",
    ],
    "08_Processes": [
        "README.md",
        "fork_copies_the_process",
        "a_child_process_and_its_exit_status",
        "a_pipe_between_processes",
        "a_signal_arrives_on_some_thread",
        "multiprocessing_instead_of_threads",
        "shared_memory_between_processes",
        "a_zombie_and_an_orphan",
    ],
    "09_Testing_and_Tools": [
        "README.md",
        "a_race_detector_finds_what_happened",
        "a_memory_error_detector",
        "a_stress_test_that_actually_races",
        "virtual_time_in_tests",
        "model_checking_a_small_program",
        "reading_a_thread_dump",
        "profiling_where_the_time_goes",
        "a_heisenbug",
    ],
}


def _concept_nav() -> None:
    """11_Concepts takes its reading order from the data that generates it.

    tools/build_concepts.py writes a page per concept from
    11_Concepts/<category>/concepts.toml; listing some hundred and fifty folders here
    by hand would be a second copy of that data, and a stale one within a week.
    """
    import tomllib
    from pathlib import Path

    root = Path(__file__).resolve().parent / "11_Concepts"
    cats = []
    for path in root.glob("*/concepts.toml"):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        slugs = [c["slug"] for c in data.get("concept", [])]
        cats.append((data.get("category", {}).get("order", 99), path.parent.name, slugs))
    if not cats:
        return
    cats.sort()
    extras = [name for name in ("schema", "keywords", "abbreviations") if (root / name).is_dir()]
    NAV_ORDER["11_Concepts"] = ["README.md", *extras, *(name for _, name, _ in cats)]
    for _, name, slugs in cats:
        NAV_ORDER[f"11_Concepts/{name}"] = ["README.md", *slugs]


_concept_nav()


def _label(name: str) -> str:
    """Folder name on disk -> sidebar label."""
    words = PREFIX.sub("", name).replace("_", " ").replace("-", " ").split()
    out = [FIXUPS.get(w.capitalize(), w.capitalize()) for w in words]
    if out:
        out[0] = out[0][0].upper() + out[0][1:]
    return " ".join(out)


def _is_section(item) -> bool:
    return getattr(item, "children", None) is not None


def _first_src(item) -> str:
    """Source path of `item`, or of the first page anywhere beneath it."""
    page_file = getattr(item, "file", None)
    if page_file is not None:
        return page_file.src_uri
    for child in getattr(item, "children", None) or []:
        found = _first_src(child)
        if found:
            return found
    return ""


def _on_disk_name(item, depth: int) -> str:
    """The name NAV_ORDER lists this child by: a filename, or a folder segment."""
    src = _first_src(item)
    if not src:
        return (getattr(item, "title", "") or "").lower()
    parts = src.split("/")
    if not _is_section(item):
        return parts[-1]
    return parts[depth] if depth < len(parts) - 1 else parts[-1]


def _order_key(path: str, name: str) -> tuple[int, str]:
    listed = NAV_ORDER.get(path, [])
    if name in listed:
        return (listed.index(name), "")
    return (len(listed), name.lower())


def _readme_h1(section) -> str:
    """The H1 of a section's own README.md, read from disk ("" if it has none).

    Read from disk because MkDocs fills in a page's title only when it renders
    the page, long after `on_nav`. Backticks are dropped: the sidebar prints
    them as literal characters.
    """
    for child in section.children:
        page_file = getattr(child, "file", None)
        if page_file is None or page_file.src_uri.rsplit("/", 1)[-1] != "README.md":
            continue
        with open(page_file.abs_src_path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("# "):
                    return line[2:].strip().replace("`", "")
    return ""


def _visit(items: list, path: str, depth: int) -> None:
    for child in items:
        if not _is_section(child):
            continue
        name = _on_disk_name(child, depth)
        if name in LABEL_OVERRIDES:
            child.title = LABEL_OVERRIDES[name]
        elif PREFIX.match(name):
            child.title = _label(name)
        else:
            child.title = _readme_h1(child) or child.title

    items.sort(key=lambda c: _order_key(path, _on_disk_name(c, depth)))

    for child in items:
        if not _is_section(child):
            continue
        name = _on_disk_name(child, depth)
        _visit(child.children, f"{path}/{name}".lstrip("/"), depth + 1)


def _pages_in_nav_order(items: list) -> list:
    """Every page under `items`, depth-first, in the order the sidebar shows."""
    out = []
    for item in items:
        if item.is_page:
            out.append(item)
        elif item.is_section:
            out.extend(_pages_in_nav_order(item.children))
    return out


def on_nav(nav, config, files):
    """Relabel numbered chapters, apply NAV_ORDER, and re-chain prev/next."""
    _visit(nav.items, "", 0)

    # Sorting nav.items fixes the sidebar and nothing else. MkDocs computes every
    # page's previous_page/next_page inside get_navigation(), which runs BEFORE
    # this hook -- so without the re-chain below, the arrows at the foot of a
    # lesson walk the reader alphabetically while the sidebar beside them reads
    # in order. For a library with a reading order, the arrow IS the order.
    ordered = _pages_in_nav_order(nav.items)
    # Compared by source path, not by identity: MkDocs' Page defines __eq__
    # without __hash__, so a Page cannot go in a set.
    walked = {page.file.src_uri for page in ordered}
    known = {page.file.src_uri for page in nav.pages}
    assert walked == known, (
        "_pages_in_nav_order is out of step with mkdocs.structure.nav: "
        f"missed {sorted(known - walked)}, invented {sorted(walked - known)}"
    )
    for i, page in enumerate(ordered):
        page.previous_page = ordered[i - 1] if i else None
        page.next_page = ordered[i + 1] if i + 1 < len(ordered) else None
    nav.pages[:] = ordered

    return nav
