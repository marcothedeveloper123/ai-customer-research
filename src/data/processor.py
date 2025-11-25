"""Text preprocessing utilities."""

import re
import pandas as pd
from typing import Dict, List
from src.utils.logger import get_logger

logger = get_logger(__name__)


class TextProcessor:
    """Preprocess text data for analysis."""

    def __init__(self, config: Dict = None):
        """
        Initialize text processor.

        Args:
            config: Preprocessing configuration
        """
        self.config = config or {}

    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Process all text in DataFrame.

        Args:
            data: Input DataFrame

        Returns:
            Processed DataFrame
        """
        if "text" not in data.columns:
            raise ValueError("DataFrame must have 'text' column")

        logger.info(f"Processing {len(data)} text entries")

        # Apply cleaning
        data["text"] = data["text"].apply(self.clean_text)

        # Filter by length
        min_length = self.config.get("filtering", {}).get("min_length", 10)
        max_length = self.config.get("filtering", {}).get("max_length", 10000)

        data = data[
            (data["text"].str.len() >= min_length)
            & (data["text"].str.len() <= max_length)
        ]

        # Remove duplicates
        if self.config.get("filtering", {}).get("remove_duplicates", True):
            data = data.drop_duplicates(subset=["text"])

        logger.info(f"After processing: {len(data)} entries")
        return data

    def clean_text(self, text: str) -> str:
        """
        Clean individual text entry.

        Args:
            text: Input text

        Returns:
            Cleaned text
        """
        if not isinstance(text, str):
            return ""

        # Remove HTML tags
        if self.config.get("cleaning", {}).get("remove_html", True):
            text = re.sub(r"<[^>]+>", "", text)

        # Remove URLs
        if self.config.get("cleaning", {}).get("remove_urls", True):
            text = re.sub(r"http\S+|www.\S+", "", text)

        # Remove emails
        if self.config.get("cleaning", {}).get("remove_emails", True):
            text = re.sub(r"\S+@\S+", "", text)

        # Remove extra whitespace
        if self.config.get("cleaning", {}).get("remove_extra_whitespace", True):
            text = re.sub(r"\s+", " ", text)

        return text.strip()
