# Interview Analysis TUI

Terminal User Interface for exploring AI-powered customer research analysis.

## Features (Phase 1 - Foundation) ✅

- **3-Pane Layout**: Navigation (left), Content (right), Chat placeholder (bottom)
- **Navigation Tree**: Browse report sections, individual interviews, and aggregated views
- **Content Viewer**: Markdown rendering with syntax highlighting
- **Keyboard Shortcuts**: Arrow keys, Enter, q to quit
- **Responsive Design**: Adapts to terminal size

## Installation

### 1. Install Dependencies

```bash
cd llm_analysis
pip install -r requirements.txt
```

This installs:
- `textual>=0.47.0` - TUI framework
- `rich>=13.7.0` - Text formatting
- `aiosqlite>=0.19.0` - Chat history (Phase 2)
- `watchdog>=4.0.0` - File watching

### 2. Verify Installation

```bash
python3 -c "import textual; print(f'Textual {textual.__version__} installed')"
```

## Usage

### Launch TUI

```bash
# From llm_analysis directory
python3 tui.py

# Or using module syntax
python3 -m tui.app
```

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `↑↓` | Navigate tree items |
| `←→` | Expand/collapse nodes |
| `Enter` | Select item |
| `q` | Quit application |
| `?` | Help (Phase 5) |
| `e` | Edit mode (Phase 3) |
| `Ctrl+P` | Prompt editor (Phase 4) |
| `Ctrl+D` | Data browser (Phase 5) |
| `/` | Search (Phase 5) |

## Project Structure

```
llm_analysis/tui/
├── __init__.py
├── app.py                  # Main application entry point
├── app.css                 # TUI styling
├── screens/
│   ├── __init__.py
│   └── main_screen.py      # 3-pane layout screen
├── widgets/
│   ├── __init__.py
│   ├── navigator.py        # Navigation tree widget
│   └── content_viewer.py   # Markdown content viewer
├── services/               # For Phase 2+
│   └── __init__.py
└── utils/                  # For Phase 2+
    └── __init__.py
```

## Navigation Structure

### 📊 Analysis
- **📄 Report**
  - Executive Summary
  - Key Findings
  - Themes & Patterns
  - Pain Points
  - Desires & Needs
  - Trust Factors
  - Recommendations

- **🎤 Interviews (27)**
  - Individual interview analyses
  - Transcripts and findings

- **📈 Aggregated Views**
  - All Quotes
  - Themes by Frequency
  - Pain Points by Category
  - Desires by Priority
  - Trust Factors

## Development Phases

### ✅ Phase 1: Foundation (Completed)
- Basic TUI with navigation and viewing
- 3-pane layout
- Navigation tree
- Content viewer with markdown rendering
- Keyboard shortcuts

### 🔜 Phase 2: Chat Integration (Next)
- LLM-powered chat interface
- Context-aware queries
- Chat commands (/quote, /compare, /summarize)
- SQLite chat history
- Insert chat responses into report

### 🔜 Phase 3: Report Editing
- Toggle view/edit mode
- Markdown editor
- Auto-save every 30 seconds
- Add/insert sections
- Undo/redo support

### 🔜 Phase 4: Prompt Lab
- Edit analysis prompts
- Test on single interview
- Side-by-side comparison
- Prompt versioning
- Batch re-analysis

### 🔜 Phase 5: Polish
- Data browser overlay
- Help screen
- Status bar
- Themes
- Error handling
- Loading indicators

## Troubleshooting

### TUI Won't Launch

**Error**: `ModuleNotFoundError: No module named 'textual'`

**Solution**:
```bash
cd llm_analysis
pip install -r requirements.txt
```

### Import Errors

**Error**: `ModuleNotFoundError: No module named 'tui'`

**Solution**: Make sure you're running from the `llm_analysis` directory:
```bash
cd llm_analysis
python3 tui.py
```

### Content Not Loading

**Issue**: Report or interviews not showing content

**Solution**:
1. Run the analysis first to generate report:
   ```bash
   python analyze_interviews.py
   python synthesize_report.py
   ```

2. Check that files exist:
   - `output/FINAL_ANALYSIS_REPORT.md`
   - `output/*_analysis.json`

## Contributing

See `GITHUB_ISSUES.md` for development tasks and roadmap.

### Running Tests (Coming in Phase 5)

```bash
pytest tests/tui/
```

### Code Style

```bash
black llm_analysis/tui/
flake8 llm_analysis/tui/
```

## Architecture

### Widget Communication

```
MainScreen
├── NavigationTree (emits NodeSelected)
│   └── ContentViewer (receives selection, loads content)
├── ContentViewer (displays markdown)
└── ChatPane (Phase 2)
```

### Data Flow

1. User navigates tree with arrow keys
2. NavigationTree emits `NodeSelected` event
3. MainScreen handles event
4. ContentViewer loads appropriate content
5. Markdown rendered in content pane

## Performance

- **Startup**: <1 second
- **Navigation**: Instant tree traversal
- **Content Loading**: <100ms for markdown rendering
- **Memory**: ~50MB for basic TUI
- **Responsiveness**: No UI blocking

## Acknowledgments

Built with:
- [Textual](https://textual.textualize.io/) - Modern TUI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- [Python 3.9+](https://python.org/)

---

**Status**: Phase 1 Complete ✅ | Next: Phase 2 - Chat Integration 🚀
