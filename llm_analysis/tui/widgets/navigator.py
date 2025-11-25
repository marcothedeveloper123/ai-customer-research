"""Navigation tree widget for browsing report structure."""

from pathlib import Path
from textual.widgets import Tree
from textual.widgets.tree import TreeNode


class NavigationTree(Tree):
    """Navigation tree for browsing analysis structure."""

    def __init__(self, *args, **kwargs):
        """Initialize the navigation tree with label."""
        # Tree requires a label parameter
        super().__init__("📊 Analysis", *args, **kwargs)
        self.show_root = True
        self.guide_depth = 4

    def on_mount(self) -> None:
        """Initialize the navigation tree."""
        # Build the tree structure
        self.build_tree()

    def build_tree(self) -> None:
        """Build the navigation tree from analysis data."""
        try:
            # Root node (already set in __init__)
            root = self.root
            root.expand()

            # Add Report node
            report_node = root.add("📄 Report", data={"type": "report"})
            self.add_report_sections(report_node)

            # Add Interviews node
            interviews_node = root.add("🎤 Interviews (27)", data={"type": "interviews"})
            self.add_interviews(interviews_node)

            # Add Aggregated Views node
            aggregated_node = root.add("📈 Aggregated Views", data={"type": "aggregated"})
            self.add_aggregated_views(aggregated_node)

        except Exception as e:
            self.notify(f"Error building tree: {e}", severity="error")

    def add_report_sections(self, parent: TreeNode) -> None:
        """Add report sections to the tree."""
        # These would be loaded from the actual report structure
        # For now, adding placeholder sections
        sections = [
            "Executive Summary",
            "Key Findings",
            "Themes & Patterns",
            "Pain Points",
            "Desires & Needs",
            "Trust Factors",
            "Recommendations",
        ]

        for section in sections:
            parent.add_leaf(
                f"📝 {section}",
                data={"type": "section", "name": section}
            )

    def add_interviews(self, parent: TreeNode) -> None:
        """Add individual interviews to the tree."""
        # Check for interview files
        interview_path = Path(__file__).parent.parent.parent / "AI for Customer Research Nov 2025"

        if interview_path.exists():
            # Load actual interview files
            docx_files = sorted(interview_path.glob("*.docx"))
            for idx, file in enumerate(docx_files, 1):
                parent.add_leaf(
                    f"👤 Interview {idx}: {file.stem[:30]}...",
                    data={"type": "interview", "path": str(file)}
                )
        else:
            # Placeholder interviews
            for i in range(1, 28):
                parent.add_leaf(
                    f"👤 Interview {i}",
                    data={"type": "interview", "id": i}
                )

    def add_aggregated_views(self, parent: TreeNode) -> None:
        """Add aggregated view options to the tree."""
        views = [
            ("📋 All Quotes", "quotes"),
            ("🏷️ Themes by Frequency", "themes"),
            ("😟 Pain Points by Category", "pain_points"),
            ("🎯 Desires by Priority", "desires"),
            ("🔒 Trust Factors", "trust"),
        ]

        for label, view_type in views:
            parent.add_leaf(
                label,
                data={"type": "aggregated_view", "view": view_type}
            )

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        """Handle node selection."""
        node = event.node
        if node.data:
            self.post_message(self.NodeSelected(node))

    class NodeSelected(Tree.NodeSelected):
        """Custom event for node selection with data."""
        pass
