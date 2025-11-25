"""Main entry point for AI Customer Research application."""

import argparse
import sys
from pathlib import Path

from src.utils.logger import get_logger
from src.utils.config import load_config
from src.data.loader import DataLoader
from src.data.processor import TextProcessor
from src.models.analyzer import CustomerAnalyzer

logger = get_logger(__name__)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="AI Customer Research Analysis Tool"
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to input data file (CSV, JSON, or TXT)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/output/analysis_results.json",
        help="Path to output file",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="llama2",
        help="Ollama model to use for analysis",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "csv", "markdown"],
        default="json",
        help="Output format",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=10,
        help="Batch size for processing",
    )
    parser.add_argument(
        "--focus",
        type=str,
        choices=["sentiment", "themes", "insights", "all"],
        default="all",
        help="Analysis focus",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_args()

    # Set logging level
    if args.verbose:
        logger.level = "DEBUG"

    logger.info("Starting AI Customer Research Analysis")
    logger.info(f"Input: {args.input}")
    logger.info(f"Model: {args.model}")
    logger.info(f"Focus: {args.focus}")

    try:
        # Load configuration
        logger.info("Loading configuration...")
        config = load_config()

        # Load data
        logger.info("Loading data...")
        loader = DataLoader()
        data = loader.load(args.input)
        logger.info(f"Loaded {len(data)} records")

        # Preprocess
        logger.info("Preprocessing text...")
        processor = TextProcessor(config=config.get("preprocessing", {}))
        processed_data = processor.process(data)

        # Analyze
        logger.info("Running analysis...")
        analyzer = CustomerAnalyzer(
            model=args.model,
            config=config.get("analysis", {}),
        )
        results = analyzer.analyze(
            processed_data,
            focus=args.focus,
            batch_size=args.batch_size,
        )

        # Save results
        logger.info(f"Saving results to {args.output}...")
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if args.format == "json":
            results.to_json(args.output)
        elif args.format == "csv":
            results.to_csv(args.output)
        else:
            results.to_markdown(args.output)

        logger.info("Analysis complete!")
        logger.info(f"Results saved to: {args.output}")

        return 0

    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        if args.verbose:
            logger.exception(e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
