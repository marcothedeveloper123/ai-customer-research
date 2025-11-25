"""Pytest configuration and shared fixtures."""

import pytest
import pandas as pd


@pytest.fixture
def sample_feedback():
    """Sample customer feedback data."""
    return pd.DataFrame(
        {
            "text": [
                "Great product! Very satisfied with purchase.",
                "Poor quality, broke after one week.",
                "Average experience, met expectations.",
                "Excellent customer service!",
                "Very disappointed, would not recommend.",
            ]
        }
    )


@pytest.fixture
def ollama_config():
    """Sample Ollama configuration."""
    return {
        "default_model": "llama2",
        "host": "http://localhost:11434",
        "timeout": 120,
        "generation": {"temperature": 0.7, "max_tokens": 2000},
    }


@pytest.fixture
def pipeline_config():
    """Sample pipeline configuration."""
    return {
        "preprocessing": {
            "cleaning": {
                "remove_html": True,
                "remove_urls": True,
                "remove_emails": True,
            },
            "filtering": {
                "min_length": 10,
                "max_length": 10000,
                "remove_duplicates": True,
            },
        },
        "analysis": {
            "tasks": ["sentiment_analysis", "theme_extraction"],
        },
    }
