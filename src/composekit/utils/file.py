from pathlib import Path


def iter_container_files(containers_folder: str) -> list[Path]:
    folder = Path(containers_folder)
    if not folder.is_dir():
        raise SystemExit(f"containers folder not found: {folder}")

    return sorted(
        p
        for p in folder.iterdir()
        if p.is_file() and p.suffix in {".yml", ".yaml"}
    )
