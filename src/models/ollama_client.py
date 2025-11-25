"""Ollama API client for AI inference."""

import requests
from typing import Dict, List, Optional
from src.utils.logger import get_logger

logger = get_logger(__name__)


class OllamaClient:
    """Client for interacting with Ollama API."""

    def __init__(
        self,
        model: str = "llama2",
        host: str = "http://localhost:11434",
        timeout: int = 120,
    ):
        """
        Initialize Ollama client.

        Args:
            model: Name of the Ollama model to use
            host: Ollama API host URL
            timeout: Request timeout in seconds
        """
        self.model = model
        self.host = host
        self.timeout = timeout
        self._verify_connection()

    def _verify_connection(self) -> bool:
        """Verify connection to Ollama service."""
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            response.raise_for_status()
            logger.info("Successfully connected to Ollama")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Ollama: {e}")
            raise ConnectionError(
                f"Cannot connect to Ollama at {self.host}. "
                "Make sure Ollama is running."
            )

    def generate(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        **kwargs,
    ) -> str:
        """
        Generate text using Ollama model.

        Args:
            prompt: Input prompt for the model
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional generation parameters

        Returns:
            Generated text response
        """
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "stream": False,
                **kwargs,
            }

            response = requests.post(
                f"{self.host}/api/generate",
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()

            result = response.json()
            return result.get("response", "")

        except requests.exceptions.Timeout:
            logger.error(f"Request timeout after {self.timeout}s")
            raise
        except Exception as e:
            logger.error(f"Generation failed: {e}")
            raise

    def analyze_text(
        self,
        text: str,
        task: str = "sentiment",
        **kwargs,
    ) -> Dict:
        """
        Analyze text for specific task.

        Args:
            text: Text to analyze
            task: Analysis task (sentiment, themes, insights)
            **kwargs: Additional parameters

        Returns:
            Analysis results as dictionary
        """
        prompts = {
            "sentiment": (
                f"Analyze the sentiment of this customer feedback. "
                f"Respond with: positive, neutral, or negative.\n\n"
                f"Feedback: {text}\n\nSentiment:"
            ),
            "themes": (
                f"Extract key themes from this customer feedback. "
                f"List 3-5 main themes.\n\n"
                f"Feedback: {text}\n\nThemes:"
            ),
            "insights": (
                f"Generate actionable insights from this customer feedback.\n\n"
                f"Feedback: {text}\n\nInsights:"
            ),
        }

        prompt = prompts.get(task, prompts["insights"])
        response = self.generate(prompt, **kwargs)

        return {
            "task": task,
            "input": text,
            "response": response,
            "model": self.model,
        }

    def batch_analyze(
        self,
        texts: List[str],
        task: str = "sentiment",
        batch_size: int = 10,
        **kwargs,
    ) -> List[Dict]:
        """
        Analyze multiple texts in batches.

        Args:
            texts: List of texts to analyze
            task: Analysis task
            batch_size: Number of texts per batch
            **kwargs: Additional parameters

        Returns:
            List of analysis results
        """
        results = []
        total = len(texts)

        for i in range(0, total, batch_size):
            batch = texts[i : i + batch_size]
            logger.info(f"Processing batch {i // batch_size + 1}")

            for text in batch:
                try:
                    result = self.analyze_text(text, task=task, **kwargs)
                    results.append(result)
                except Exception as e:
                    logger.error(f"Failed to analyze text: {e}")
                    results.append({"error": str(e), "input": text})

        return results
