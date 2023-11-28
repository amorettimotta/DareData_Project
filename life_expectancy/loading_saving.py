# loading_saving
import re
from pathlib import Path
import sys
import argparse
import pandas as pd
from life_expectancy.cleaning import clean_data

def load_dataset():
    script_dir = Path(__file__).parent
    data_path = script_dir / "data" / "eu_life_expectancy_raw.tsv"
    df = pd.read_csv(data_path, sep='\t')
    return df


def save_cleaned_data(original_df, country_arg='PT'):
    df_cleaned = clean_data(original_df, country_arg)
    script_dir = Path(__file__).parent
    csv_path = script_dir / "data" / "pt_life_expectancy.csv"
    df_cleaned.to_csv(csv_path, index=False)

if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser(prog='cleaning.py', description="Script to clean a dataset")
    parser.add_argument('--country', type=str, nargs='*', help= 'Country to filter the dataframe')
    args = parser.parse_args()

    original_df = load_dataset()

    if len(sys.argv) > 1:
        df_cleaned = clean_data(original_df, args.country[0])
    else:
        df_cleaned = clean_data(original_df)

    save_cleaned_data(df_cleaned)
