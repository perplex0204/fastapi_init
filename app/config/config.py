from dynaconf import Dynaconf
from pathlib import Path
import glob

__all__ = ("config",)

ROOT_DIR = Path(__file__).parent


def read_files(file_path: str) -> list:
    return [str(p) for p in ROOT_DIR.glob("default/*.yml")]


confs = read_files("default/*.yml")
config = Dynaconf(
    settings_files=confs,
    core_loaders=["YAML"],
    load_dotenv=True,
    root_path=ROOT_DIR,
)
