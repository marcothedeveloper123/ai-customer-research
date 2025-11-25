"""Configuration management utilities."""

import yaml
from pathlib import Path
from typing import Dict, Any
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_config(config_path: str = "config/pipeline.yaml") -> Dict[str, Any]:
    """
    Load configuration from YAML file.

    Args:
        config_path: Path to configuration file

    Returns:
        Configuration dictionary
    """
    path = Path(config_path)

    if not path.exists():
        logger.warning(f"Config file not found: {config_path}")
        return {}

    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        logger.info(f"Loaded configuration from {config_path}")
        return config
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        return {}


def load_model_config(
    config_path: str = "config/models/ollama.yaml",
) -> Dict[str, Any]:
    """
    Load model configuration.

    Args:
        config_path: Path to model config file

    Returns:
        Model configuration dictionary
    """
    return load_config(config_path)
