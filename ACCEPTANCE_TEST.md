# Phase 1 TUI - Acceptance Testing Guide

**Date**: November 25, 2025
**Version**: Phase 1 - Foundation
**Tester**: Marco

## Pre-Test Setup ✅

- [x] Dependencies installed: `pip install -r requirements.txt`
- [x] All imports successful
- [x] File structure verified
- [x] App instantiates without errors

## Launch Instructions

```bash
cd "/Users/marco/Documents/ai for customer research/llm_analysis"
python3 tui.py
```

**Expected**: TUI launches in your terminal

---

## Acceptance Test Checklist

### Test 1: Application Launch ⏳

**Objective**: Verify TUI launches without errors

**Steps**:
1. Run `python3 tui.py`
2. Observe the startup

**Expected Results**:
- [ ] Application launches within 2 seconds
- [ ] No error messages appear
- [ ] Terminal clears and shows TUI interface
- [ ] Title bar shows "AI Customer Research - Interview Analysis"
- [ ] Footer shows available keyboard shortcuts

**Actual Results**:
- Outcome: _____________
- Notes: _____________

---

### Test 2: Three-Pane Layout ⏳

**Objective**: Verify all three panes are visible and properly sized

**Steps**:
1. After launch, observe the layout
2. Resize terminal window (if possible)

**Expected Results**:
- [ ] Left pane visible (Navigation) - approximately 30% width
- [ ] Right pane visible (Content) - approximately 70% width
- [ ] Bottom pane visible (Chat) - approximately 20% height
- [ ] Each pane has clear borders
- [ ] Pane titles are visible and readable
- [ ] Layout adapts when terminal resized

**Actual Results**:
- Left pane: _____________
- Right pane: _____________
- Bottom pane: _____________
- Resizing: _____________

---

### Test 3: Navigation Tree Structure ⏳

**Objective**: Verify navigation tree displays correctly

**Steps**:
1. Focus on left pane (navigation)
2. Observe the tree structure

**Expected Results**:
- [ ] Root node "📊 Analysis" is visible
- [ ] Three main sections visible:
  - [ ] 📄 Report
  - [ ] 🎤 Interviews (27)
  - [ ] 📈 Aggregated Views
- [ ] Icons/emojis display correctly
- [ ] Tree is readable and not cut off
- [ ] Root node is expanded by default

**Actual Results**:
- Structure: _____________
- Icons: _____________
- Notes: _____________

---

### Test 4: Keyboard Navigation - Arrow Keys ⏳

**Objective**: Verify arrow key navigation works

**Steps**:
1. Press `↓` (down arrow) multiple times
2. Press `↑` (up arrow) multiple times
3. Press `→` (right arrow) on "Report" node
4. Press `←` (left arrow) on expanded node

**Expected Results**:
- [ ] `↓` moves selection down one item
- [ ] `↑` moves selection up one item
- [ ] `→` expands collapsed nodes (shows children)
- [ ] `←` collapses expanded nodes (hides children)
- [ ] Current selection is clearly highlighted
- [ ] Navigation wraps or stops at boundaries
- [ ] No lag or delay in navigation

**Actual Results**:
- Down arrow: _____________
- Up arrow: _____________
- Right arrow (expand): _____________
- Left arrow (collapse): _____________
- Highlighting: _____________

---

### Test 5: Node Selection with Enter ⏳

**Objective**: Verify Enter key selects items and loads content

**Steps**:
1. Navigate to "Report" node
2. Press `Enter`
3. Navigate to a specific section (e.g., "Executive Summary")
4. Press `Enter`
5. Navigate to "Interviews" node
6. Expand and select an interview
7. Press `Enter`

**Expected Results**:
- [ ] Pressing Enter on "Report" loads report overview
- [ ] Content pane updates with selected content
- [ ] Pressing Enter on section loads that section
- [ ] Section content displays in right pane
- [ ] Pressing Enter on interview loads interview data
- [ ] Content updates happen smoothly (<500ms)
- [ ] No error messages appear

**Actual Results**:
- Report selection: _____________
- Section selection: _____________
- Interview selection: _____________
- Content loading speed: _____________

---

### Test 6: Content Display - Markdown Rendering ⏳

**Objective**: Verify content displays correctly with markdown formatting

**Steps**:
1. Select various items from navigation
2. Observe content in right pane
3. Scroll through content using arrow keys or mouse

**Expected Results**:
- [ ] Markdown headers render with formatting
- [ ] Bold/italic text displays correctly
- [ ] Lists (bulleted/numbered) format properly
- [ ] Code blocks have syntax highlighting
- [ ] Links are visible (even if not clickable)
- [ ] Content is readable and not cut off
- [ ] Scrolling works smoothly
- [ ] Long content shows scrollbar

**Actual Results**:
- Headers: _____________
- Formatting: _____________
- Code blocks: _____________
- Scrolling: _____________

---

### Test 7: Welcome Content ⏳

**Objective**: Verify welcome/default content displays

**Steps**:
1. Launch TUI (should show welcome by default)
2. Read the welcome content

**Expected Results**:
- [ ] Welcome content displays on launch
- [ ] Content includes:
  - [ ] Title "Welcome to AI Customer Research TUI"
  - [ ] Getting Started instructions
  - [ ] Keyboard shortcuts list
  - [ ] Phase status information
- [ ] Formatting is clear and readable

**Actual Results**:
- Welcome displays: _____________
- Content complete: _____________
- Readability: _____________

---

### Test 8: Chat Pane Placeholder ⏳

**Objective**: Verify chat pane shows placeholder for Phase 2

**Steps**:
1. Observe bottom pane
2. Read the placeholder message

**Expected Results**:
- [ ] Bottom pane labeled "💬 Chat (Coming in Phase 2)"
- [ ] Placeholder text explains feature coming in Phase 2
- [ ] Text is readable
- [ ] Pane is clearly separated from others

**Actual Results**:
- Label: _____________
- Message: _____________

---

### Test 9: Quit Functionality ⏳

**Objective**: Verify 'q' key quits the application

**Steps**:
1. With TUI running, press `q`
2. Observe behavior

**Expected Results**:
- [ ] Application exits immediately
- [ ] Terminal returns to normal prompt
- [ ] No error messages on exit
- [ ] Terminal state restored properly

**Actual Results**:
- Exit behavior: _____________
- Clean exit: _____________

---

### Test 10: Keyboard Shortcut Indicators ⏳

**Objective**: Verify placeholder shortcuts show notifications

**Steps**:
1. Press `?` (help)
2. Press `e` (edit mode)
3. Press `Ctrl+P` (prompt editor)
4. Press `Ctrl+D` (data browser)
5. Press `/` (search)

**Expected Results**:
- [ ] Each key shows a notification message
- [ ] Messages indicate feature coming in later phase
- [ ] Notifications are visible and readable
- [ ] Notifications dismiss automatically or with key
- [ ] No crashes or errors

**Actual Results**:
- Help (?): _____________
- Edit (e): _____________
- Prompts (Ctrl+P): _____________
- Data (Ctrl+D): _____________
- Search (/): _____________

---

### Test 11: Terminal Resizing ⏳

**Objective**: Verify TUI adapts to terminal size changes

**Steps**:
1. With TUI running, resize terminal window:
   - Make it wider
   - Make it narrower
   - Make it taller
   - Make it shorter
2. Observe layout adaptation

**Expected Results**:
- [ ] Layout adapts to width changes
- [ ] Layout adapts to height changes
- [ ] Panes remain proportional
- [ ] Content remains readable
- [ ] No visual glitches or overlapping
- [ ] Scrollbars appear/disappear as needed

**Actual Results**:
- Width changes: _____________
- Height changes: _____________
- Visual quality: _____________

---

### Test 12: Multiple Content Types ⏳

**Objective**: Verify different content types load correctly

**Steps**:
1. Select "Report" node → observe content
2. Select "Executive Summary" section → observe content
3. Select "Interviews" overview → observe content
4. Select individual interview → observe content
5. Select "Aggregated Views" overview → observe content
6. Select specific aggregated view → observe content

**Expected Results**:
- [ ] Each content type displays appropriate content
- [ ] No crashes when switching between types
- [ ] Content makes sense for selected item
- [ ] Formatting appropriate for content type

**Actual Results**:
- Report: _____________
- Section: _____________
- Interview: _____________
- Aggregated: _____________

---

## Performance Tests

### Test P1: Startup Time ⏳

**Steps**: Time from `python3 tui.py` command to TUI fully displayed

**Expected**: < 2 seconds

**Actual**: _________ seconds

---

### Test P2: Navigation Responsiveness ⏳

**Steps**: Press arrow keys rapidly, observe lag

**Expected**: Immediate response, no visible lag

**Actual**: _____________

---

### Test P3: Content Loading Time ⏳

**Steps**: Time from pressing Enter to content displayed

**Expected**: < 500ms

**Actual**: _________ ms

---

### Test P4: Memory Usage ⏳

**Steps**: Check memory usage with Activity Monitor while TUI running

**Expected**: < 100MB

**Actual**: _________ MB

---

## Edge Cases & Error Handling

### Test E1: Rapid Key Presses ⏳

**Steps**: Press keys very rapidly (navigation, selection)

**Expected**: No crashes, responses queued properly

**Actual**: _____________

---

### Test E2: Missing Data Files ⏳

**Steps**: Note behavior when analysis files don't exist

**Expected**: Graceful fallback to placeholder content

**Actual**: _____________

---

### Test E3: Very Long Content ⏳

**Steps**: Select item with long content, test scrolling

**Expected**: Smooth scrolling, no memory issues

**Actual**: _____________

---

## Success Criteria Summary

**Phase 1 Success Criteria** (from Epic #1):
- [ ] ✅ Can launch TUI from command line
- [ ] ✅ Can navigate report sections using arrow keys
- [ ] ✅ Can view markdown content with proper rendering
- [ ] ✅ Keyboard shortcuts work (↑↓←→, Enter, q)

---

## Final Assessment

### Overall Rating: _____ / 10

### Issues Found:
1. _____________
2. _____________
3. _____________

### Recommendations:
1. _____________
2. _____________
3. _____________

### Ready for Phase 2? [ ] Yes [ ] No

**Notes**:
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

---

## Sign-off

**Tester**: _______________
**Date**: _______________
**Status**: [ ] PASS [ ] FAIL [ ] PASS WITH ISSUES

**Next Steps**:
- [ ] Fix any critical issues
- [ ] Update requirements.txt (if needed)
- [ ] Commit test results
- [ ] Begin Phase 2 implementation
