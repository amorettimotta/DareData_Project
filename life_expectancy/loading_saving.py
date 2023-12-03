# loading_saving
from pathlib import Path
import sys
import argparse
import pandas as pd
from life_expectancy.cleaning import clean_data
#from . import OUTPUT_DIR

def load_dataset(file_path, separator):
    original_df = pd.read_csv(file_path, sep=separator)
    return original_df

def save_cleaned_data(original_df, saving_path, separator="\t"): 
    original_df.to_csv(saving_path, index=False, sep=separator)

# Isto deve sair daqui para um ficheiro à parte usado para invocar as funcoes do programa. Confirmar com o Prof.
if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser(prog='cleaning.py', description="Script to clean a dataset")
    parser.add_argument('--country', type=str, nargs='*', help= 'Country to filter the dataframe')
    args = parser.parse_args()

    #original_df = load_dataset(OUTPUT_DIR / "eu_life_expectancy_raw.tsv")
    original_df = load_dataset(Path(__file__).parent / "data" / "eu_life_expectancy_raw.tsv", '\t')

    if len(sys.argv) > 1:
        df_cleaned = clean_data(original_df, args.country[0])
    else:
        df_cleaned = clean_data(original_df)

    #save_cleaned_data(df_cleaned, OUTPUT_DIR / "pt_life_expectancy.csv")
    save_cleaned_data(df_cleaned, Path(__file__).parent / "data"/ "pt_life_expectancy.csv", ',')