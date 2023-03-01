from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Ui_Doc_Gen_View_Application_Panel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.prev_coords = None
        self.full_screened = False
        self.setObjectName("Ui_Doc_Gen_View_Application_Panel")
        self.load_widgets()
        self.set_layout()
        self.load_widget_assets()

        with open("src/genlore/ui_modules/doc_gen_view/ui_application_panel.qss", "r") as qss_file:
            self.setStyleSheet(qss_file.read())

    def load_widgets(self):
        self.title_bar = QWidget(parent=self)
        self.title_bar.setObjectName("title_bar")
        self.back_btn = QPushButton(parent=self)
        self.back_btn.setObjectName("back_btn")
        self.back_btn_spacer = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.file_name = QLabel(parent=self, text="Story/Summary Generation")
        self.file_name_spacer = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.minimize_btn = QPushButton(parent=self)
        self.minimize_btn.setObjectName("minimize_btn")
        self.maximize_btn = QPushButton(parent=self)
        self.maximize_btn.setObjectName("maximize_btn")
        self.exit_btn = QPushButton(parent=self)
        self.exit_btn.setObjectName("exit_btn")
        self.title_bar_sep = QFrame(parent=self)

        # self.action_label = QLabel(parent=self,text="Story/Summary Generation")
        # self.input_box = QPlainTextEdit(parent=self)
        self.text_title = QLabel(parent=self, text="Title:")
        self.text_title_input = QLineEdit(parent=self)
        self.user_input = QLabel(parent=self, text="Initial Lines/Context:")
        self.user_input_box = QPlainTextEdit(parent=self)
        self.generate_btn = QPushButton(parent=self, text="Generate")
        self.generate_btn.setObjectName("generate_btn")
        self.generate_btn_lspacer = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.generate_btn_rspacer = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        # self.output_box = QPlainTextEdit(parent=self)

    def set_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 5, 0, 0)
        doc_layout = QVBoxLayout()

        layout = QHBoxLayout()
        layout.addWidget(self.back_btn)
        layout.addSpacerItem(self.back_btn_spacer)
        layout.addWidget(self.file_name)
        layout.addSpacerItem(self.file_name_spacer)
        layout.addWidget(self.minimize_btn)
        layout.addWidget(self.maximize_btn)
        layout.addWidget(self.exit_btn)
        layout.setContentsMargins(11, 5, 11, 5)
        self.title_bar.setLayout(layout)
        main_layout.addWidget(self.title_bar)

        main_layout.addWidget(self.title_bar_sep)

        # doc_layout.addWidget(self.action_label)
        # doc_layout.addWidget(self.input_box)
        inner_layout = QHBoxLayout()
        inner_layout.addWidget(self.text_title)
        inner_layout.addWidget(self.text_title_input)
        doc_layout.addLayout(inner_layout)
        doc_layout.addWidget(self.user_input)
        doc_layout.addWidget(self.user_input_box)
        inner_layout = QHBoxLayout()
        inner_layout.addSpacerItem(self.generate_btn_lspacer)
        inner_layout.addWidget(self.generate_btn)
        inner_layout.addSpacerItem(self.generate_btn_rspacer)
        doc_layout.addLayout(inner_layout)
        # doc_layout.addWidget(self.generate_btn)
        # doc_layout.addWidget(self.output_box)
        doc_layout.setContentsMargins(11, 11, 11, 11)

        # ? Can make a Result layout Horizontally mounted here

        main_layout.addLayout(doc_layout)
        self.setLayout(main_layout)

    def eventFilter(self, watched, event: QMouseEvent) -> bool:
        if event.type() == QEvent.MouseButtonPress:
            print("[Mouse Pressed]")
            self.prev_coords = event.scenePosition().toPoint()

        if self.prev_coords is not None:
            if event.type() == QEvent.MouseButtonRelease:
                print("[Mouse Release]")
                self.prev_coords = None
            elif event.type() == QEvent.MouseMove:
                print("[Mouse Move]")
                self.window().move(event.globalPosition().toPoint() - self.prev_coords)

        return super().eventFilter(watched, event)

    def load_widget_assets(self):
        back_icon = QIcon("icons/chevron-left.svg")
        self.back_btn.setIcon(back_icon)
        minimize_btn_icon = QPixmap("icons/window-minimize.svg")
        mask = minimize_btn_icon.createMaskFromColor(
            QColor("black"), Qt.MaskOutColor)
        minimize_btn_icon.fill(QColor("#FE5D9F"))
        minimize_btn_icon.setMask(mask)
        self.minimize_btn.setIcon(minimize_btn_icon)
        self.minimize_btn.setFixedSize(20, 20)
        maximize_btn_icon = QPixmap("icons/window-maximize.svg")
        mask = maximize_btn_icon.createMaskFromColor(
            QColor("black"), Qt.MaskOutColor)
        maximize_btn_icon.fill(QColor("#FE5D9F"))
        maximize_btn_icon.setMask(mask)
        self.maximize_btn.setIcon(maximize_btn_icon)
        self.maximize_btn.setFixedSize(20, 20)
        exit_btn_icon = QPixmap("icons/xmark.svg")
        mask = exit_btn_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        exit_btn_icon.fill(QColor("#E1E1E1"))
        exit_btn_icon.setMask(mask)
        self.exit_btn.setIcon(exit_btn_icon)
        self.exit_btn.setFixedSize(20, 20)
        self.title_bar_sep.setFrameShape(QFrame.HLine)

        self.title_bar.installEventFilter(self)
        self.minimize_btn.clicked.connect(
            lambda: self.window().showMinimized())

        def change_window_state():
            if self.full_screened:
                self.window().showNormal()
                self.full_screened = False
            else:
                self.window().showMaximized()
                self.full_screened = True

        self.maximize_btn.clicked.connect(lambda: change_window_state())
        self.exit_btn.clicked.connect(lambda: self.window().close())


if __name__ == "__main__":
    app = QApplication()
    window = Ui_Doc_Gen_View_Application_Panel()
    window.show()
    app.exec()
