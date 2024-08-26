import os
import json
from qgis.PyQt.QtWidgets import QFileDialog, QDialog
from qgis.core import QgsPointXY, QgsVectorLayer, QgsFeature, QgsGeometry, QgsField, QgsProject
from qgis.PyQt.QtCore import QVariant

class DirectoryWaypointPlugin:

    def __init__(self, iface):
        """Initialize the plugin with QGIS interface."""
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)

    def initGui(self):
        """Create the GUI elements of the plugin (e.g., toolbar buttons)."""
        #self.action = self.iface.addToolBarIcon(QIcon("icon.png"))
        self.action.setToolTip("Create waypoints from JSON files")
        self.action.triggered.connect(self.run)

    def unload(self):
        """Remove the plugin's GUI elements."""
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        """Main function that runs when the plugin is triggered."""
        dialog = MainDialog(self.iface)
        dialog.exec_()

class MainDialog(QDialog):

    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.initUI()

    def initUI(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory with JSON and PNG files")
        if directory:
            self.processDirectory(directory)
            self.accept()

    def processDirectory(self, directory):
        json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
        
        layer = QgsVectorLayer("Point?crs=EPSG:4326", "Waypoints", "memory")
        provider = layer.dataProvider()

        provider.addAttributes([QgsField("name", QVariant.String), QgsField("image", QVariant.String)])
        layer.updateFields()

        for json_file in json_files:
            json_path = os.path.join(directory, json_file)
            png_file = json_file.replace('.json', '.png')
            png_path = os.path.join(directory, png_file)

            with open(json_path, 'r') as file:
                data = json.load(file)
                name = os.path.splitext(json_file)[0]
                coord = data['coordinate']  # Assuming JSON structure is {"coordinate": [lon, lat]}
                point = QgsPointXY(coord[0], coord[1])

                feature = QgsFeature()
                feature.setGeometry(QgsGeometry.fromPointXY(point))
                feature.setAttributes([name, png_path])
                provider.addFeature(feature)

        layer.updateExtents()
        QgsProject.instance().addMapLayer(layer)

