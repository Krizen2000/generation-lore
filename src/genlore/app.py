from PySide6.QtGui import *
from PySide6.QtWidgets import *

from src.genlore.main_window import Main_Window

class app:
    def __init__(self):
        self.app_instance = QApplication()
        self.main_window = Main_Window(self.app_instance)

    def exec(self):
        self.main_window.show()
        self.app_instance.exec()