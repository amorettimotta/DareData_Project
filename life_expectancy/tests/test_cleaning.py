"""Tests for the cleaning module"""
import pandas as pd
from unittest.mock import patch
from life_expectancy.cleaning import clean_data

def test_clean_data(input_fixture, output_fixture):
    """Run the `clean_data` function and compare the output to the expected output"""

    input_df = input_fixture
    eu_life_expectancy_actual = clean_data (input_df)

    eu_life_expectancy_expected = output_fixture

      # Reset indices
    eu_life_expectancy_actual.reset_index(drop=True, inplace=True)
    eu_life_expectancy_expected.reset_index(drop=True, inplace=True)


    pd.testing.assert_frame_equal(
        eu_life_expectancy_actual, eu_life_expectancy_expected
    )