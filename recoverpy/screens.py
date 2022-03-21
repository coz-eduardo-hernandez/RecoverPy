from typing import Any, Dict, Final, Type
from py_cui import PyCUI

from recoverpy.screens import (
    screen_config,
    screen_parameters,
    screen_results,
    screen_search,
)


class ViewsHandler:
    """Store UI windows instances and provide navigation logic.

    Attributes:
        _parameters_screen_window (PyCUI): Parameters window.
        _config_screen_window  (PyCUI): Config window.
        _search_screen_window (PyCUI): Search window.
        _results_screen_window (PyCUI): Results window.
    """

    SCREENS_CLASSES: Final[Dict[str, Type]] = {
        "parameters": screen_parameters.ParametersView,
        "config": screen_config.ConfigView,
        "search": screen_search.SearchView,
        "results": screen_results.ResultsView,
    }

    def __init__(self):
        """Initialize ViewsHandler."""
        # TO DO: Faire un dict de screens plutôt que x variables
        self.screens: Dict[str, Any] = {
            "parameters": None,
            "config": None,
            "search": None,
            "results": None,
        }
        self.current_screen = None
        self.previous_screen = None

    def create_screen(self):
        """Create a PyCUI instance with standard attributes.

        Returns:
            PyCUI: Created screen
        """
        screen = PyCUI(10, 10)
        screen.toggle_unicode_borders()
        screen.set_title("RecoverPy 1.5.0")

        return screen

    def open_screen(self, screen_name: str):
        self.screen[screen_name] = self.create_screen()
        self.SCREENS_CLASSES[screen_name](self.screen[screen_name])
        self.screen[screen_name].start()

        self.current_screen, self.previous_screen = screen_name, self.current_screen

    def close_screen(self, screen_name):
        if self.screen[screen_name] is None:
            return
        self.screen[screen_name].stop()

    def config_go_back(self):
        """Go back from config screen to parameters screen."""
        self.close_screen_config()
        self._parameters_screen_window._stopped = False
        self._parameters_screen_window.start()

    def results_go_back(self):
        """Go back from results screen to search screen."""
        self.close_screen_results()
        self._search_screen_window._stopped = False
        self._search_screen_window.start()


SCREENS_HANDLER = ViewsHandler()
