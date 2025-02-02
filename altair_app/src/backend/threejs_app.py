from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtCore import QUrl, Qt
import os
import sys

class ThreeJsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window title and dimensions
        self.setWindowTitle("PyQt with Three.js")
        self.setGeometry(100, 100, 1024, 768)

        # Define path to the HTML file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(base_dir, "index.html")

        # Create the browser widget and set URL to the local HTML file
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile(html_file))  

        # Explicitly enables JavaScript
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)

        # Set up layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)    # creates a qapplicaion instance
    window = ThreeJsApp()           # creates instance of a main window
    window.show()                   # shows the window
    sys.exit(app.exec())            # starts the application's event loop