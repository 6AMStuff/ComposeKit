from pathlib import Path


def iter_container_files(containers_folder: str) -> list[Path]:
    return sorted(
        p
        for p in Path(containers_folder).iterdir()
        if p.is_file() and p.suffix in {".yml", ".yaml"}
    )
