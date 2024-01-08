# loading_saving
from pathlib import Path
import argparse
import pandas as pd
from life_expectancy.cleaning import clean_data, Region

class FileStrategy:
    def read(self, file_path):
        pass

# Ler ficheiros em diferentes formatos CSV, TSV, JSON
class CsvFileStrategy(FileStrategy):
    def read(self, file_path):
        return pd.read_csv(file_path, sep=',')

class TsvFileStrategy(FileStrategy):
    def read(self, file_path):
        return pd.read_csv(file_path, sep='\t')

class JsonFileStrategy(FileStrategy):
    def read(self, file_path):
        return pd.read_json(file_path)

# salvar os dados limpos
def save_cleaned_data(original_df, saving_path, separator="\t"):
    original_df.to_csv(saving_path, index=False, sep=separator)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='cleaning.py',
                                     description="Script to clean a dataset")
    parser.add_argument('--country', type=Region, nargs='*',
                        help='Country to filter the dataframe')
    parser.add_argument('--file_type', choices=['csv', 'tsv', 'json'],
                        default='tsv',
                        help='Type of file to read/save')

    args = parser.parse_args()

    # Verificar se o argumento --file_type foi fornecido
    if not args.file_type:
        raise ValueError("Please provide --file_type argument")

    # Selecionar a estratégia com base no tipo de arquivo fornecido
    if args.file_type == 'csv':
        strategy = CsvFileStrategy()
    elif args.file_type == 'tsv':
        strategy = TsvFileStrategy()
    elif args.file_type == 'json':
        strategy = JsonFileStrategy()
    else:
        raise ValueError("Invalid file type")

    # Utilizar a estratégia para ler o ficheiro

    file_type = args.file_type or 'tsv'

    if args.file_type is None or args.file_type == 'tsv':
        input_df = strategy.read(Path(__file__).parent / "data" / "eu_life_expectancy_raw.tsv")
        if args.country:
            country_enum = Region(args.country[0])
            df_cleaned = clean_data(input_df, country_enum)
        else:
            df_cleaned = clean_data(input_df)
    elif file_type == 'json':
        input_df = strategy.read(Path(__file__).parent / "data" / "eurostat_life_expect.json")
        df_cleaned = input_df
    else:
        raise ValueError("Invalid file type")


    print(df_cleaned)

    # Utilizar a estratégia para salvar o ficheiro (em formato csv especificamente)
    save_cleaned_data(df_cleaned, Path(__file__).parent / "data"/ "pt_life_expectancy.csv", ',')
