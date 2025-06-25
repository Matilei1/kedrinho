import pandas as pd

def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"


def _parse_percentage(x: pd.Series) -> pd.Series:
    x = x.str.replace("%", "")
    x = x.astype(float) / 100
    return x


def _parse_money(x: pd.Series) -> pd.Series:
    x = x.str.replace("$", "").str.replace(",", "")
    x = x.astype(float)
    return x


import pandas as pd

import pandas as pd

def clean_weatheraus_data(df: pd.DataFrame) -> pd.DataFrame:

   # Nodo de preprocesamiento para el dataset weatherAUS.

    # 1. Conversión de fechas y descomposición
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    # 2. Eliminación de columnas con más del 40% de nulos
    cols_to_drop = ['Evaporation', 'Sunshine', 'Cloud9am', 'Cloud3pm']
    df = df.drop(columns=cols_to_drop, errors='ignore')

    # 3. Relleno de columnas numéricas con la media
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # 4. Rellenar solo estas categóricas con 'Desconocido'
    categorical_cols = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna('Desconocido')

    # 5. Filtrado de localidades agrícolas relevantes
    localidades_permitidas = [
        'Adelaide', 'Albury', 'Ballarat', 'Bendigo', 'Brisbane', 'Cairns', 'Canberra',
        'Darwin', 'GoldCoast', 'Launceston', 'Mildura', 'Moree', 'MountGambier',
        'Newcastle', 'Perth', 'Sale', 'Sydney', 'WaggaWagga', 'Wollongong'
    ]
    df = df[df['Location'].isin(localidades_permitidas)].copy()

    # 6. Codificación one-hot para categóricas (excepto 'Location')
    # Nota: drop_first=True evita multicolinealidad
    categorical_cols = df.select_dtypes(include='object').columns.drop('Location', errors='ignore')
    df = pd.get_dummies(df, columns=categorical_cols, dummy_na=True, drop_first=True)

    return df

def guardar_en_bd(df: pd.DataFrame) -> pd.DataFrame:
    # Simplemente retorna el DataFrame para que Kedro lo guarde vía DataCatalog
    return df
