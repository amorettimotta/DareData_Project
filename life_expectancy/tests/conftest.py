# conftest.py

import pytest
import pandas as pd
from . import FIXTURES_DIR

@pytest.fixture(scope="session")
def input_fixture():
    return pd.read_csv(FIXTURES_DIR + "/eu_life_expectancy_raw.tsv" , sep='\t')

@pytest.fixture(scope="session")
def output_fixture():
    return pd.read_csv(FIXTURES_DIR + "/pt_life_expectancy_expected.csv")