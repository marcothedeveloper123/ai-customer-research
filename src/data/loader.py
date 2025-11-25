"""Data loading utilities."""

import pandas as pd
from pathlib import Path
from typing import Union
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DataLoader:
    """Load data from various file formats."""

    def load(self, file_path: Union[str, Path]) -> pd.DataFrame:
        """
        Load data from file.

        Args:
            file_path: Path to data file

        Returns:
            DataFrame with loaded data
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        logger.info(f"Loading data from {path.name}")

        if path.suffix == ".csv":
            return self.load_csv(path)
        elif path.suffix == ".json":
            return self.load_json(path)
        elif path.suffix == ".txt":
            return self.load_txt(path)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")

    def load_csv(self, path: Path) -> pd.DataFrame:
        """Load CSV file."""
        df = pd.read_csv(path)
        logger.info(f"Loaded {len(df)} rows from CSV")
        return df

    def load_json(self, path: Path) -> pd.DataFrame:
        """Load JSON file."""
        df = pd.read_json(path)
        logger.info(f"Loaded {len(df)} rows from JSON")
        return df

    def load_txt(self, path: Path) -> pd.DataFrame:
        """Load TXT file (one entry per line)."""
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        df = pd.DataFrame({"text": lines})
        logger.info(f"Loaded {len(df)} lines from TXT")
        return df
