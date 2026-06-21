from pathlib import Path


ROOT = Path(__file__).absolute().parents[1]

DATA_DIR = ROOT / "data"

RAW_DIR = DATA_DIR / "raw"

SRC_DIR = ROOT / "src"

NOTEBOOKS_DIR = ROOT / "notebooks"

FIGURES_DIR = ROOT / "figures"

repos = [DATA_DIR,
        RAW_DIR,
        NOTEBOOKS_DIR,
        FIGURES_DIR ]

for repo in repos:
    repo.mkdir(parents = True, exist_ok = True)



RAW_DATA = RAW_DIR / "communes_light_2022.csv"

