from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from kedrinho.pipelines.weatherAus.pipeline import create_pipeline  # Ajusta la importación

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # Registra el pipeline por nombre
    pipelines = {
        "__default__": create_pipeline(),  # O puedes elegir otro nombre si lo prefieres
        "weatherAus": create_pipeline()    # Si es un pipeline específico para weatherAus
    }
    return pipelines
