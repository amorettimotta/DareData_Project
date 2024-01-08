# conftest.py
from pathlib import Path
import pandas as pd
import pytest
from life_expectancy.loading_saving import TsvFileStrategy, CsvFileStrategy

def load_fixture(strategy_name, file_type):
    strategy = {
        'tsv': TsvFileStrategy(),
        'csv': CsvFileStrategy()
    }.get(strategy_name)

    if not strategy:
        raise ValueError(f"Invalid strategy name: {strategy_name}")

    file_path = (Path(__file__).parent / "fixtures" /
                f"eu_life_expectancy_{file_type}.{strategy_name}")
    df = strategy.read(file_path)
    return df

@pytest.fixture(scope="session", params=['tsv'])
def input_fixture(request) -> pd.DataFrame:
    return load_fixture(request.param, 'raw')

@pytest.fixture(scope="session", params=['csv'])
def output_fixture(request):
    return load_fixture(request.param, 'expected')
