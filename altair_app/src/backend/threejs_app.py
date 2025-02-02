from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt
import os

class ThreeJsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt with Three.js")
        self.setGeometry(100, 100, 1024, 768)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(base_dir, "index.html")

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile(html_file))  

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
