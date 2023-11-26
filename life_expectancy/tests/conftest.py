# conftest.py
import pytest
from life_expectancy.tests.fixture_functions import load_and_sample_data, expected_result_function
#from . import FIXTURES_DIR

@pytest.fixture(scope="session")
def input_fixture():
    return load_and_sample_data()

@pytest.fixture(scope="session")
def output_fixture():
    return expected_result_function()