"""Content viewer widget for displaying markdown and analysis results."""

from pathlib import Path
from textual.widgets import Static, Markdown
from textual.containers import VerticalScroll


class ContentViewer(VerticalScroll):
    """Content viewer for displaying report sections and analysis data."""

    def on_mount(self) -> None:
        """Initialize the content viewer."""
        self.load_welcome_content()

    def load_welcome_content(self) -> None:
        """Load welcome/instructions content."""
        welcome_md = """
# Welcome to AI Customer Research TUI

## Getting Started

Use the **Navigation** pane (left) to browse:

- 📄 **Report** - View the analysis report sections
- 🎤 **Interviews** - Browse individual interview analyses
- 📈 **Aggregated Views** - See patterns across all interviews

## Keyboard Shortcuts

- `↑↓` - Navigate tree items
- `←→` - Expand/collapse nodes
- `Enter` - Select item
- `q` - Quit application
- `?` - Show help (Coming in Phase 5)

## What's Available Now (Phase 1)

✅ Navigation tree with report structure
✅ Content viewing with markdown rendering
✅ Keyboard navigation
✅ Three-pane layout

## Coming Soon

- **Phase 2**: Chat with LLM about findings
- **Phase 3**: Edit report directly in TUI
- **Phase 4**: Test and iterate on analysis prompts
- **Phase 5**: Data browser, themes, and polish

---

**Select an item from the navigation tree to view content.**
"""
        self.mount(Markdown(welcome_md))

    def load_content(self, node) -> None:
        """Load content based on selected navigation node."""
        try:
            # Clear existing content
            self.remove_children()

            node_data = node.data or {}
            content_type = node_data.get("type", "unknown")

            if content_type == "section":
                self.load_section_content(node_data)
            elif content_type == "interview":
                self.load_interview_content(node_data)
            elif content_type == "aggregated_view":
                self.load_aggregated_view(node_data)
            elif content_type == "report":
                self.load_full_report()
            elif content_type == "interviews":
                self.load_interviews_overview()
            elif content_type == "aggregated":
                self.load_aggregated_overview()
            else:
                self.load_placeholder_content(node.label)

        except Exception as e:
            self.mount(Markdown(f"# Error\n\nFailed to load content: {e}"))

    def load_section_content(self, data: dict) -> None:
        """Load specific report section content."""
        section_name = data.get("name", "Unknown Section")

        # Try to load from actual report file
        report_path = Path(__file__).parent.parent.parent / "output" / "FINAL_ANALYSIS_REPORT.md"

        if report_path.exists():
            content = report_path.read_text()
            # Extract section (simplified - would need better parsing)
            self.mount(Markdown(f"# {section_name}\n\n*Content from: {report_path.name}*\n\n{content[:2000]}..."))
        else:
            placeholder = f"""
# {section_name}

*This section will display content from the analysis report.*

## Section Preview

This would show the actual content from the **{section_name}** section of your analysis report.

In Phase 2, you'll be able to:
- Ask questions about this section
- Get summaries and insights
- Compare findings across interviews

---

**Note**: Report file not found at expected location.
Make sure analysis has been run and report generated.
"""
            self.mount(Markdown(placeholder))

    def load_interview_content(self, data: dict) -> None:
        """Load individual interview content."""
        interview_id = data.get("id", "?")
        interview_path = data.get("path", "")

        if interview_path and Path(interview_path).exists():
            # Load actual interview analysis
            analysis_path = Path(interview_path).with_suffix('_analysis.json')
            if analysis_path.exists():
                import json
                try:
                    analysis_data = json.loads(analysis_path.read_text())
                    md = self.format_interview_analysis(interview_id, analysis_data)
                    self.mount(Markdown(md))
                    return
                except Exception as e:
                    pass

        # Placeholder content
        placeholder = f"""
# Interview {interview_id}

## Overview

*This would display the analysis for Interview {interview_id}*

### Key Findings
- Finding 1
- Finding 2
- Finding 3

### Pain Points
- Pain point 1
- Pain point 2

### Desires
- Desire 1
- Desire 2

---

**Note**: In Phase 2, you'll be able to chat with this interview data and ask specific questions.
"""
        self.mount(Markdown(placeholder))

    def format_interview_analysis(self, interview_id: str, data: dict) -> str:
        """Format interview analysis JSON as markdown."""
        md = f"# Interview {interview_id}\n\n"

        for key, value in data.items():
            md += f"## {key.replace('_', ' ').title()}\n\n"
            if isinstance(value, list):
                for item in value:
                    md += f"- {item}\n"
            else:
                md += f"{value}\n"
            md += "\n"

        return md

    def load_aggregated_view(self, data: dict) -> None:
        """Load aggregated view across interviews."""
        view_type = data.get("view", "unknown")

        placeholder = f"""
# {view_type.replace('_', ' ').title()}

*This view aggregates data across all 27 interviews*

## Coming in Phase 2

This view will show:
- Frequency analysis
- Common patterns
- Quote aggregation
- Cross-interview comparisons

---

**Select individual interviews or report sections to view specific content.**
"""
        self.mount(Markdown(placeholder))

    def load_full_report(self) -> None:
        """Load the full analysis report."""
        report_path = Path(__file__).parent.parent.parent / "output" / "FINAL_ANALYSIS_REPORT.md"

        if report_path.exists():
            content = report_path.read_text()
            self.mount(Markdown(content))
        else:
            placeholder = """
# Analysis Report

*Full analysis report will be displayed here.*

## Missing Report

The analysis report was not found at the expected location.

Please run the analysis first:
```bash
cd llm_analysis
python analyze_interviews.py
python synthesize_report.py
```

---

**Navigate to specific sections using the navigation tree.**
"""
            self.mount(Markdown(placeholder))

    def load_interviews_overview(self) -> None:
        """Load interviews overview."""
        content = """
# Interviews Overview

## All Interviews (27 total)

Use the navigation tree to browse individual interviews.

Each interview includes:
- Raw transcript
- AI-generated analysis
- Key findings and themes
- Pain points and desires
- Trust factors

---

**Expand the Interviews node to view individual interviews.**
"""
        self.mount(Markdown(content))

    def load_aggregated_overview(self) -> None:
        """Load aggregated views overview."""
        content = """
# Aggregated Views

## Available Views

- **📋 All Quotes** - Verbatim quotes organized by topic
- **🏷️ Themes by Frequency** - Most common themes across interviews
- **😟 Pain Points by Category** - Organized pain points
- **🎯 Desires by Priority** - User needs and wants
- **🔒 Trust Factors** - What builds or breaks trust

---

**Select a specific view from the navigation tree.**
"""
        self.mount(Markdown(content))

    def load_placeholder_content(self, label: str) -> None:
        """Load placeholder content for unknown types."""
        content = f"""
# {label}

*Content will be loaded here when implemented.*

---

**This feature is under development.**
"""
        self.mount(Markdown(content))
