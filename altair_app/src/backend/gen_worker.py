from PyQt6.QtCore import QObject, pyqtSignal

class GenPaperWorker(QObject):
        finished = pyqtSignal()
        error = pyqtSignal(str)

        def __init__(self, gen_manager, file_path):
            super().__init__()
            self.gen_manager = gen_manager
            self.file_path = file_path

        def run(self):
            try:
                self.gen_manager.gen_paper(self.file_path)
            except Exception as e:
                #TODO HANDLE
                self.error.emit(str(e))
            finally:
                self.finished.emit()