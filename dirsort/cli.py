#!/usr/bin/env python3
"""Top-level file organizer.

- Organizes only files directly inside the target directory.
- Does NOT recurse into child directories.
- Moves files into numbered category folders: 00_pdf, 01_photo, 02_documents, ...
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

# Category order controls folder numbering.
CATEGORY_RULES: list[tuple[str, set[str]]] = [
    ("pdf", {".pdf"}),
    (
        "image",
        {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".heic", ".heif"},
    ),
    ("doc", {".hwp", ".hwpx", ".doc", ".docx", ".txt", ".rtf", ".odt"}),
    ("excel", {".xls", ".xlsx", ".xlsm", ".xlsb", ".csv"}),
    ("ppt", {".ppt", ".pptx"}),
    ("video", {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"}),
    ("audio", {".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"}),
    ("archive", {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"}),
    ("ebook", {".epub", ".mobi"}),
    ("font", {".ttf", ".otf", ".woff", ".woff2"}),
    (
        "code",
        {".py", ".js", ".ts", ".java", ".c", ".cpp", ".html", ".css", ".json", ".xml", ".yaml", ".yml"},
    ),
    ("executable", {".exe", ".dmg", ".pkg", ".deb", ".msi", ".app"}),
]


def build_extension_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for category, exts in CATEGORY_RULES:
        for ext in exts:
            mapping[ext] = category
    return mapping


def unique_destination(dest_dir: Path, original_name: str) -> Path:
    """Return a non-conflicting path in dest_dir.

    example.pdf -> example (1).pdf if file already exists.
    """
    candidate = dest_dir / original_name
    if not candidate.exists():
        return candidate

    src = Path(original_name)
    stem, suffix = src.stem, src.suffix
    i = 1
    while True:
        candidate = dest_dir / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def collect_top_level_files(target_dir: Path) -> list[Path]:
    return [p for p in target_dir.iterdir() if p.is_file()]


def find_existing_category_dir(target_dir: Path, category: str) -> Path | None:
    """Find an existing folder for the category regardless of its numeric prefix."""
    for p in target_dir.iterdir():
        if p.is_dir() and p.name.split("_", 1)[-1] == category:
            return p
    return None


def ensure_dirs(target_dir: Path, active_categories: list[str], dry_run: bool) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for category in active_categories:
        existing = find_existing_category_dir(target_dir, category)
        if existing:
            out[category] = existing
        else:
            idx = next(i for i, (name, _) in enumerate(CATEGORY_RULES) if name == category)
            folder = target_dir / f"{idx:02d}_{category}"
            out[category] = folder
            if not dry_run:
                folder.mkdir(exist_ok=True)
    return out


def organize(target_dir: Path, dry_run: bool = False) -> tuple[int, int]:
    ext_map = build_extension_map()
    files = collect_top_level_files(target_dir)

    grouped: dict[str, list[Path]] = {}
    skipped = 0

    for file_path in files:
        category = ext_map.get(file_path.suffix.lower())
        if category is None:
            skipped += 1
            print(f"[SKIP] {file_path.name} (unsupported extension)")
            continue
        grouped.setdefault(category, []).append(file_path)

    if not grouped:
        print("No matching files found.")
        return 0, skipped

    active_categories = [name for name, _ in CATEGORY_RULES if name in grouped]
    destination_dirs = ensure_dirs(target_dir, active_categories, dry_run)

    moved = 0
    for category in active_categories:
        dest_dir = destination_dirs[category]
        for src in grouped[category]:
            dest = unique_destination(dest_dir, src.name)
            if dry_run:
                print(f"[DRY-RUN] MOVE {src} -> {dest}")
            else:
                shutil.move(str(src), str(dest))
                print(f"[MOVED] {src.name} -> {dest_dir.name}/{dest.name}"  if dest.name != src.name else f"[MOVED] {src.name} -> {dest_dir.name}/")
            moved += 1

    return moved, skipped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organize top-level files in a directory by type (no recursion)."
    )
    parser.add_argument("target_dir", nargs="?", type=Path, default=Path.cwd(), help="Directory to organize (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes only")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_dir = args.target_dir

    if not target_dir.exists():
        raise SystemExit(f"Target does not exist: {target_dir}")
    if not target_dir.is_dir():
        raise SystemExit(f"Target is not a directory: {target_dir}")

    moved, skipped = organize(target_dir, dry_run=args.dry_run)
    print(f"Done. moved={moved}, skipped={skipped}, dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
