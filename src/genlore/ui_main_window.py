from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Ui_Main_Window")
        # self.setMinimumSize(750,500)
        self.setMinimumSize(950, 700)
        self.load_widget()
        self.set_layout()

        self.setWindowFlags(
            Qt.FramelessWindowHint
        )

    def load_widget(self):
        self.main_widget = QWidget(parent=self)
        self.action_panel = QStackedWidget(parent=self)
        self.action_panel.setFixedWidth(150)
        self.application_panel = QStackedWidget(parent=self)

    def set_layout(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.action_panel)
        self.main_layout.addWidget(self.application_panel)

        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
