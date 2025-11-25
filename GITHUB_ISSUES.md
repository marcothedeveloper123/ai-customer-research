# TUI Implementation - GitHub Issues

Generated from PRD: Interview Analysis TUI

## Issue Organization

**Labels**:
- `epic` - Large feature containing multiple stories
- `phase-1` through `phase-5` - Implementation phases
- `enhancement` - New feature
- `bug` - Defect
- `documentation` - Documentation updates
- `priority-high` - Critical path items
- `priority-medium` - Important but not blocking
- `priority-low` - Nice to have
- `frontend` - UI/UX work
- `backend` - Service/logic work
- `testing` - Test-related work

**Milestones**:
- `Phase 1: Foundation` (4-6 hours)
- `Phase 2: Chat Integration` (6-8 hours)
- `Phase 3: Report Editing` (4-6 hours)
- `Phase 4: Prompt Lab` (6-8 hours)
- `Phase 5: Polish` (3-4 hours)

---

## Epic Issues

### Epic #1: Phase 1 - Foundation
**Labels**: `epic`, `phase-1`, `priority-high`
**Milestone**: Phase 1: Foundation
**Estimate**: 4-6 hours

**Description**:
Set up basic TUI infrastructure with navigation and viewing capabilities. Users should be able to launch the TUI and browse the entire report.

**Success Criteria**:
- ✅ Can launch TUI from command line
- ✅ Can navigate report sections using arrow keys
- ✅ Can view markdown content with proper rendering
- ✅ Keyboard shortcuts work (↑↓←→, Enter, q)

**Related Issues**: #2, #3, #4, #5, #6, #7

---

### Epic #2: Phase 2 - Chat Integration
**Labels**: `epic`, `phase-2`, `priority-high`
**Milestone**: Phase 2: Chat Integration
**Estimate**: 6-8 hours

**Description**:
Enable interactive querying of analysis data through LLM-powered chat interface with context awareness.

**Success Criteria**:
- ✅ Can ask natural language questions about analysis
- ✅ Responses include interview citations
- ✅ Chat commands (/quote, /compare, /summarize) work
- ✅ Chat history persists to SQLite
- ✅ Can insert chat responses into report

**Related Issues**: #8, #9, #10, #11, #12, #13, #14

---

### Epic #3: Phase 3 - Report Editing
**Labels**: `epic`, `phase-3`, `priority-high`
**Milestone**: Phase 3: Report Editing
**Estimate**: 4-6 hours

**Description**:
Add report editing capabilities directly within TUI without context switching.

**Success Criteria**:
- ✅ Can toggle between view and edit modes
- ✅ Can add new sections to report
- ✅ Auto-save works every 30 seconds
- ✅ Manual save works with Ctrl+S
- ✅ Changes persist after TUI restart

**Related Issues**: #15, #16, #17, #18, #19, #20, #21

---

### Epic #4: Phase 4 - Prompt Lab
**Labels**: `epic`, `phase-4`, `priority-medium`
**Milestone**: Phase 4: Prompt Lab
**Estimate**: 6-8 hours

**Description**:
Enable prompt engineering workflow with testing and iteration capabilities.

**Success Criteria**:
- ✅ Can edit analysis prompts in overlay
- ✅ Can test prompt on single interview
- ✅ Side-by-side comparison shows differences
- ✅ Can save prompt versions
- ✅ Can re-run analysis on all interviews

**Related Issues**: #22, #23, #24, #25, #26, #27, #28

---

### Epic #5: Phase 5 - Polish
**Labels**: `epic`, `phase-5`, `priority-low`
**Milestone**: Phase 5: Polish
**Estimate**: 3-4 hours

**Description**:
Production-ready UX with data browser, help system, and error handling.

**Success Criteria**:
- ✅ Data browser overlay works (Ctrl+D)
- ✅ Help screen accessible with ?
- ✅ Status bar shows context info
- ✅ Error messages are clear and helpful
- ✅ Loading indicators show for LLM calls

**Related Issues**: #29, #30, #31, #32, #33, #34, #35

---

## Phase 1: Foundation Issues

### Issue #2: Set up Textual app boilerplate
**Labels**: `phase-1`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 1: Foundation
**Estimate**: 1 hour

**Description**:
Create basic Textual application structure with entry point and configuration.

**Tasks**:
- [ ] Create `llm_analysis/tui/` directory structure
- [ ] Create `tui/__init__.py`
- [ ] Create `tui/app.py` with basic Textual App class
- [ ] Add `textual ^0.47.0` to requirements.txt
- [ ] Add `rich ^13.7.0` to requirements.txt
- [ ] Create entry point script `tui.py`
- [ ] Test app launches without errors

**Acceptance Criteria**:
- App launches with `python3 -m tui.app`
- Basic window appears with title
- Pressing 'q' quits the application

**Files to Create**:
- `llm_analysis/tui/__init__.py`
- `llm_analysis/tui/app.py`
- `llm_analysis/tui.py` (symlink)

---

### Issue #3: Load existing report and analyses
**Labels**: `phase-1`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 1: Foundation
**Estimate**: 1.5 hours

**Description**:
Create service to load and parse existing analysis JSONs and report markdown.

**Tasks**:
- [ ] Create `tui/services/` directory
- [ ] Create `analysis_loader.py` service
- [ ] Implement `load_all_analyses()` to read 27 JSON files
- [ ] Implement `parse_analysis_json()` for validation
- [ ] Create `report_manager.py` service
- [ ] Implement `load_report()` to read markdown
- [ ] Implement `parse_report_structure()` for sections
- [ ] Add error handling for missing files

**Acceptance Criteria**:
- Successfully loads all 27 analysis JSON files
- Parses report markdown into hierarchical structure
- Returns meaningful error if files missing
- No performance issues (<500ms load time)

**Files to Create**:
- `llm_analysis/tui/services/__init__.py`
- `llm_analysis/tui/services/analysis_loader.py`
- `llm_analysis/tui/services/report_manager.py`

---

### Issue #4: Create 3-pane layout (nav, content, chat)
**Labels**: `phase-1`, `enhancement`, `priority-high`, `frontend`
**Milestone**: Phase 1: Foundation
**Estimate**: 1.5 hours

**Description**:
Implement responsive 3-pane layout with navigation tree (left), content viewer (right), and chat placeholder (bottom).

**Tasks**:
- [ ] Create `tui/screens/main_screen.py`
- [ ] Implement `MainScreen` with 3-pane container layout
- [ ] Set up left pane (30% width) for navigation
- [ ] Set up right pane (70% width) for content
- [ ] Set up bottom pane (20% height) for chat placeholder
- [ ] Add pane borders and labels
- [ ] Ensure responsive resizing

**Acceptance Criteria**:
- Three panes visible on launch
- Panes resize proportionally with terminal
- Borders and labels clearly distinguish panes
- No visual glitches or overlapping

**Files to Create**:
- `llm_analysis/tui/screens/__init__.py`
- `llm_analysis/tui/screens/main_screen.py`

---

### Issue #5: Build navigation tree widget
**Labels**: `phase-1`, `enhancement`, `priority-high`, `frontend`
**Milestone**: Phase 1: Foundation
**Estimate**: 2 hours

**Description**:
Create hierarchical tree widget for browsing report sections and individual interviews.

**Tasks**:
- [ ] Create `tui/widgets/` directory
- [ ] Create `navigator.py` widget
- [ ] Implement `NavigationTree` widget extending Textual Tree
- [ ] Load report structure into tree (sections, subsections)
- [ ] Add individual interviews node (27 items)
- [ ] Add aggregated views node (quotes, patterns)
- [ ] Implement arrow key navigation
- [ ] Implement Enter to select/expand
- [ ] Emit selection events to main screen

**Acceptance Criteria**:
- Tree shows full report hierarchy
- Can expand/collapse nodes with Enter
- Arrow keys navigate smoothly
- Current selection is highlighted
- Selection event triggers content update

**Files to Create**:
- `llm_analysis/tui/widgets/__init__.py`
- `llm_analysis/tui/widgets/navigator.py`

---

### Issue #6: Build content viewer widget
**Labels**: `phase-1`, `enhancement`, `priority-high`, `frontend`
**Milestone**: Phase 1: Foundation
**Estimate**: 2 hours

**Description**:
Create markdown content viewer with syntax highlighting and rendering.

**Tasks**:
- [ ] Create `content_viewer.py` widget
- [ ] Implement `ContentViewer` using Rich Markdown
- [ ] Add markdown syntax highlighting
- [ ] Implement scroll support
- [ ] Add code block rendering
- [ ] Handle images/links gracefully (text-only display)
- [ ] Sync with navigation selection
- [ ] Add status indicator (view mode)

**Acceptance Criteria**:
- Markdown renders properly with formatting
- Scrolling works smoothly
- Code blocks have syntax highlighting
- Updates when navigation selection changes
- Performance good for large content (>10k lines)

**Files to Create**:
- `llm_analysis/tui/widgets/content_viewer.py`

---

### Issue #7: Implement keyboard shortcuts
**Labels**: `phase-1`, `enhancement`, `priority-high`, `frontend`
**Milestone**: Phase 1: Foundation
**Estimate**: 1 hour

**Description**:
Add core keyboard shortcuts for navigation and basic operations.

**Tasks**:
- [ ] Implement ↑↓ for tree navigation
- [ ] Implement ←→ for expand/collapse
- [ ] Implement Enter for selection
- [ ] Implement 'q' for quit with confirmation
- [ ] Implement '/' for search (placeholder)
- [ ] Implement 'g' for quick jump (placeholder)
- [ ] Add keybinding help in status bar
- [ ] Handle conflicts gracefully

**Acceptance Criteria**:
- All arrow keys work as expected
- Enter selects items correctly
- 'q' shows quit confirmation
- No accidental quits
- Keybindings displayed somewhere visible

**Files to Modify**:
- `llm_analysis/tui/screens/main_screen.py`
- `llm_analysis/tui/app.py`

---

## Phase 2: Chat Integration Issues

### Issue #8: Create chat input widget
**Labels**: `phase-2`, `enhancement`, `priority-high`, `frontend`
**Milestone**: Phase 2: Chat Integration
**Estimate**: 1.5 hours

**Description**:
Build chat interface widget with input field and message history display.

**Tasks**:
- [ ] Create `chat_input.py` widget
- [ ] Implement input field with history scrollback
- [ ] Add message list container (user + assistant messages)
- [ ] Implement Enter to submit query
- [ ] Add ↑↓ for command history
- [ ] Add typing indicator for LLM processing
- [ ] Style user vs assistant messages differently
- [ ] Handle multi-line input (Shift+Enter)

**Acceptance Criteria**:
- Can type and submit queries
- Message history displays correctly
- User can scroll through previous messages
- Typing indicator shows during processing
- Messages are clearly distinguished (user vs AI)

**Files to Create**:
- `llm_analysis/tui/widgets/chat_input.py`

---

### Issue #9: Implement LLM service with context management
**Labels**: `phase-2`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 2: Chat Integration
**Estimate**: 2 hours

**Description**:
Create LLM service layer with Ollama integration and intelligent context management.

**Tasks**:
- [ ] Create `llm_service.py` in services
- [ ] Implement `LLMService` class with Ollama client
- [ ] Create `ChatContext` class for context management
- [ ] Implement global mode (all 27 analyses)
- [ ] Implement section mode (filtered context)
- [ ] Implement interview mode (single participant)
- [ ] Add context aggregation methods
- [ ] Add token counting and truncation
- [ ] Add error handling for Ollama failures

**Acceptance Criteria**:
- Can query LLM with different context modes
- Context switches based on navigation selection
- Handles context window limits gracefully
- Provides meaningful errors when Ollama unavailable
- Response time <3 seconds for typical queries

**Files to Create**:
- `llm_analysis/tui/services/llm_service.py`

---

### Issue #10: Implement global query mode
**Labels**: `phase-2`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 2: Chat Integration
**Estimate**: 1 hour

**Description**:
Enable querying across all 27 interview analyses simultaneously.

**Tasks**:
- [ ] Implement `build_global_context()` method
- [ ] Aggregate all analysis JSONs
- [ ] Create summarized context for token efficiency
- [ ] Add interview citations in responses
- [ ] Test with example queries from PRD
- [ ] Optimize for <3s response time

**Acceptance Criteria**:
- Queries search all 27 interviews
- Responses cite specific interviews
- Context fits within LLM limits
- Response time meets <3s target

**Files to Modify**:
- `llm_analysis/tui/services/llm_service.py`

---

### Issue #11: Implement section-aware query mode
**Labels**: `phase-2`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 2: Chat Integration
**Estimate**: 1 hour

**Description**:
Enable context-aware queries filtered to current report section.

**Tasks**:
- [ ] Implement `build_section_context()` method
- [ ] Filter analyses by current section topic
- [ ] Extract relevant quotes and findings
- [ ] Maintain section focus in conversation
- [ ] Update context when navigation changes

**Acceptance Criteria**:
- Queries focus on current section content
- Context updates when section changes
- Faster than global mode (<2s)
- Responses relevant to section topic

**Files to Modify**:
- `llm_analysis/tui/services/llm_service.py`

---

### Issue #12: Implement chat commands (/quote, /compare, /summarize)
**Labels**: `phase-2`, `enhancement`, `priority-medium`, `backend`
**Milestone**: Phase 2: Chat Integration
**Estimate**: 2 hours

**Description**:
Add specialized chat commands for common analysis operations.

**Tasks**:
- [ ] Implement `/quote [topic]` - find verbatim quotes
- [ ] Implement `/compare [criteria]` - cross-participant comparison
- [ ] Implement `/summarize` - summarize current section
- [ ] Implement `/insert` - add response to report
- [ ] Add command autocomplete suggestions
- [ ] Add command help messages
- [ ] Handle invalid command syntax

**Acceptance Criteria**:
- All four commands work correctly
- Commands provide focused, relevant results
- Error messages guide correct usage
- Commands faster than natural language queries

**Files to Modify**:
- `llm_analysis/tui/services/llm_service.py`
- `llm_analysis/tui/widgets/chat_input.py`

---

### Issue #13: Add SQLite chat history persistence
**Labels**: `phase-2`, `enhancement`, `priority-medium`, `backend`
**Milestone**: Phase 2: Chat Integration
**Estimate**: 1.5 hours

**Description**:
Store chat conversations in SQLite for cross-session persistence.

**Tasks**:
- [ ] Add `aiosqlite ^0.19.0` to requirements
- [ ] Create `utils/chat_history.py`
- [ ] Design chat history schema (sessions, messages)
- [ ] Implement `save_message()` method
- [ ] Implement `load_session()` method
- [ ] Implement `search_history()` method
- [ ] Add session management (new/resume)
- [ ] Handle database migrations

**Acceptance Criteria**:
- Chat history persists across TUI sessions
- Can resume previous conversations
- Can search historical queries
- Database operations don't block UI

**Files to Create**:
- `llm_analysis/tui/utils/__init__.py`
- `llm_analysis/tui/utils/chat_history.py`

---

### Issue #14: Implement insert chat response to report
**Labels**: `phase-2`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 2: Chat Integration
**Estimate**: 1 hour

**Description**:
Allow inserting chat responses directly into report at cursor position.

**Tasks**:
- [ ] Add `/insert` command to chat
- [ ] Format chat response as markdown
- [ ] Insert at current cursor position in content pane
- [ ] Show preview before inserting
- [ ] Add confirmation dialog
- [ ] Update report file
- [ ] Show success notification

**Acceptance Criteria**:
- Can insert last chat response with /insert
- Formatted properly as markdown
- Inserts at correct cursor location
- Report file updates immediately
- Undo option available

**Files to Modify**:
- `llm_analysis/tui/widgets/chat_input.py`
- `llm_analysis/tui/widgets/content_viewer.py`
- `llm_analysis/tui/services/report_manager.py`

---

## Phase 3: Report Editing Issues

### Issue #15: Implement view/edit mode toggle
**Labels**: `phase-3`, `enhancement`, `priority-high`, `frontend`
**Milestone**: Phase 3: Report Editing
**Estimate**: 1 hour

**Description**:
Add ability to toggle between view mode (rendered markdown) and edit mode (raw editor).

**Tasks**:
- [ ] Add 'e' keybinding to toggle modes
- [ ] Create mode indicator in status bar
- [ ] Preserve scroll position when toggling
- [ ] Add confirmation if unsaved changes
- [ ] Handle mode conflicts with other features

**Acceptance Criteria**:
- 'e' toggles between view and edit modes
- Mode clearly indicated in UI
- Scroll position preserved
- Unsaved changes prompt confirmation

**Files to Modify**:
- `llm_analysis/tui/widgets/content_viewer.py`
- `llm_analysis/tui/screens/main_screen.py`

---

### Issue #16: Create markdown editor widget
**Labels**: `phase-3`, `enhancement`, `priority-high`, `frontend`
**Milestone**: Phase 3: Report Editing
**Estimate**: 2 hours

**Description**:
Build full-featured markdown editor with syntax support and editing capabilities.

**Tasks**:
- [ ] Create `markdown_editor.py` widget
- [ ] Implement `MarkdownEditor` extending Textual TextArea
- [ ] Add markdown syntax highlighting
- [ ] Implement standard text editing (cut, copy, paste)
- [ ] Add line numbers
- [ ] Add cursor position indicator
- [ ] Support undo/redo (Ctrl+Z, Ctrl+Shift+Z)
- [ ] Handle large files efficiently

**Acceptance Criteria**:
- Full text editing capabilities
- Syntax highlighting works
- Undo/redo functions correctly
- Good performance with large documents
- Cursor position clearly visible

**Files to Create**:
- `llm_analysis/tui/widgets/markdown_editor.py`

---

### Issue #17: Implement add section command
**Labels**: `phase-3`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 3: Report Editing
**Estimate**: 1.5 hours

**Description**:
Add 'a' command to create new report sections with LLM-suggested content.

**Tasks**:
- [ ] Add 'a' keybinding for add section
- [ ] Create section title input dialog
- [ ] Query LLM for suggested content
- [ ] Show content preview
- [ ] Insert section at appropriate location
- [ ] Update navigation tree
- [ ] Save to report file

**Acceptance Criteria**:
- 'a' prompts for section title
- LLM suggests relevant content
- User can preview before inserting
- Navigation tree updates immediately
- Section saves to file

**Files to Modify**:
- `llm_analysis/tui/screens/main_screen.py`
- `llm_analysis/tui/services/llm_service.py`
- `llm_analysis/tui/services/report_manager.py`

---

### Issue #18: Implement insert finding command
**Labels**: `phase-3`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 3: Report Editing
**Estimate**: 1 hour

**Description**:
Add 'i' command to insert findings from current context into report.

**Tasks**:
- [ ] Add 'i' keybinding
- [ ] Pull findings from current navigation context
- [ ] Show finding selection dialog
- [ ] Format finding as markdown
- [ ] Insert at cursor position
- [ ] Update report file

**Acceptance Criteria**:
- 'i' shows relevant findings
- User can select from list
- Properly formatted when inserted
- Report updates immediately

**Files to Modify**:
- `llm_analysis/tui/screens/main_screen.py`
- `llm_analysis/tui/services/report_manager.py`

---

### Issue #19: Add auto-save every 30 seconds
**Labels**: `phase-3`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 3: Report Editing
**Estimate**: 1 hour

**Description**:
Implement automatic report saving every 30 seconds to prevent data loss.

**Tasks**:
- [ ] Create background auto-save task
- [ ] Check for unsaved changes
- [ ] Save if changes detected
- [ ] Add "saving..." indicator
- [ ] Add "saved" confirmation
- [ ] Handle save errors gracefully
- [ ] Add configuration option for interval

**Acceptance Criteria**:
- Auto-saves every 30 seconds
- Only saves if changes detected
- Visual feedback during save
- No UI blocking during save
- Configurable interval

**Files to Modify**:
- `llm_analysis/tui/services/report_manager.py`
- `llm_analysis/tui/screens/main_screen.py`
- `llm_analysis/config.py`

---

### Issue #20: Implement manual save (Ctrl+S)
**Labels**: `phase-3`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 3: Report Editing
**Estimate**: 30 minutes

**Description**:
Add Ctrl+S keybinding for manual save with visual confirmation.

**Tasks**:
- [ ] Add Ctrl+S keybinding
- [ ] Trigger report save
- [ ] Show save confirmation notification
- [ ] Reset "unsaved changes" flag
- [ ] Handle save errors

**Acceptance Criteria**:
- Ctrl+S saves report immediately
- Visual confirmation shown
- Works in both view and edit modes
- Error messages clear and helpful

**Files to Modify**:
- `llm_analysis/tui/screens/main_screen.py`
- `llm_analysis/tui/services/report_manager.py`

---

### Issue #21: Add undo/redo support
**Labels**: `phase-3`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 3: Report Editing
**Estimate**: 1 hour

**Description**:
Implement undo/redo functionality for text editing operations.

**Tasks**:
- [ ] Add Ctrl+Z for undo
- [ ] Add Ctrl+Shift+Z for redo
- [ ] Maintain edit history stack
- [ ] Limit history size (configurable)
- [ ] Clear history after save
- [ ] Add undo/redo to status bar

**Acceptance Criteria**:
- Ctrl+Z undoes last edit
- Ctrl+Shift+Z redoes undone edit
- History limited to prevent memory issues
- Works seamlessly with auto-save

**Files to Modify**:
- `llm_analysis/tui/widgets/markdown_editor.py`

---

## Phase 4: Prompt Lab Issues

### Issue #22: Create prompt editor overlay
**Labels**: `phase-4`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 4: Prompt Lab
**Estimate**: 1.5 hours

**Description**:
Build Ctrl+P overlay for editing analysis prompts.

**Tasks**:
- [ ] Create `prompt_editor.py` screen
- [ ] Add Ctrl+P keybinding to show overlay
- [ ] Create modal layout with editor
- [ ] Add prompt type selector (analysis, synthesis, chat)
- [ ] Add close/cancel actions
- [ ] Add save action
- [ ] Style as modal overlay

**Acceptance Criteria**:
- Ctrl+P opens prompt editor overlay
- Can select prompt type
- Overlay dismisses with Esc
- Modal doesn't block background

**Files to Create**:
- `llm_analysis/tui/screens/prompt_editor.py`

---

### Issue #23: Load current prompts from config
**Labels**: `phase-4`, `enhancement`, `priority-medium`, `backend`
**Milestone**: Phase 4: Prompt Lab
**Estimate**: 1 hour

**Description**:
Load existing prompts from config.py into editor.

**Tasks**:
- [ ] Create `config_manager.py` utility
- [ ] Implement `load_prompts()` method
- [ ] Parse prompt templates from config
- [ ] Handle missing/invalid prompts
- [ ] Add default prompt fallbacks
- [ ] Display prompts in editor

**Acceptance Criteria**:
- Current prompts load correctly
- Invalid prompts show warning
- Defaults used if prompts missing
- Prompts displayed with formatting

**Files to Create**:
- `llm_analysis/tui/utils/config_manager.py`

---

### Issue #24: Implement prompt template editor
**Labels**: `phase-4`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 4: Prompt Lab
**Estimate**: 1.5 hours

**Description**:
Create text editor for modifying prompt templates with variable highlighting.

**Tasks**:
- [ ] Add text editor to prompt overlay
- [ ] Highlight template variables (e.g., {transcript})
- [ ] Add syntax validation
- [ ] Show variable documentation
- [ ] Add template previews
- [ ] Validate on save

**Acceptance Criteria**:
- Can edit prompt text freely
- Variables highlighted clearly
- Validation catches errors
- Save only enabled when valid

**Files to Modify**:
- `llm_analysis/tui/screens/prompt_editor.py`

---

### Issue #25: Implement test on single interview
**Labels**: `phase-4`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 4: Prompt Lab
**Estimate**: 2 hours

**Description**:
Create prompt testing service to test prompts on individual interviews.

**Tasks**:
- [ ] Create `prompt_tester.py` service
- [ ] Implement `test_prompt()` method
- [ ] Load interview transcript
- [ ] Apply new prompt to Ollama
- [ ] Parse and validate JSON response
- [ ] Compare with existing analysis
- [ ] Return diff results

**Acceptance Criteria**:
- Can test prompt on any interview
- Results returned in <30 seconds
- JSON validation works
- Diff shows clear changes
- Error handling for failed tests

**Files to Create**:
- `llm_analysis/tui/services/prompt_tester.py`

---

### Issue #26: Create side-by-side result comparison
**Labels**: `phase-4`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 4: Prompt Lab
**Estimate**: 1.5 hours

**Description**:
Display test results side-by-side with existing analysis for comparison.

**Tasks**:
- [ ] Create comparison view layout
- [ ] Show existing analysis (left pane)
- [ ] Show new analysis (right pane)
- [ ] Highlight differences
- [ ] Add diff summary statistics
- [ ] Allow scrolling both panes in sync

**Acceptance Criteria**:
- Side-by-side view clear and readable
- Differences highlighted
- Synchronized scrolling
- Summary shows key changes

**Files to Modify**:
- `llm_analysis/tui/screens/prompt_editor.py`

---

### Issue #27: Implement prompt version saving
**Labels**: `phase-4`, `enhancement`, `priority-medium`, `backend`
**Milestone**: Phase 4: Prompt Lab
**Estimate**: 1.5 hours

**Description**:
Save prompt versions with history and rollback capability.

**Tasks**:
- [ ] Create `prompts/` directory structure
- [ ] Implement `save_prompt_version()` method
- [ ] Add timestamp and metadata
- [ ] Create version history UI
- [ ] Implement rollback functionality
- [ ] Add version comparison

**Acceptance Criteria**:
- Each save creates versioned file
- Can view version history
- Can rollback to previous version
- Versions include metadata (date, description)

**Files to Modify**:
- `llm_analysis/tui/utils/config_manager.py`
- `llm_analysis/tui/screens/prompt_editor.py`

---

### Issue #28: Implement batch re-analysis
**Labels**: `phase-4`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 4: Prompt Lab
**Estimate**: 2 hours

**Description**:
Enable re-running analysis on all 27 interviews with new prompt.

**Tasks**:
- [ ] Add "Re-run All" button to prompt editor
- [ ] Create batch processing workflow
- [ ] Add progress indicator (X/27 complete)
- [ ] Run in background thread
- [ ] Update analyses incrementally
- [ ] Handle failures gracefully
- [ ] Show completion summary

**Acceptance Criteria**:
- Can re-run all interviews from UI
- Progress indicator shows status
- Doesn't block TUI interaction
- Failed interviews reported clearly
- Results save automatically

**Files to Create/Modify**:
- `llm_analysis/tui/services/batch_analyzer.py`
- `llm_analysis/tui/screens/prompt_editor.py`

---

## Phase 5: Polish Issues

### Issue #29: Create data browser overlay
**Labels**: `phase-5`, `enhancement`, `priority-low`, `frontend`
**Milestone**: Phase 5: Polish
**Estimate**: 1.5 hours

**Description**:
Build Ctrl+D overlay for inspecting raw analysis data.

**Tasks**:
- [ ] Create `data_browser.py` screen
- [ ] Add Ctrl+D keybinding
- [ ] Create JSON viewer for interviews
- [ ] Add field aggregation view
- [ ] Create quote explorer
- [ ] Add statistics view
- [ ] Implement search/filter

**Acceptance Criteria**:
- Ctrl+D opens data browser
- Can inspect individual interview JSONs
- Can view aggregated fields
- Statistics accurate and helpful

**Files to Create**:
- `llm_analysis/tui/screens/data_browser.py`

---

### Issue #30: Implement help screen
**Labels**: `phase-5`, `enhancement`, `priority-medium`, `documentation`
**Milestone**: Phase 5: Polish
**Estimate**: 1 hour

**Description**:
Create help screen accessible with '?' showing all keybindings and commands.

**Tasks**:
- [ ] Add '?' keybinding
- [ ] Create help screen layout
- [ ] List all keyboard shortcuts
- [ ] List all chat commands
- [ ] Add feature descriptions
- [ ] Add search within help
- [ ] Make dismissible with Esc

**Acceptance Criteria**:
- '?' opens help screen
- All keybindings documented
- Help is searchable
- Easy to dismiss

**Files to Create**:
- `llm_analysis/tui/screens/help_screen.py`

---

### Issue #31: Add status bar with context info
**Labels**: `phase-5`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 5: Polish
**Estimate**: 1 hour

**Description**:
Create status bar showing current context, mode, and helpful information.

**Tasks**:
- [ ] Create status bar widget
- [ ] Show current section/interview
- [ ] Show current mode (view/edit)
- [ ] Show chat context mode
- [ ] Show unsaved changes indicator
- [ ] Show keybinding hints
- [ ] Update in real-time

**Acceptance Criteria**:
- Status bar always visible
- Information accurate and current
- Doesn't clutter interface
- Helpful for new users

**Files to Create**:
- `llm_analysis/tui/widgets/status_bar.py`

---

### Issue #32: Add theme/color customization
**Labels**: `phase-5`, `enhancement`, `priority-low`, `frontend`
**Milestone**: Phase 5: Polish
**Estimate**: 1 hour

**Description**:
Allow users to customize TUI theme and colors.

**Tasks**:
- [ ] Define theme configuration structure
- [ ] Create default themes (dark, light, monokai)
- [ ] Add theme selector to settings
- [ ] Apply theme to all widgets
- [ ] Save theme preference
- [ ] Add theme preview

**Acceptance Criteria**:
- Can switch between themes
- Theme persists across sessions
- All widgets respect theme
- Preview shows actual appearance

**Files to Create**:
- `llm_analysis/tui/themes.py`

**Files to Modify**:
- `llm_analysis/config.py`

---

### Issue #33: Implement error handling and user feedback
**Labels**: `phase-5`, `enhancement`, `priority-high`, `backend`
**Milestone**: Phase 5: Polish
**Estimate**: 1.5 hours

**Description**:
Add comprehensive error handling with clear user-facing messages.

**Tasks**:
- [ ] Create error notification system
- [ ] Add try/catch to all LLM calls
- [ ] Handle Ollama connection failures
- [ ] Handle file I/O errors
- [ ] Handle JSON parse errors
- [ ] Add error recovery suggestions
- [ ] Log errors for debugging

**Acceptance Criteria**:
- No unhandled exceptions
- Error messages clear and actionable
- Suggests recovery steps
- Logs technical details for debugging

**Files to Modify**:
- All service files
- All widget files

---

### Issue #34: Add loading indicators for LLM calls
**Labels**: `phase-5`, `enhancement`, `priority-medium`, `frontend`
**Milestone**: Phase 5: Polish
**Estimate**: 1 hour

**Description**:
Show loading spinners and progress indicators during LLM operations.

**Tasks**:
- [ ] Create loading indicator widget
- [ ] Show spinner during chat queries
- [ ] Show progress for batch operations
- [ ] Add estimated time remaining
- [ ] Allow cancellation of long operations
- [ ] Update status messages

**Acceptance Criteria**:
- Loading states clear and visible
- Progress accurate for batch jobs
- Can cancel long-running operations
- No frozen UI during processing

**Files to Create**:
- `llm_analysis/tui/widgets/loading_indicator.py`

---

### Issue #35: Implement command palette (Ctrl+K)
**Labels**: `phase-5`, `enhancement`, `priority-low`, `frontend`
**Milestone**: Phase 5: Polish
**Estimate**: 1.5 hours

**Description**:
Add command palette for fuzzy searching all available actions.

**Tasks**:
- [ ] Add Ctrl+K keybinding
- [ ] Create command palette overlay
- [ ] Index all available commands
- [ ] Implement fuzzy search
- [ ] Show command descriptions
- [ ] Execute selected command
- [ ] Show keybinding shortcuts

**Acceptance Criteria**:
- Ctrl+K opens command palette
- Can search all commands
- Fuzzy matching works well
- Commands execute correctly

**Files to Create**:
- `llm_analysis/tui/widgets/command_palette.py`

---

## Documentation Issues

### Issue #36: Create TUI user guide
**Labels**: `documentation`, `priority-medium`
**Milestone**: Phase 5: Polish
**Estimate**: 2 hours

**Description**:
Write comprehensive user guide for TUI usage.

**Tasks**:
- [ ] Document installation steps
- [ ] Document all features
- [ ] Add screenshot examples
- [ ] Document keyboard shortcuts
- [ ] Add troubleshooting section
- [ ] Add FAQ section

**Acceptance Criteria**:
- Complete feature coverage
- Clear examples
- Easy to follow
- Addresses common issues

**Files to Create**:
- `llm_analysis/tui/README.md`

---

### Issue #37: Add inline code documentation
**Labels**: `documentation`, `priority-low`, `testing`
**Milestone**: Phase 5: Polish
**Estimate**: 2 hours

**Description**:
Add docstrings and type hints throughout codebase.

**Tasks**:
- [ ] Add docstrings to all classes
- [ ] Add docstrings to all methods
- [ ] Add type hints to all functions
- [ ] Document complex algorithms
- [ ] Add usage examples in docstrings

**Acceptance Criteria**:
- 100% of public APIs documented
- Type hints on all functions
- Examples in critical methods
- Passes mypy type checking

**Files to Modify**:
- All Python files in `tui/`

---

## Testing Issues

### Issue #38: Create unit tests for services
**Labels**: `testing`, `priority-high`
**Estimate**: 4 hours

**Description**:
Write unit tests for all service layer components.

**Tasks**:
- [ ] Test `analysis_loader.py`
- [ ] Test `report_manager.py`
- [ ] Test `llm_service.py` (mocked)
- [ ] Test `prompt_tester.py` (mocked)
- [ ] Test `config_manager.py`
- [ ] Achieve >80% coverage

**Acceptance Criteria**:
- All services have test coverage
- Tests pass consistently
- Mocks used appropriately
- Coverage >80%

**Files to Create**:
- `llm_analysis/tests/tui/test_services.py`

---

### Issue #39: Create integration tests
**Labels**: `testing`, `priority-medium`
**Estimate**: 3 hours

**Description**:
Write integration tests for full workflows.

**Tasks**:
- [ ] Test launch → navigate → view workflow
- [ ] Test chat query → response workflow
- [ ] Test edit → save → reload workflow
- [ ] Test prompt edit → test → save workflow

**Acceptance Criteria**:
- Key workflows tested end-to-end
- Tests use real TUI components
- Tests run in CI/CD

**Files to Create**:
- `llm_analysis/tests/tui/test_workflows.py`

---

## Configuration & Setup Issues

### Issue #40: Update requirements.txt
**Labels**: `enhancement`, `priority-high`
**Estimate**: 15 minutes

**Description**:
Add all TUI dependencies to requirements.txt.

**Tasks**:
- [ ] Add `textual ^0.47.0`
- [ ] Add `rich ^13.7.0`
- [ ] Add `aiosqlite ^0.19.0`
- [ ] Add `watchdog ^4.0.0`
- [ ] Update existing dependencies if needed

**Files to Modify**:
- `llm_analysis/requirements.txt`

---

### Issue #41: Update config.py with TUI settings
**Labels**: `enhancement`, `priority-high`
**Estimate**: 30 minutes

**Description**:
Add TUI configuration section to config.py.

**Tasks**:
- [ ] Add `TUI_CONFIG` dictionary
- [ ] Add chat system prompt
- [ ] Add default settings
- [ ] Add path configurations
- [ ] Document all settings

**Files to Modify**:
- `llm_analysis/config.py`

---

### Issue #42: Create TUI entry point
**Labels**: `enhancement`, `priority-high`
**Estimate**: 15 minutes

**Description**:
Create convenient entry point script for launching TUI.

**Tasks**:
- [ ] Create `llm_analysis/tui.py` symlink
- [ ] Update README with launch instructions
- [ ] Add to setup.py if exists
- [ ] Test launch command

**Files to Create**:
- `llm_analysis/tui.py`

**Files to Modify**:
- `llm_analysis/README.md`

---

## Total Estimates by Phase

- **Phase 1**: 9 hours (actual estimate: 4-6 hours with optimization)
- **Phase 2**: 11 hours (actual estimate: 6-8 hours with optimization)
- **Phase 3**: 9 hours (actual estimate: 4-6 hours with optimization)
- **Phase 4**: 11.5 hours (actual estimate: 6-8 hours with optimization)
- **Phase 5**: 10 hours (actual estimate: 3-4 hours with optimization)
- **Documentation**: 4 hours
- **Testing**: 7 hours
- **Setup**: 1 hour

**Total**: ~62.5 hours (actual optimized: ~23-33 hours)

---

## Issue Creation Command Reference

Use GitHub CLI to create these issues:

```bash
# Phase 1 Issues
gh issue create --title "Set up Textual app boilerplate" --body-file issue_02.md --label "phase-1,enhancement,priority-high,backend" --milestone "Phase 1: Foundation"

# Phase 2 Issues
gh issue create --title "Create chat input widget" --body-file issue_08.md --label "phase-2,enhancement,priority-high,frontend" --milestone "Phase 2: Chat Integration"

# ... repeat for all issues
```

Or use the bulk creation script provided in the next file.
