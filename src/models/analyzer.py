"""Customer research analyzer using Ollama."""

from typing import Dict, List, Any
import pandas as pd
from src.models.ollama_client import OllamaClient
from src.utils.logger import get_logger

logger = get_logger(__name__)


class CustomerAnalyzer:
    """Analyzer for customer research data."""

    def __init__(self, model: str = "llama2", config: Dict = None):
        """
        Initialize customer analyzer.

        Args:
            model: Ollama model name
            config: Analysis configuration
        """
        self.model = model
        self.config = config or {}
        self.client = OllamaClient(model=model)

    def analyze(
        self,
        data: pd.DataFrame,
        focus: str = "all",
        batch_size: int = 10,
    ) -> pd.DataFrame:
        """
        Analyze customer data.

        Args:
            data: Input data as DataFrame
            focus: Analysis focus (sentiment, themes, insights, all)
            batch_size: Batch size for processing

        Returns:
            DataFrame with analysis results
        """
        logger.info(f"Starting {focus} analysis on {len(data)} records")

        results = data.copy()

        if focus in ["sentiment", "all"]:
            logger.info("Running sentiment analysis...")
            results = self._analyze_sentiment(results, batch_size)

        if focus in ["themes", "all"]:
            logger.info("Extracting themes...")
            results = self._extract_themes(results, batch_size)

        if focus in ["insights", "all"]:
            logger.info("Generating insights...")
            results = self._generate_insights(results, batch_size)

        logger.info("Analysis complete")
        return results

    def _analyze_sentiment(
        self, data: pd.DataFrame, batch_size: int
    ) -> pd.DataFrame:
        """Analyze sentiment for each text."""
        texts = data["text"].tolist()
        sentiments = self.client.batch_analyze(
            texts, task="sentiment", batch_size=batch_size
        )

        data["sentiment"] = [s.get("response", "unknown") for s in sentiments]
        return data

    def _extract_themes(
        self, data: pd.DataFrame, batch_size: int
    ) -> pd.DataFrame:
        """Extract themes from texts."""
        texts = data["text"].tolist()
        themes = self.client.batch_analyze(
            texts, task="themes", batch_size=batch_size
        )

        data["themes"] = [t.get("response", "") for t in themes]
        return data

    def _generate_insights(
        self, data: pd.DataFrame, batch_size: int
    ) -> pd.DataFrame:
        """Generate insights from texts."""
        # Aggregate analysis for insights
        summary_text = self._create_summary(data)

        insight_result = self.client.analyze_text(
            summary_text, task="insights"
        )

        data.attrs["insights"] = insight_result.get("response", "")
        return data

    def _create_summary(self, data: pd.DataFrame) -> str:
        """Create summary text for insight generation."""
        sample_size = min(100, len(data))
        sample = data.head(sample_size)

        summary = f"Analysis of {len(data)} customer feedback entries.\n\n"
        summary += "Sample feedback:\n"

        for idx, row in sample.iterrows():
            summary += f"- {row['text'][:200]}...\n"

        return summary
