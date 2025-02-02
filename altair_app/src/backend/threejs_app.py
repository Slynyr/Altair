import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtCore import QUrl
from backend.gen_manager import GenManager
from backend.gen_worker import GenPaperWorker
from PyQt6.QtCore import QThread

class NoDragWebEngineView(QWebEngineView):
    """QWebEngineView subclass that ignores drag events to let the parent handle them."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(False)

    def dragEnterEvent(self, event):
        event.ignore()

    def dropEvent(self, event):
        event.ignore()

class ThreeJsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m_GenManager = GenManager()

        self.setWindowTitle("PyQt with Three.js")
        self.setGeometry(100, 100, 1024, 768)

        # Let the main window accept drops
        self.setAcceptDrops(True)

        # Prepare the web view (NoDrag subclass)
        self.browser = NoDragWebEngineView()

        # Point to your local "index.html"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(base_dir, "index.html")
        self.browser.setUrl(QUrl.fromLocalFile(html_file))

        # Enable JavaScript, etc.
        self.browser.settings().setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptEnabled, True
        )
        self.browser.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True
        )

        # Layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.browser)
        self.setCentralWidget(central_widget)

    def dragEnterEvent(self, event):
        """Accept file drags if they contain URLs (file paths)."""
        print("dragEnterEvent on main window")
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self, event):
        """Handle the actual drop."""
        print("dropEvent on main window")
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                self.on_file_dropped(file_path)
            event.acceptProposedAction()
        else:
            super().dropEvent(event)

    def on_file_dropped(self, file_path):
        print("Dropped file:", file_path)

        # Create Worker
        self.worker = GenPaperWorker(self.m_GenManager, file_path)
        self.thread = QThread()

        # Move worker to that thread
        self.worker.moveToThread(self.thread)

        # Thread starts => call worker.run
        self.thread.started.connect(self.worker.run)

        # Worker finishes => clean up
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(lambda: self.browser.page().runJavaScript("setOrbitSpeed(0.03);"))

        # Go!
        self.thread.start()

        self.browser.page().runJavaScript("setOrbitSpeed(0.1);")