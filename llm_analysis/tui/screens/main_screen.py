"""Main screen with 3-pane layout for TUI."""

from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Label
from textual.binding import Binding

from tui.widgets.navigator import NavigationTree
from tui.widgets.content_viewer import ContentViewer


class MainScreen(Screen):
    """Main screen with navigation, content, and chat panes."""

    BINDINGS = [
        Binding("e", "toggle_edit_mode", "Edit Mode", show=True),
        Binding("ctrl+p", "show_prompt_editor", "Prompts", show=True),
        Binding("ctrl+d", "show_data_browser", "Data", show=True),
        Binding("/", "search", "Search", show=True),
    ]

    def compose(self) -> ComposeResult:
        """Compose the main screen layout."""
        yield Header()

        # Main content area with horizontal split
        with Horizontal(id="main-container"):
            # Left pane - Navigation
            with Vertical(id="navigation-pane"):
                yield Label("📚 Navigation", id="navigation-pane-title")
                yield NavigationTree(id="navigation-tree")

            # Right pane - Content Viewer
            with Vertical(id="content-pane"):
                yield Label("📄 Content", id="content-pane-title")
                yield ContentViewer(id="content-viewer")

        # Bottom pane - Chat (placeholder for Phase 2)
        with Vertical(id="chat-pane"):
            yield Label("💬 Chat (Coming in Phase 2)", id="chat-pane-title")
            yield Static(
                "Chat functionality will be available in Phase 2.\n"
                "You'll be able to query analysis data and interact with findings.",
                classes="chat-placeholder"
            )

        yield Footer()

    def on_mount(self) -> None:
        """Initialize the main screen."""
        self.query_one("#navigation-tree", NavigationTree).focus()

    def on_navigation_tree_node_selected(self, event) -> None:
        """Handle navigation tree selection."""
        content_viewer = self.query_one("#content-viewer", ContentViewer)
        content_viewer.load_content(event.node)

    def action_toggle_edit_mode(self) -> None:
        """Toggle between view and edit mode (Phase 3)."""
        self.notify("Edit mode coming in Phase 3!")

    def action_show_prompt_editor(self) -> None:
        """Show prompt editor overlay (Phase 4)."""
        self.notify("Prompt editor coming in Phase 4!")

    def action_show_data_browser(self) -> None:
        """Show data browser overlay (Phase 5)."""
        self.notify("Data browser coming in Phase 5!")

    def action_search(self) -> None:
        """Show search interface (Phase 5)."""
        self.notify("Search coming in Phase 5!")
