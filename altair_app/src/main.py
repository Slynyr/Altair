from PyQt6.QtWidgets import QApplication
from backend.threejs_app import ThreeJsApp
from dotenv import load_dotenv
import sys

load_dotenv()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThreeJsApp()
    window.show()
    sys.exit(app.exec())

    
