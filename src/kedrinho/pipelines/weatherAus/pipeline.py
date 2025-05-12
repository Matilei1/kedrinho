from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_weatherAUS, fillNullValues, dropNullValues, clean_weatherAus_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_weatherAUS,
                inputs="weatherAus", 
                outputs="preprocessed_weatherAUS",#Salida que se utiliza en el siguiente nodo
                name="preprocess_weatherAUS_node",
            ),
            node(
                func=clean_weatherAus_data,
                inputs="preprocessed_weatherAUS",  # Usando la salida del nodo anterior
                outputs="cleaned_weatherAUS",  # Resultado final después de la limpieza
                name="clean_weatherAus_data_node"
            ),
            node(
                func=fillNullValues,
                inputs="cleaned_weatherAUS",  # Usar salida del nodo anterior
                outputs="weatherAUS_filled",  # Resultado después de rellenar los valores nulos
                name="fill_null_values_node"
            ),
           
        ]
    )
