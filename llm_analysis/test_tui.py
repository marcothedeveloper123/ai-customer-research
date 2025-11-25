#!/usr/bin/env python3
"""Test script for TUI acceptance testing."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 60)
print("TUI Acceptance Testing")
print("=" * 60)
print()

# Test 1: Imports
print("Test 1: Component Imports")
print("-" * 60)
try:
    from tui.app import InterviewAnalysisTUI
    from tui.widgets.navigator import NavigationTree
    from tui.widgets.content_viewer import ContentViewer
    from tui.screens.main_screen import MainScreen
    print("✅ All components import successfully")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)

# Test 2: Dependencies
print()
print("Test 2: Dependencies")
print("-" * 60)
try:
    import textual
    import rich
    import aiosqlite
    import watchdog
    print(f"✅ Textual: {textual.__version__}")
    print(f"✅ Rich: installed")
    print(f"✅ aiosqlite: installed")
    print(f"✅ watchdog: installed")
except ImportError as e:
    print(f"❌ Dependency missing: {e}")
    sys.exit(1)

# Test 3: File Structure
print()
print("Test 3: File Structure")
print("-" * 60)
required_files = [
    "tui/__init__.py",
    "tui/app.py",
    "tui/app.css",
    "tui/screens/main_screen.py",
    "tui/widgets/navigator.py",
    "tui/widgets/content_viewer.py",
    "tui.py",
    "requirements.txt",
]

all_files_exist = True
for file_path in required_files:
    if Path(file_path).exists():
        print(f"✅ {file_path}")
    else:
        print(f"❌ {file_path} - MISSING")
        all_files_exist = False

if not all_files_exist:
    print("\n⚠️  Some files are missing")
    sys.exit(1)

# Test 4: App instantiation
print()
print("Test 4: App Instantiation")
print("-" * 60)
try:
    app = InterviewAnalysisTUI()
    print("✅ App instantiates successfully")
    print(f"   Title: {app.TITLE}")
    print(f"   CSS: {app.CSS_PATH}")
except Exception as e:
    print(f"❌ App instantiation failed: {e}")
    sys.exit(1)

# Summary
print()
print("=" * 60)
print("✅ ALL TESTS PASSED")
print("=" * 60)
print()
print("Ready for manual acceptance testing!")
print()
print("Launch TUI with:")
print("  python3 tui.py")
print()
print("Acceptance Testing Checklist:")
print("  1. ✅ TUI launches without errors")
print("  2. ⏳ Three panes are visible (navigation, content, chat)")
print("  3. ⏳ Navigation tree shows report structure")
print("  4. ⏳ Arrow keys navigate tree items")
print("  5. ⏳ Enter key selects items and loads content")
print("  6. ⏳ Content pane displays markdown properly")
print("  7. ⏳ 'q' key quits the application")
print("  8. ⏳ Terminal resizing works properly")
print()
