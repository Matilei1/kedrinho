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

def preprocess_weatherAUS(weatherAUS: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the weatherAUS data without knowing the columns beforehand."""
    
    # Imprime las primeras filas del DataFrame para inspeccionar los datos
    print(weatherAUS.head())  # Muestra los primeros registros del DataFrame
    
    # Inspecciona las columnas de tu DataFrame
    print(f"Column names: {weatherAUS.columns.tolist()}")  # Muestra las columnas disponibles
    
    print(weatherAUS.describe())
    # Retorna el DataFrame tal cual
    print('existen ' + str(weatherAUS.shape[1]) + ' columnas')
    print('con un total de ' + str(weatherAUS.shape[0]) + ' filas')
    return weatherAUS

def seeNullValues(weatherAUS: pd.DataFrame) -> pd.DataFrame:   
    # Ver cuántos valores nulos hay en cada columna
    print(weatherAUS.isnull().sum())

def fillNullValues(weatherAUS: pd.DataFrame) -> pd.DataFrame:   
    # Rellenar valores nulos con la media (ejemplo para datos numéricos)
    #weatherAUS.fillna(weatherAUS.mean(), inplace=True)
    return weatherAUS.fillna(weatherAUS.mean())


def dropNullValues(weatherAUS: pd.DataFrame) -> pd.DataFrame:   
    #eliminar filas con valores nulos
   # weatherAUS.dropna(inplace=True)
   return weatherAUS.dropna()

def convertDateFormat(weatherAUS: pd.DataFrame) -> pd.DataFrame:
    #convertimos fechas por separado, para facilitar el analisis historico
    weatherAUS["Date"] = pd.to_datetime(weatherAUS["Date"])
    weatherAUS["Year"] = weatherAUS["Date"].dt.year
    weatherAUS["Month"] = weatherAUS["Date"].dt.month
    weatherAUS["Day"] = weatherAUS["Date"].dt.day #Solo el número
    return weatherAUS
#Filtro de localidades
#---------
def clean_weatherAus_data(weatherAUS: pd.DataFrame) -> pd.DataFrame:
    #Filtrar localidades que si se dedican a la agricultura
    localidades_permitidas = [
        'Adelaide', 'Albury', 'Ballarat', 'Bendigo', 'Brisbane', 'Cairns', 'Canberra',
        'Darwin', 'GoldCoast', 'Launceston', 'Mildura', 'Moree', 'MountGambier',
        'Newcastle', 'Perth', 'Sale', 'Sydney', 'WaggaWagga', 'Wollongong'
    ]
    weatherAUS = weatherAUS[weatherAUS['Location'].isin(localidades_permitidas)]

     # One-hot encoding para variables categóricas excepto Location. 
     # Quedan como columnas binarias
    categorical_cols = weatherAUS.select_dtypes(include=['object']).columns.drop('Location')
    df_encoded = pd.get_dummies(weatherAUS, columns=categorical_cols, dummy_na=True, drop_first=True)

    return df_encoded
