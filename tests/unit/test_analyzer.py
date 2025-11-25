"""Unit tests for CustomerAnalyzer."""

import pytest
import pandas as pd
from unittest.mock import Mock, patch
from src.models.analyzer import CustomerAnalyzer


class TestCustomerAnalyzer:
    """Test cases for CustomerAnalyzer."""

    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing."""
        return pd.DataFrame(
            {
                "text": [
                    "Great product! Very satisfied.",
                    "Poor quality, disappointed.",
                    "Average experience, nothing special.",
                ]
            }
        )

    @patch("src.models.analyzer.OllamaClient")
    def test_analyzer_initialization(self, mock_client):
        """Test analyzer initialization."""
        analyzer = CustomerAnalyzer(model="llama2")
        assert analyzer.model == "llama2"
        mock_client.assert_called_once()

    @patch("src.models.analyzer.OllamaClient")
    def test_sentiment_analysis(self, mock_client, sample_data):
        """Test sentiment analysis."""
        mock_instance = Mock()
        mock_instance.batch_analyze.return_value = [
            {"response": "positive"},
            {"response": "negative"},
            {"response": "neutral"},
        ]
        mock_client.return_value = mock_instance

        analyzer = CustomerAnalyzer(model="llama2")
        result = analyzer.analyze(sample_data, focus="sentiment")

        assert "sentiment" in result.columns
        assert len(result) == 3
        mock_instance.batch_analyze.assert_called_once()

    @patch("src.models.analyzer.OllamaClient")
    def test_theme_extraction(self, mock_client, sample_data):
        """Test theme extraction."""
        mock_instance = Mock()
        mock_instance.batch_analyze.return_value = [
            {"response": "quality, satisfaction"},
            {"response": "quality issues"},
            {"response": "average experience"},
        ]
        mock_client.return_value = mock_instance

        analyzer = CustomerAnalyzer(model="llama2")
        result = analyzer.analyze(sample_data, focus="themes")

        assert "themes" in result.columns
        mock_instance.batch_analyze.assert_called_once()

    @patch("src.models.analyzer.OllamaClient")
    def test_full_analysis(self, mock_client, sample_data):
        """Test complete analysis workflow."""
        mock_instance = Mock()
        mock_instance.batch_analyze.return_value = [
            {"response": "positive"},
            {"response": "negative"},
            {"response": "neutral"},
        ]
        mock_instance.analyze_text.return_value = {
            "response": "Mixed feedback overall"
        }
        mock_client.return_value = mock_instance

        analyzer = CustomerAnalyzer(model="llama2")
        result = analyzer.analyze(sample_data, focus="all")

        assert "sentiment" in result.columns
        assert "themes" in result.columns
        assert len(result) == 3
