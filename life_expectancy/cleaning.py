# cleaning
import re
import pandas as pd

def clean_data(original_df, country_arg='PT') -> pd.DataFrame:

    original_df.columns.values[0] = 'unit,sex,age,geo_time'
    original_df[['unit', 'sex', 'age', 'geo_time']] = original_df['unit,sex,age,geo_time'].str.split(',', expand=True)
    original_df.drop('unit,sex,age,geo_time', axis=1, inplace=True)
    original_df = pd.melt(original_df, id_vars=['unit', 'sex', 'age', 'geo_time'], var_name='year', value_name='value')
    original_df.columns.values[3] = 'region'
    original_df['year'] = original_df['year'].astype('int64')
    original_df['value'] = original_df['value'].astype(str)
    original_df['value'] = original_df['value'].apply(clean)
    original_df['value'] = original_df['value'].replace('', pd.NA)
    original_df = original_df.dropna(subset=['value'])
    original_df['region'] = original_df['region'].str.extract(r'([A-Z]{2})', expand=False)
    original_df['value'] = original_df['value'].astype(float)
    df_clean = original_df[original_df['region'] == country_arg]
    
    return df_clean

def clean(value):
    cleaned_value = re.sub(r'[^0-9.]', '', value)
    return cleaned_value