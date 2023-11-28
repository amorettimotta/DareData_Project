"""Pytest fixtures file"""
import pandas as pd
from pathlib import Path
from life_expectancy.cleaning import load_dataset,clean
from . import FIXTURES_DIR

def load_and_sample_data() -> pd.DataFrame:
    """Fixture to load a sample of the input data for testing."""
    df = load_dataset()
    sample_df = df.sample(50)

    return sample_df


if __name__ == "__main__": # pragma: no cover
    input_df = load_and_sample_data()
    input_file_path = FIXTURES_DIR + "/eu_life_expectancy_raw.tsv"
    input_df.to_csv(input_file_path, sep='\t', index=False)
    
    output_file_path = FIXTURES_DIR + "/pt_life_expectancy_expected.csv"
    output_df = clean(input_df)
    output_df.to_csv(output_file_path, index=False)