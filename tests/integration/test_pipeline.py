"""Integration tests for full analysis pipeline."""

import pytest
import pandas as pd
from pathlib import Path
from unittest.mock import patch
from src.data.loader import DataLoader
from src.data.processor import TextProcessor
from src.models.analyzer import CustomerAnalyzer


class TestPipeline:
    """Integration tests for complete analysis pipeline."""

    @pytest.fixture
    def temp_csv_file(self, tmp_path):
        """Create temporary CSV file for testing."""
        csv_path = tmp_path / "test_data.csv"
        df = pd.DataFrame(
            {
                "text": [
                    "Excellent service!",
                    "Very disappointed with quality.",
                    "Average product, nothing special.",
                ]
            }
        )
        df.to_csv(csv_path, index=False)
        return csv_path

    def test_data_loading(self, temp_csv_file):
        """Test data loading from file."""
        loader = DataLoader()
        data = loader.load(temp_csv_file)

        assert isinstance(data, pd.DataFrame)
        assert len(data) == 3
        assert "text" in data.columns

    def test_text_preprocessing(self):
        """Test text preprocessing."""
        processor = TextProcessor()
        data = pd.DataFrame(
            {
                "text": [
                    "Text with <html>tags</html>",
                    "Text with http://url.com",
                    "Normal text",
                ]
            }
        )

        result = processor.process(data)
        assert len(result) == 3
        assert "<html>" not in result["text"].iloc[0]

    @patch("src.models.analyzer.OllamaClient")
    def test_end_to_end_pipeline(self, mock_client, temp_csv_file):
        """Test complete pipeline from loading to analysis."""
        # Mock Ollama responses
        mock_instance = mock_client.return_value
        mock_instance.batch_analyze.return_value = [
            {"response": "positive"},
            {"response": "negative"},
            {"response": "neutral"},
        ]

        # Load data
        loader = DataLoader()
        data = loader.load(temp_csv_file)

        # Preprocess
        processor = TextProcessor()
        processed = processor.process(data)

        # Analyze
        analyzer = CustomerAnalyzer(model="llama2")
        results = analyzer.analyze(processed, focus="sentiment")

        # Verify
        assert isinstance(results, pd.DataFrame)
        assert "sentiment" in results.columns
        assert len(results) == 3

    @patch("src.models.analyzer.OllamaClient")
    def test_pipeline_with_invalid_data(self, mock_client):
        """Test pipeline handling of invalid data."""
        processor = TextProcessor(
            config={"filtering": {"min_length": 10, "max_length": 100}}
        )

        data = pd.DataFrame({"text": ["short", "x" * 200, "valid text here"]})

        result = processor.process(data)
        assert len(result) == 1  # Only valid text remains
