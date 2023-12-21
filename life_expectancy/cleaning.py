# cleaning
import re
from enum import Enum
import pandas as pd


class Region(Enum):
    PT = 'PT'
    BE = 'BE'
    BG = 'BG'
    AT = 'AT'
    CH = 'CH'
    CY = 'CY'
    CZ = 'CZ'
    DK = 'DK'
    EE = 'EE'
    EL = 'EL'
    ES = 'ES'
    EU = 'EU'
    FI = 'FI'
    FR = 'FR'
    HR = 'HR'
    HU = 'HU'
    IS = 'IS'
    IT = 'IT'
    LI = 'LI'
    LT = 'LT'
    LU = 'LU'
    LV = 'LV'
    MT = 'MT'
    NL = 'NL'
    NO = 'NO'
    PL = 'PL'
    RO = 'RO'
    SE = 'SE'
    SI = 'SI'
    SK = 'SK'
    DE = 'DE'
    AL = 'AL'
    EA = 'EA'
    EF = 'EF'
    IE = 'IE'
    ME = 'ME'
    MK = 'MK'
    RS = 'RS'
    AM = 'AM'
    AZ = 'AZ'
    GE = 'GE'
    TR = 'TR'
    UA = 'UA'
    BY = 'BY'
    UK = 'UK'
    XK = 'XK'
    FX = 'FX'
    MD = 'MD'
    SM = 'SM'
    RU = 'RU'
    EA18 = 'EA18'
    EA19 = 'EA19'
    EFTA = 'EFTA'
    EEA30_2007 = 'EEA30_2007'
    EEA31 = 'EEA31'
    EU27_2007 = 'EU27_2007'
    EU28 = 'EU28'

    @classmethod
    def get_countries(cls):
        return [reg.value for reg in cls if len(reg.value) == 2]

def clean_data(original_df, country_arg=Region.PT) -> pd.DataFrame:

    original_df.columns.values[0] = 'unit,sex,age,geo_time'
    original_df[['unit', 'sex', 'age', 'geo_time']] = (
        original_df['unit,sex,age,geo_time'].str.split(',', expand=True)
    )
    original_df.drop('unit,sex,age,geo_time', axis=1, inplace=True)
    original_df = pd.melt(
    original_df,
        id_vars=['unit', 'sex', 'age', 'geo_time'], var_name='year', value_name='value')
    original_df.columns.values[3] = 'region'
    original_df['year'] = original_df['year'].astype('int64')
    original_df['value'] = original_df['value'].astype(str)
    original_df['value'] = original_df['value'].apply(clean)
    original_df['value'] = original_df['value'].replace('', pd.NA)
    original_df = original_df.dropna(subset=['value'])
    original_df['value'] = original_df['value'].astype(float)

    print(f"Cleaned DataFrame:\n{original_df.head()}\n")

    df_clean = original_df[original_df['region'] == country_arg.value]

    return df_clean

def clean(value):
    cleaned_value = re.sub(r'[^0-9.]', '', value)
    return cleaned_value

if __name__ == "__main__": # pragma: no cover
    region = Region

    lst = list(Region)
    print(region.get_countries())
    