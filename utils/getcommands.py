from pathlib import Path
import os


def get_extensions():
    here = Path(__file__).parent.parent
    path = 'Commands'
    for f in (here / path).iterdir():
        if f.is_file():
            pathname = str(f.relative_to(here))
            if pathname[-3:] != ".py":
                continue
            yield pathname[:-3].replace("/", ".").replace("\\", ".")