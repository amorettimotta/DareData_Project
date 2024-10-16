#sample file
from pathlib import Path
import pandas as pd
from life_expectancy.loading_saving import TsvFileStrategy, save_cleaned_data
from life_expectancy.cleaning import clean_data

#from . import FIXTURES_DIR, OUTPUT_DIR

def load_and_sample_data() -> pd.DataFrame:
    """Fixture to load a sample of the input data for testing."""

    #df = load_dataset(OUTPUT_DIR / "eu_life_expectancy_raw.tsv")
    tsv_strategy = TsvFileStrategy()
    file_path = Path(__file__).parents[1] / "data" / "eu_life_expectancy_raw.tsv"

    # Utilizar a estratégia para ler o arquivo TSV
    sample_df = tsv_strategy.read(file_path).sample(50)

    #save_cleaned_data(sample_df, FIXTURES_DIR / "eu_life_expectancy_raw.tsv")
    save_cleaned_data(sample_df, Path(__file__).parent / "fixtures" / "eu_life_expectancy_raw.tsv")

    return sample_df

def expected_result_function(sample_df) -> pd.DataFrame:
    """Fixture to generate the expected result based on the sample data."""
    expected_result = clean_data(sample_df)

    #save_cleaned_data(expected_result, FIXTURES_DIR / "eu_life_expectancy_expected.csv")
    save_cleaned_data(expected_result, Path(__file__).parent / "fixtures" /
                      "eu_life_expectancy_expected.csv", ",")   

    return expected_result

if __name__ == "__main__": # pragma: no cover
    input_df = load_and_sample_data()
    expected_result_function(input_df)
