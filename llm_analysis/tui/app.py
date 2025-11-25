"""Main TUI application for AI Customer Research analysis."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container
from tui.screens.main_screen import MainScreen


class InterviewAnalysisTUI(App):
    """Interview Analysis Terminal User Interface."""

    TITLE = "AI Customer Research - Interview Analysis"
    CSS_PATH = "app.css"

    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),
        Binding("ctrl+c", "quit", "Quit", show=False),
        Binding("?", "help", "Help"),
    ]

    def on_mount(self) -> None:
        """Initialize the application."""
        self.push_screen(MainScreen())

    def action_help(self) -> None:
        """Show help screen."""
        self.notify("Help screen coming in Phase 5!")

    def action_quit(self) -> None:
        """Quit the application."""
        self.exit()


def main():
    """Entry point for the TUI application."""
    app = InterviewAnalysisTUI()
    app.run()


if __name__ == "__main__":
    main()
