# %%
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TestDataPaths:
    _root_dir: Path = Path(__file__).parent.parent
    _test_data_dir: Path = _root_dir / "test_data"

    _lens_model_dir: Path = _test_data_dir / "lens_model"
    lens_model_cat: Path = _lens_model_dir / "cat.png"
