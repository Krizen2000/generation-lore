from PySide6.QtWidgets import *


class Title_View(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.load_widgets()
        self.set_layout()

    def load_widgets(self):
        self.title_bar = QPushButton(parent=self)
        self.title_bar.setMouseTracking(True)
        self.title_bar.setObjectName("title_bar")
        self.app_name = QLabel(parent=self,text="GenLore")
        self.app_name_left_spacer = QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Minimum)
        self.app_name_right_spacer = QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Minimum)

        self.minimize_btn = QPushButton(parent=self)
        self.maximize_btn = QPushButton(parent=self)
        self.exit_btn = QPushButton(parent=self)
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(lambda: self.mapToGlobal(QPoint(500,500)))
        # self.exit_btn.click
        self.exit_btn.clicked.connect(lambda: print("Button clicked"))

    def set_layout(self):
        main_layout = QVBoxLayout()

        main_layout.addItem(self.app_name_left_spacer)
        main_layout.addWidget(self.app_name)
        main_layout.addItem(self.app_name_right_spacer)
        main_layout.addWidget(self.minimize_btn)
        main_layout.addWidget(self.maximize_btn)
        main_layout.addWidget(self.exit_btn)


if __name__ == "__main__":
    app = QApplication()
    tb = Title_View()
    tb.show()
    app.exec()