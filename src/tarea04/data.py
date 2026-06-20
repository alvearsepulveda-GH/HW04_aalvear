"""Utilidades iniciales para acceso a datos."""

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    """Carga un CSV aceptando rutas como texto o Path."""
    return pd.read_csv(Path(path), **kwargs)

