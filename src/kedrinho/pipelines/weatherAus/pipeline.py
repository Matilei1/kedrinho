from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_weatherAUS

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_weatherAUS,
                inputs="weatherAus",
                outputs="preprocessed_weatherAUS",
                name="preprocess_weatherAUS_node",
            ),
        ]
    )
