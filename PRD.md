# PRD: Interview Analysis TUI

## Overview

**Product**: Terminal User Interface for AI-powered interview analysis
**Current State**: Python scripts analyze 27 interviews → generate static markdown report
**Goal**: Interactive environment for exploring findings, conversing with results, and iteratively refining analysis

## User & Use Case

**Primary user**: Marco (UX researcher analyzing interview data)

**Core workflow**:
1. Run batch analysis (existing functionality)
2. Launch TUI to explore results
3. Chat with LLM about findings ("What are trust factors in interviews 5-10?")
4. Edit/extend report based on insights
5. Adjust prompts and re-analyze specific interviews
6. Export final report

## Success Criteria

- Chat queries return relevant answers in <3 seconds
- Can navigate entire analysis without leaving TUI
- Edit prompts and test on single interview in <30 seconds
- Report changes save automatically
- Zero context switching to external tools

## Features

### 1. Navigation Pane (Left)

**Purpose**: Browse analysis structure

**Contents**:
- Report sections (hierarchical tree)
- Individual interviews (27 files)
- Aggregated views (quotes by topic, patterns by frequency)

**Interactions**:
- Arrow keys navigate
- Enter selects/expands
- `/` search across all content
- `g` quick jump to section

### 2. Content Pane (Right)

**Purpose**: View and edit report

**Modes**:
- **View mode**: Rendered markdown with syntax highlighting
- **Edit mode**: Live markdown editor
- **Diff mode**: Compare prompt variations

**Actions**:
- `e` toggle edit mode
- `a` add new section (prompts for title, LLM suggests content)
- `i` insert finding from current context
- `s` save (auto-saves every 30s)

### 3. Chat Pane (Bottom)

**Purpose**: Query analysis results

**Context awareness**:
- Knows current selected section
- Has access to all 27 analysis JSONs
- Remembers conversation within session

**Commands**:
- Natural language queries
- `/quote [topic]` - find verbatim quotes
- `/compare [criteria]` - compare across participants
- `/summarize` - summarize current section
- `/insert` - add last response to report at cursor

**Example queries**:
```
> What trust factors appear in >50% of interviews?
> Find quotes about hallucinations
> Compare desires between technical vs non-technical users
> Summarize pain points for section 2.3
```

### 4. Prompt Manager (Overlay: Ctrl+P)

**Purpose**: Edit and test analysis prompts

**Components**:
- Prompt templates (analysis, synthesis, chat system prompt)
- Test runner (apply to single interview)
- Results preview (side-by-side JSON comparison)
- Version history (rollback capability)

**Workflow**:
1. Select prompt type
2. Edit in modal editor
3. Click "Test on Interview X"
4. Review output quality
5. Save or revert
6. Optionally re-run full analysis

### 5. Data Browser (Overlay: Ctrl+D)

**Purpose**: Inspect raw analysis data

**Views**:
- JSON viewer for individual interviews
- Field aggregation (all pain_points across interviews)
- Quote explorer with full context
- Statistics (field counts, coverage %)

## Technical Architecture

### Stack

```
textual          ^0.47.0    # TUI framework
rich             ^13.7.0    # Text formatting
ollama           ^0.3.0     # LLM interface (existing)
python-docx      ^1.1.0     # Document reading (existing)
aiosqlite        ^0.19.0    # Chat history cache
watchdog         ^4.0.0     # File watching for auto-reload
```

### Project Structure

```
llm_analysis/
├── tui/
│   ├── __init__.py
│   ├── app.py                  # Main Textual application
│   ├── screens/
│   │   ├── main_screen.py      # 3-pane layout
│   │   ├── prompt_editor.py    # Ctrl+P overlay
│   │   └── data_browser.py     # Ctrl+D overlay
│   ├── widgets/
│   │   ├── navigator.py        # Left pane tree
│   │   ├── content_viewer.py   # Right pane viewer/editor
│   │   ├── chat_input.py       # Bottom chat interface
│   │   └── markdown_editor.py  # Markdown editing widget
│   ├── services/
│   │   ├── llm_service.py      # Ollama interaction + context mgmt
│   │   ├── analysis_loader.py  # Load/parse JSON analyses
│   │   ├── report_manager.py   # Read/write report file
│   │   └── prompt_tester.py    # Single-interview test runner
│   └── utils/
│       ├── chat_history.py     # SQLite conversation storage
│       └── config_manager.py   # Load/save TUI preferences
├── analyze_interviews.py       # Existing
├── synthesize_report.py        # Existing
└── config.py                   # Existing + TUI config section
```

### LLM Context Management

**Chat mode strategy**:

```python
class ChatContext:
	def __init__(self):
		self.mode = "global"  # or "section"
		self.current_section = None
		self.analyses = []    # All 27 JSONs

	def build_context(self) -> str:
		if self.mode == "global":
			return self._aggregate_all()
		else:
			return self._filter_by_section()
```

**Context types**:
- **Global**: All 27 analyses (slower, comprehensive)
- **Section**: Filtered subset (fast, focused)
- **Interview**: Single participant deep dive

### Prompt Testing Flow

```python
# prompt_tester.py
async def test_prompt(prompt: str, interview_path: str):
	# 1. Load interview
	transcript = read_transcript(interview_path)

	# 2. Apply new prompt
	result = await ollama.chat(prompt.format(transcript=transcript))

	# 3. Parse and validate JSON
	analysis = parse_analysis(result)

	# 4. Return comparison with existing
	return {
		'new': analysis,
		'existing': load_existing_analysis(interview_path),
		'diff': compute_diff(analysis, existing)
	}
```

## Implementation Phases

### Phase 1: Foundation (4-6 hours)
**Goal**: Basic TUI with navigation and viewing

- [ ] Set up Textual app boilerplate
- [ ] Load existing report and analyses
- [ ] 3-pane layout (nav, content, chat placeholder)
- [ ] Navigation tree with section browsing
- [ ] Content viewer (markdown rendering)
- [ ] Keyboard shortcuts (↑↓←→, Enter, q to quit)

**Validation**: Can launch TUI and browse entire report

### Phase 2: Chat Integration (6-8 hours)
**Goal**: Interactive querying of analysis data

- [ ] Chat input widget with history
- [ ] LLM service with context management
- [ ] Global mode: query all analyses
- [ ] Section mode: context-aware queries
- [ ] Commands: /quote, /compare, /summarize
- [ ] SQLite chat history persistence
- [ ] Insert chat response into report

**Validation**: Can ask questions and get relevant answers with sources

### Phase 3: Report Editing (4-6 hours)
**Goal**: Modify report without leaving TUI

- [ ] Toggle view/edit mode
- [ ] Markdown editor widget
- [ ] Add section command
- [ ] Insert finding command (pulls from context)
- [ ] Auto-save every 30s
- [ ] Manual save with Ctrl+S
- [ ] Undo/redo support

**Validation**: Can add section, edit content, save, verify changes persist

### Phase 4: Prompt Lab (6-8 hours)
**Goal**: Iterate on analysis prompts

- [ ] Prompt editor overlay (Ctrl+P)
- [ ] Load current prompts from config.py
- [ ] Edit prompt templates
- [ ] Test on single interview
- [ ] Side-by-side result comparison
- [ ] Save prompt versions
- [ ] Re-run analysis on all interviews
- [ ] Progress indicator for batch re-analysis

**Validation**: Edit prompt, test on 1 interview, see output, apply to all

### Phase 5: Polish (3-4 hours)
**Goal**: Production-ready UX

- [ ] Data browser overlay (Ctrl+D)
- [ ] Help screen (? key)
- [ ] Status bar with context info
- [ ] Theme/color customization
- [ ] Error handling and user feedback
- [ ] Loading indicators for LLM calls
- [ ] Command palette (Ctrl+K)

**Validation**: All features work smoothly, good error messages

## Entry Point

```bash
# Launch TUI
cd "/Users/marco/Documents/ai for customer research/llm_analysis"
python3 -m tui.app

# Or add to setup
python3 tui.py  # symlink to tui/app.py
```

## Configuration Additions

```python
# config.py additions
TUI_CONFIG = {
	"default_chat_mode": "section",  # or "global"
	"autosave_interval": 30,          # seconds
	"theme": "monokai",
	"chat_history_db": "output/chat_history.db",
	"prompt_versions_dir": "prompts/",
}

# Chat system prompt
CHAT_SYSTEM_PROMPT = """You are an AI research assistant helping analyze interview data.

You have access to:
- 27 interview analyses (JSON format)
- Current report content
- User's selected section/context

When answering:
- Cite specific interviews (e.g., "Interview 5 mentioned...")
- Use verbatim quotes when relevant
- Indicate confidence level if uncertain
- Suggest follow-up queries
"""
```

## Non-Goals (Out of Scope)

- Web interface (TUI only)
- Multi-user collaboration
- Real-time analysis (batch only)
- Integration with Coloop/Marvin
- Export to formats other than Markdown
- Voice/audio transcript support

## Open Questions

1. **Prompt versioning**: Git-based or custom system?
2. **Report format**: Lock to Markdown or support DOCX export?
3. **Chat history**: Per-session or persistent across launches?
4. **Batch re-analysis**: Background process or block TUI?
5. **Context window limits**: How to handle when all 27 analyses exceed LLM context?

## Success Metrics

- Complete analysis exploration without leaving TUI
- Chat queries answered in <3 seconds (95th percentile)
- Prompt iteration cycle <1 minute (edit → test → evaluate)
- Zero data loss (auto-save works reliably)
- User completes analysis in <50% of time vs manual approach
