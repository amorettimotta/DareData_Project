import re
from pathlib import Path
import sys
import pandas as pd
import argparse

def clean_data(country_arg = 'PT'):
    # Carregar os dados do arquivo eu_life_expectancy_raw.tsv
    script_dir = Path(__file__).parent
    data_path = script_dir / "data" / "eu_life_expectancy_raw.tsv"
    df = pd.read_csv(data_path, sep='\t')

    # Alterar o nome da coluna geo\time para geo_time
    df.columns.values[0] = 'unit,sex,age,geo_time'

    # Split 'unit,sex,age,geo_time' into 'unit,' 'sex,'
    # 'age,' and 'geo_time' and drop 'geo_time'
    df[['unit', 'sex', 'age', 'geo_time']] = df['unit,sex,age,geo_time'].str.split(',', expand=True)

    df.drop('unit,sex,age,geo_time', axis=1, inplace=True)

    # Melt the DataFrame to create separate rows for each year
    df = pd.melt(df, id_vars=['unit', 'sex', 'age', 'geo_time'],
                 var_name='year', value_name='value')

    # mudar o nome da quarta coluna "geo_time"
    df.columns.values[3] = 'region'

    # Alterar o tipo de dados de 'year' para int
    df['year'] = df['year'].astype(int)

    # Aplicar a funcao clean à coluna value para limpar todas as letras
    df['value'] = df['value'].apply(clean)

    # Substituir : por Nan e em seguida eliminar NaN
    df['value'] = df['value'].replace('', pd.NA)
    df = df.dropna(subset=['value'])

    df['region'] = df['region'].str.extract(r'([A-Z]{2})', expand=False)
    #df['age'] = df['age'].apply(clean)

    df['value'] = df['value'].astype(float)
    df = df[df['region'] == country_arg]

    # Salvar o DataFrame resultante em um novo arquivo
    df.to_csv(script_dir / "data" / "pt_life_expectancy.csv", index=False)
    

# Funcao para limpar as letras da coluna value
def clean (value):
    cleaned_value = re.sub(r'[^0-9.]', '', value)
    return cleaned_value

if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser(prog='cleaning.py', description="Script to clean a dataset")
    parser.add_argument('country', type=str, nargs='*', help= 'Country to filter the dataframe')
    args = parser.parse_args()
    print(args)
    if len(sys.argv) > 1:
        clean_data(args.country[0])
    else:
        clean_data()
