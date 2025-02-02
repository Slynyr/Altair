from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView
from backend.gen_worker import GenPaperWorker
from backend.gen_manager import GenManager
from PyQt6.QtCore import pyqtSignal, QUrl, QThread, QUrl
import sys
import os
import json


class MyWebEnginePage(QWebEnginePage):
    # Signal to emit when a file icon is clicked.
    fileIconClicked = pyqtSignal(str)

    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if url.scheme() == 'open':
            # url.path() will return a string like "/0"
            index_str = url.path()[1:]  # Remove the leading slash
            print("File icon clicked, index:", index_str)
            self.fileIconClicked.emit(index_str)
            return False  # Prevent the navigation from occurring.
        return super().acceptNavigationRequest(url, _type, isMainFrame)

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
        self.setAcceptDrops(True)

        # Prepare the web view.
        self.browser = NoDragWebEngineView()
        page = MyWebEnginePage(self.browser)
        page.fileIconClicked.connect(self.handleFileIconClicked)
        self.browser.setPage(page)

        # Resolve base path
        if getattr(sys, 'frozen', False):  # Running as an .exe
            base_dir = sys._MEIPASS
        else:  # Running as a script
            base_dir = os.path.dirname(os.path.abspath(__file__))

        # Load index.html
        html_file = os.path.join(base_dir, "backend", "index.html")
        print(f"Loading HTML file from: {html_file}")

        # Load texture file and convert it into a proper `file://` URL
        texture_file = os.path.join(base_dir, "assets", "file-icon.png")
        texture_url = QUrl.fromLocalFile(texture_file).toString()

        print(f"Image Path: {texture_url}")  # Debugging check

        # Inject texture_url into the HTML via JavaScript
        self.browser.setUrl(QUrl.fromLocalFile(html_file))
        self.browser.loadFinished.connect(lambda: self.inject_image_url(texture_url))

        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.browser)
        self.setCentralWidget(central_widget)

    def inject_image_url(self, texture_url):
        """Inject the correct image path into JavaScript."""
        js_code = f"window.textureUrl = '{texture_url}';"
        print("Injecting image path:", js_code)  # Debugging check
        self.browser.page().runJavaScript(js_code)

    def handleFileIconClicked(self, index):
        print("Previewing Paper")
        self.m_GenManager.preview_paper(int(index))

    def dragEnterEvent(self, event):
        """Accept file drags if they contain URLs (file paths)."""
        print("dragEnterEvent on main window")
        print(self.m_GenManager.get_latest_index())
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

        # Create Worker (your existing code)
        self.worker = GenPaperWorker(self.m_GenManager, file_path)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # After the worker finishes, call JavaScript to add the file icon.
        # (Also adjust the orbit speed if desired.)
        self.worker.finished.connect(lambda: self.browser.page().runJavaScript("setOrbitSpeed(0.03);"))
        #self.worker.finished.connect(lambda: SoundHandler.ding())
        # Use json.dumps to properly encode the file_path string.
        self.worker.finished.connect(
            lambda: self.browser.page().runJavaScript(
                "addFileIcon(" + json.dumps(self.m_GenManager.get_latest_index()) + ");"
            )
        )

        self.thread.start()

        # Optionally, change the orbit speed while the file is processing.
        self.browser.page().runJavaScript("setOrbitSpeed(0.1);")