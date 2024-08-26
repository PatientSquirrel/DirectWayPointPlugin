DirectoryWaypointPlugin

DirectoryWaypointPlugin is a QGIS plugin designed to create waypoints from JSON files containing coordinates and associate images with those waypoints. This plugin allows users to easily visualize data stored in JSON files on the QGIS map canvas.
Features

    Load waypoints from JSON files with coordinates.
    Associate images with waypoints based on file names.
    Easy integration into the QGIS interface.

Installation

    Download the Plugin:
        Obtain the plugin ZIP file or clone the repository from the source.

    Install the Plugin in QGIS:
        Open QGIS.
        Go to the Plugins menu and select Manage and Install Plugins....
        Click on the Install from ZIP tab.
        Browse to and select the ZIP file containing the DirectoryWaypointPlugin.
        Click Install Plugin.

    Verify Plugin Installation:
        After installation, you should see DirectoryWaypointPlugin listed in the installed plugins.
        Restart QGIS if necessary.

Setup

    /QGIS/QGIS3/profiles/default/python/plugin

    Prepare Your Data Directory:
        Create a directory with JSON files and corresponding PNG images.
        Each JSON file should follow this format:

        json

        {
            "coordinate": [longitude, latitude]
        }

        Ensure that each JSON file has a corresponding PNG image with the same name but different extensions (e.g., example.json should have a corresponding example.png).

    Run the Plugin:
        In QGIS, go to the Plugins menu and select DirectoryWaypointPlugin.
        Click on the plugin action button added to the toolbar.
        A file dialog will open prompting you to select the directory containing your JSON files and PNG images.
        Select the directory and the plugin will process the files, creating waypoints on the map at the coordinates specified in the JSON files and associating the images with those waypoints.

Usage

    Toolbar Button: Click the toolbar button added by the plugin to open the directory selection dialog.
    File Dialog: Navigate to and select the directory containing your JSON and PNG files.
    Waypoints: The plugin will add waypoints to the map based on the coordinates in the JSON files.

Troubleshooting

    Error: No section: 'general':
        Ensure the metadata.txt file is correctly formatted and located in the plugin directory.
    Error: ImportError: cannot import name 'DirectoryWaypointPlugin':
        Verify that the class name in main.py matches DirectoryWaypointPlugin.
    Error: QIcon Type Error:
        Make sure the action is correctly defined and connected in the initGui() method.



Contributions are welcome! Please submit a pull request or report issues to the plugin repository.
License

This plugin is licensed under the MIT License.


