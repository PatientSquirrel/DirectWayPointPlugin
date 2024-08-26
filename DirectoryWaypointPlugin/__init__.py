from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsProject
from qgis.PyQt.QtWidgets import QAction
from .main import MainDialog
from .main import DirectoryWaypointPlugin
import os

def classFactory(iface):
    """Load DirectoryWaypointPlugin class from file main."""
    return DirectoryWaypointPlugin(iface)

class DirectoryWaypointPlugin:

    def __init__(self, iface):
        """Initialize the plugin with QGIS interface."""
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)

    def initGui(self):
        """Create the GUI elements of the plugin (e.g., toolbar buttons)."""
        # Create an action with an icon and text
        icon = QIcon(os.path.join(self.plugin_dir, "icon.png"))
        self.action = QAction(icon, "Create waypoints from JSON files", self.iface.mainWindow())

        # Connect the action to the plugin's run method
        self.action.triggered.connect(self.run)

        # Add the action to the QGIS toolbar
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        """Remove the plugin's GUI elements."""
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        """Main function that runs when the plugin is triggered."""
        dialog = MainDialog(self.iface)
        dialog.exec_()
