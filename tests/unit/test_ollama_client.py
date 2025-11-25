"""Unit tests for Ollama client."""

import pytest
from unittest.mock import Mock, patch
from src.models.ollama_client import OllamaClient


class TestOllamaClient:
    """Test cases for OllamaClient."""

    @patch("src.models.ollama_client.requests.get")
    def test_connection_successful(self, mock_get):
        """Test successful connection to Ollama."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"models": []}

        client = OllamaClient(model="llama2")
        assert client.model == "llama2"

    @patch("src.models.ollama_client.requests.get")
    def test_connection_failure(self, mock_get):
        """Test connection failure handling."""
        mock_get.side_effect = ConnectionError("Cannot connect")

        with pytest.raises(ConnectionError):
            OllamaClient(model="llama2")

    @patch("src.models.ollama_client.requests.post")
    @patch("src.models.ollama_client.requests.get")
    def test_generate_text(self, mock_get, mock_post):
        """Test text generation."""
        mock_get.return_value.status_code = 200
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "response": "This is a test response"
        }

        client = OllamaClient(model="llama2")
        result = client.generate("Test prompt")

        assert result == "This is a test response"
        mock_post.assert_called_once()

    @patch("src.models.ollama_client.requests.post")
    @patch("src.models.ollama_client.requests.get")
    def test_analyze_sentiment(self, mock_get, mock_post):
        """Test sentiment analysis."""
        mock_get.return_value.status_code = 200
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"response": "positive"}

        client = OllamaClient(model="llama2")
        result = client.analyze_text("Great product!", task="sentiment")

        assert result["task"] == "sentiment"
        assert result["input"] == "Great product!"
        assert "response" in result

    @patch("src.models.ollama_client.requests.post")
    @patch("src.models.ollama_client.requests.get")
    def test_batch_analyze(self, mock_get, mock_post):
        """Test batch analysis."""
        mock_get.return_value.status_code = 200
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"response": "positive"}

        client = OllamaClient(model="llama2")
        texts = ["Good", "Bad", "Neutral"]
        results = client.batch_analyze(texts, task="sentiment", batch_size=2)

        assert len(results) == 3
        assert mock_post.call_count == 3
