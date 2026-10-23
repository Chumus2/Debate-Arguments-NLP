import pandas as pd
from pathlib import Path



def load_data(file_path: str | Path) -> pd.DataFrame:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found at {file_path}")

    try:
        df = pd.read_csv(path)

        if df.empty:
            raise ValueError(f"File {path} is empty")

        print(f"Successfully loaded data from {path.name}")

    except pd.errors.EmptyDataError:
        print(f"File {path} is empty")
        raise
    except Exception as e:
        print(f"Failed to load data from {path.name}: {e}")
        raise

    return df