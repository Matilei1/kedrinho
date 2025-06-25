from kedro.pipeline import Pipeline, node, pipeline

from .nodes import clean_weatheraus_data,guardar_en_bd

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=clean_weatheraus_data,
                inputs="weatherAus", 
                outputs="weather_cleaned",#Dataset limpio
                name="clean_weatheraus_node",
            ),
            node(
                func=guardar_en_bd,
                inputs="weather_cleaned",
                outputs="weather_from_db",
                name="guardar_weather_en_bd"
)

        ]
    )
