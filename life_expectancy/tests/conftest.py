# conftest.py
import pandas as pd
import pytest
from pathlib import Path
from life_expectancy.loading_saving import load_dataset
#from . import FIXTURES_DIR

@pytest.fixture(scope="session")
def input_fixture() -> pd.DataFrame:
    df = load_dataset(Path(__file__).parent / "fixtures" / "eu_life_expectancy_raw.tsv", '\t')
    return df


@pytest.fixture(scope="session")
def output_fixture():
    df = load_dataset(Path(__file__).parent / "fixtures" / "eu_life_expectancy_expected.csv", ',')
    return df
