"""Tests for the cleaning module"""
import pandas as pd
from unittest.mock import patch

from life_expectancy.cleaning import clean_data


def test_clean_data(input_fixture, output_fixture):
    """Run the `clean_data` function and compare the output to the expected output"""

    eu_life_expectancy_actual = clean_data(input_fixture, country_arg = "PT")

    pd.testing.assert_frame_equal(
        eu_life_expectancy_actual, output_fixture
    )