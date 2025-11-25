#!/usr/bin/env python3
"""Entry point for the Interview Analysis TUI."""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from tui.app import main

if __name__ == "__main__":
    main()
