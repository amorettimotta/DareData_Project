"""Pytest fixtures file"""
import pandas as pd
from pathlib import Path
from life_expectancy.loading_saving import load_dataset
from life_expectancy.cleaning import clean
#from . import FIXTURES_DIR

def load_and_sample_data() -> pd.DataFrame:
    """Fixture to load a sample of the input data for testing."""
    df = load_dataset()
    sample_df = df.sample(50)

    # Save the sample as a TSV file
    sample_file_path = Path(__file__).parent / "fixtures" / "eu_life_expectancy_raw.tsv"

    save_sample(sample_df, sample_file_path)

    return sample_df

def expected_result_function() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    output_df = load_sample(Path(__file__).parent / "fixtures" / "eu_life_expectancy_raw.tsv")
    
    output_df.columns.values[0] = 'unit,sex,age,geo_time'

    output_df[['unit', 'sex', 'age', 'geo_time']] = output_df['unit,sex,age,geo_time'].str.split(',', expand=True)
    
    output_df.drop('unit,sex,age,geo_time', axis=1, inplace=True)

    output_df = pd.melt(output_df, id_vars=['unit', 'sex', 'age', 'geo_time'],
                 var_name='year', value_name='value')

    output_df.columns.values[3] = 'region'

    output_df['year'] = output_df['year'].astype(int)

    output_df['value'] = output_df['value'].astype(str)
    output_df['value'] = output_df['value'].apply(clean)

    output_df['value'] = output_df['value'].replace('', pd.NA)
    output_df = output_df.dropna(subset=['value'])

    output_df['region'] = output_df['region'].str.extract(r'([A-Z]{2})', expand=False)
    output_df['value'] = output_df['value'].astype(float)

    filtered_df= output_df[output_df['region'] == "PT"]

    # Save the sample as a CSV file
    file_path = Path(__file__).parent / "fixtures" / "eu_life_expectancy_expected.csv"
    filtered_df.to_csv(file_path, index=False)

    return pd.DataFrame(filtered_df)

def save_sample(df, file_path):
    df.to_csv(file_path, sep='\t', index=False)

def load_sample(file_path):
    df = pd.read_csv(file_path, sep='\t', header=0)
    return df

if __name__ == "__main__": # pragma: no cover
    input_df = load_and_sample_data()
    expected_df = expected_result_function()