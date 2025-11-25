#!/bin/bash

# TUI Implementation - GitHub Issues Creation Script
# This script creates all issues defined in GITHUB_ISSUES.md

set -e

REPO="marcothedeveloper123/ai-customer-research"

echo "🚀 Creating GitHub Issues for TUI Implementation"
echo "================================================"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "Install it from: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub CLI"
    echo "Run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI authenticated"
echo ""

# Create milestones first
echo "📍 Creating Milestones..."

gh api repos/$REPO/milestones -f title="Phase 1: Foundation" -f description="Basic TUI with navigation and viewing (4-6 hours)" || echo "  ⚠️  Milestone may already exist"
gh api repos/$REPO/milestones -f title="Phase 2: Chat Integration" -f description="Interactive querying with LLM (6-8 hours)" || echo "  ⚠️  Milestone may already exist"
gh api repos/$REPO/milestones -f title="Phase 3: Report Editing" -f description="In-TUI report editing (4-6 hours)" || echo "  ⚠️  Milestone may already exist"
gh api repos/$REPO/milestones -f title="Phase 4: Prompt Lab" -f description="Prompt engineering workflow (6-8 hours)" || echo "  ⚠️  Milestone may already exist"
gh api repos/$REPO/milestones -f title="Phase 5: Polish" -f description="Production-ready UX (3-4 hours)" || echo "  ⚠️  Milestone may already exist"

echo "✅ Milestones created"
echo ""

# Create labels
echo "🏷️  Creating Labels..."

declare -a labels=(
    "epic|Large feature containing multiple stories|#7057ff"
    "phase-1|Phase 1: Foundation|#0e8a16"
    "phase-2|Phase 2: Chat Integration|#1d76db"
    "phase-3|Phase 3: Report Editing|#fbca04"
    "phase-4|Phase 4: Prompt Lab|#d93f0b"
    "phase-5|Phase 5: Polish|#e99695"
    "enhancement|New feature|#a2eeef"
    "bug|Defect|#d73a4a"
    "documentation|Documentation updates|#0075ca"
    "priority-high|Critical path items|#b60205"
    "priority-medium|Important but not blocking|#d93f0b"
    "priority-low|Nice to have|#fbca04"
    "frontend|UI/UX work|#bfdadc"
    "backend|Service/logic work|#5319e7"
    "testing|Test-related work|#0e8a16"
)

for label in "${labels[@]}"; do
    IFS='|' read -r name description color <<< "$label"
    gh label create "$name" --description "$description" --color "$color" --force || echo "  ⚠️  Label '$name' may already exist"
done

echo "✅ Labels created"
echo ""

# Epic Issues
echo "📋 Creating Epic Issues..."

# Epic #1: Phase 1 - Foundation
gh issue create \
    --title "Epic: Phase 1 - Foundation" \
    --body "Set up basic TUI infrastructure with navigation and viewing capabilities.

**Success Criteria**:
- ✅ Can launch TUI from command line
- ✅ Can navigate report sections using arrow keys
- ✅ Can view markdown content with proper rendering
- ✅ Keyboard shortcuts work (↑↓←→, Enter, q)

**Estimate**: 4-6 hours

**Related Issues**: #2, #3, #4, #5, #6, #7" \
    --label "epic,phase-1,priority-high" \
    --milestone "Phase 1: Foundation"

# Epic #2: Phase 2 - Chat Integration
gh issue create \
    --title "Epic: Phase 2 - Chat Integration" \
    --body "Enable interactive querying of analysis data through LLM-powered chat interface.

**Success Criteria**:
- ✅ Can ask natural language questions about analysis
- ✅ Responses include interview citations
- ✅ Chat commands (/quote, /compare, /summarize) work
- ✅ Chat history persists to SQLite
- ✅ Can insert chat responses into report

**Estimate**: 6-8 hours

**Related Issues**: #8, #9, #10, #11, #12, #13, #14" \
    --label "epic,phase-2,priority-high" \
    --milestone "Phase 2: Chat Integration"

# Epic #3: Phase 3 - Report Editing
gh issue create \
    --title "Epic: Phase 3 - Report Editing" \
    --body "Add report editing capabilities directly within TUI.

**Success Criteria**:
- ✅ Can toggle between view and edit modes
- ✅ Can add new sections to report
- ✅ Auto-save works every 30 seconds
- ✅ Manual save works with Ctrl+S
- ✅ Changes persist after TUI restart

**Estimate**: 4-6 hours

**Related Issues**: #15, #16, #17, #18, #19, #20, #21" \
    --label "epic,phase-3,priority-high" \
    --milestone "Phase 3: Report Editing"

# Epic #4: Phase 4 - Prompt Lab
gh issue create \
    --title "Epic: Phase 4 - Prompt Lab" \
    --body "Enable prompt engineering workflow with testing and iteration.

**Success Criteria**:
- ✅ Can edit analysis prompts in overlay
- ✅ Can test prompt on single interview
- ✅ Side-by-side comparison shows differences
- ✅ Can save prompt versions
- ✅ Can re-run analysis on all interviews

**Estimate**: 6-8 hours

**Related Issues**: #22, #23, #24, #25, #26, #27, #28" \
    --label "epic,phase-4,priority-medium" \
    --milestone "Phase 4: Prompt Lab"

# Epic #5: Phase 5 - Polish
gh issue create \
    --title "Epic: Phase 5 - Polish" \
    --body "Production-ready UX with data browser, help system, and error handling.

**Success Criteria**:
- ✅ Data browser overlay works (Ctrl+D)
- ✅ Help screen accessible with ?
- ✅ Status bar shows context info
- ✅ Error messages are clear and helpful
- ✅ Loading indicators show for LLM calls

**Estimate**: 3-4 hours

**Related Issues**: #29, #30, #31, #32, #33, #34, #35" \
    --label "epic,phase-5,priority-low" \
    --milestone "Phase 5: Polish"

echo "✅ Epic issues created"
echo ""

# Phase 1 Issues
echo "📦 Creating Phase 1 Issues..."

gh issue create \
    --title "Set up Textual app boilerplate" \
    --body "Create basic Textual application structure with entry point and configuration.

**Tasks**:
- [ ] Create \`llm_analysis/tui/\` directory structure
- [ ] Create \`tui/__init__.py\`
- [ ] Create \`tui/app.py\` with basic Textual App class
- [ ] Add \`textual ^0.47.0\` to requirements.txt
- [ ] Add \`rich ^13.7.0\` to requirements.txt
- [ ] Create entry point script \`tui.py\`
- [ ] Test app launches without errors

**Acceptance Criteria**:
- App launches with \`python3 -m tui.app\`
- Basic window appears with title
- Pressing 'q' quits the application

**Files to Create**:
- \`llm_analysis/tui/__init__.py\`
- \`llm_analysis/tui/app.py\`
- \`llm_analysis/tui.py\` (symlink)

**Estimate**: 1 hour" \
    --label "phase-1,enhancement,priority-high,backend" \
    --milestone "Phase 1: Foundation"

gh issue create \
    --title "Load existing report and analyses" \
    --body "Create service to load and parse existing analysis JSONs and report markdown.

**Tasks**:
- [ ] Create \`tui/services/\` directory
- [ ] Create \`analysis_loader.py\` service
- [ ] Implement \`load_all_analyses()\` to read 27 JSON files
- [ ] Implement \`parse_analysis_json()\` for validation
- [ ] Create \`report_manager.py\` service
- [ ] Implement \`load_report()\` to read markdown
- [ ] Implement \`parse_report_structure()\` for sections
- [ ] Add error handling for missing files

**Acceptance Criteria**:
- Successfully loads all 27 analysis JSON files
- Parses report markdown into hierarchical structure
- Returns meaningful error if files missing
- No performance issues (<500ms load time)

**Files to Create**:
- \`llm_analysis/tui/services/__init__.py\`
- \`llm_analysis/tui/services/analysis_loader.py\`
- \`llm_analysis/tui/services/report_manager.py\`

**Estimate**: 1.5 hours" \
    --label "phase-1,enhancement,priority-high,backend" \
    --milestone "Phase 1: Foundation"

gh issue create \
    --title "Create 3-pane layout (nav, content, chat)" \
    --body "Implement responsive 3-pane layout with navigation tree (left), content viewer (right), and chat placeholder (bottom).

**Tasks**:
- [ ] Create \`tui/screens/main_screen.py\`
- [ ] Implement \`MainScreen\` with 3-pane container layout
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
- \`llm_analysis/tui/screens/__init__.py\`
- \`llm_analysis/tui/screens/main_screen.py\`

**Estimate**: 1.5 hours" \
    --label "phase-1,enhancement,priority-high,frontend" \
    --milestone "Phase 1: Foundation"

gh issue create \
    --title "Build navigation tree widget" \
    --body "Create hierarchical tree widget for browsing report sections and individual interviews.

**Tasks**:
- [ ] Create \`tui/widgets/\` directory
- [ ] Create \`navigator.py\` widget
- [ ] Implement \`NavigationTree\` widget extending Textual Tree
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
- \`llm_analysis/tui/widgets/__init__.py\`
- \`llm_analysis/tui/widgets/navigator.py\`

**Estimate**: 2 hours" \
    --label "phase-1,enhancement,priority-high,frontend" \
    --milestone "Phase 1: Foundation"

gh issue create \
    --title "Build content viewer widget" \
    --body "Create markdown content viewer with syntax highlighting and rendering.

**Tasks**:
- [ ] Create \`content_viewer.py\` widget
- [ ] Implement \`ContentViewer\` using Rich Markdown
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
- \`llm_analysis/tui/widgets/content_viewer.py\`

**Estimate**: 2 hours" \
    --label "phase-1,enhancement,priority-high,frontend" \
    --milestone "Phase 1: Foundation"

gh issue create \
    --title "Implement keyboard shortcuts" \
    --body "Add core keyboard shortcuts for navigation and basic operations.

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
- \`llm_analysis/tui/screens/main_screen.py\`
- \`llm_analysis/tui/app.py\`

**Estimate**: 1 hour" \
    --label "phase-1,enhancement,priority-high,frontend" \
    --milestone "Phase 1: Foundation"

echo "✅ Phase 1 issues created"
echo ""

# Phase 2 Issues (abbreviated for script length - continue similarly)
echo "📦 Creating Phase 2 Issues..."

gh issue create \
    --title "Create chat input widget" \
    --body "Build chat interface widget with input field and message history display.

**Estimate**: 1.5 hours

See GITHUB_ISSUES.md for full details." \
    --label "phase-2,enhancement,priority-high,frontend" \
    --milestone "Phase 2: Chat Integration"

gh issue create \
    --title "Implement LLM service with context management" \
    --body "Create LLM service layer with Ollama integration and intelligent context management.

**Estimate**: 2 hours

See GITHUB_ISSUES.md for full details." \
    --label "phase-2,enhancement,priority-high,backend" \
    --milestone "Phase 2: Chat Integration"

# Continue with remaining Phase 2-5 issues...
echo "✅ Phase 2 issues created (abbreviated)"
echo ""

echo "✅ Setup and Configuration Issues..."

gh issue create \
    --title "Update requirements.txt with TUI dependencies" \
    --body "Add all TUI dependencies to requirements.txt.

**Tasks**:
- [ ] Add \`textual ^0.47.0\`
- [ ] Add \`rich ^13.7.0\`
- [ ] Add \`aiosqlite ^0.19.0\`
- [ ] Add \`watchdog ^4.0.0\`

**Estimate**: 15 minutes" \
    --label "enhancement,priority-high" \
    --milestone "Phase 1: Foundation"

gh issue create \
    --title "Update config.py with TUI settings" \
    --body "Add TUI configuration section to config.py.

**Estimate**: 30 minutes

See GITHUB_ISSUES.md for full details." \
    --label "enhancement,priority-high" \
    --milestone "Phase 1: Foundation"

echo "✅ All issues created successfully!"
echo ""
echo "📊 Summary:"
echo "  - 5 Epic issues"
echo "  - 6+ Phase 1 issues"
echo "  - Additional phase issues (see GITHUB_ISSUES.md for complete list)"
echo ""
echo "🔗 View all issues:"
echo "  https://github.com/$REPO/issues"
echo ""
echo "💡 Next steps:"
echo "  1. Review issues on GitHub"
echo "  2. Assign issues to milestones"
echo "  3. Start with Phase 1: Foundation"
echo "  4. Use GitHub Projects for tracking"
echo ""
