from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Ui_Doc_Obs_View_Application_Panel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.prev_coords = None
        self.full_screened = False
        self.setObjectName("Ui_Doc_Obs_View_Application_Panel")
        self.load_widgets()
        self.set_layout()
        self.load_widget_assets()

        with open("src/genlore/ui_modules/doc_obs_view/ui_application_panel.qss", "r") as qss_file:
            self.setStyleSheet(qss_file.read())

    def load_widgets(self):
        self.title_bar = QWidget(parent=self)
        self.title_bar.setObjectName("title_bar")
        self.back_btn = QPushButton(parent=self)
        self.back_btn.setObjectName("back_btn")
        self.back_btn_spacer = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.file_name = QLabel(parent=self, text="File_Name")
        self.file_name_spacer = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.minimize_btn = QPushButton(parent=self)
        self.minimize_btn.setObjectName("minimize_btn")
        self.maximize_btn = QPushButton(parent=self)
        self.maximize_btn.setObjectName("maximize_btn")
        self.exit_btn = QPushButton(parent=self)
        self.exit_btn.setObjectName("exit_btn")
        self.title_bar_sep = QFrame(parent=self)

        self.file_content = QPlainTextEdit(parent=self)

        # Panel Layout Elements

        self.doc_head = QWidget(parent=self)
        self.doc_label = QLabel(parent=self, text="Doc Preview")
        self.doc_icon = QLabel(parent=self)

        self.doc_head_sep = QFrame(parent=self)

        self.file_icon = QLabel(parent=self)
        self.file_icon_sep = QFrame(parent=self)

        self.file_word_count_label = QLabel(parent=self, text="Word Count: ")
        self.file_sentence_count_label = QLabel(
            parent=self, text="Sentence Count: ")

        self.file_time_created_label = QLabel(
            parent=self, text="Time Created: ")
        self.file_time_created = QLabel(parent=self)

        self.file_date_created_label = QLabel(
            parent=self, text="Date Created: ")
        self.file_date_created = QLabel(parent=self)

        self.file_time_modified_label = QLabel(
            parent=self, text="Time Modified: ")
        self.file_time_modified = QLabel(parent=self)

        self.file_date_modified_label = QLabel(
            parent=self, text="Date Modified: ")
        self.file_date_modified = QLabel(parent=self)

        self.file_word_count = QLabel(parent=self)
        self.file_sentence_count = QLabel(parent=self)
        self.file_date_created = QLabel(parent=self)
        self.file_date_modified = QLabel(parent=self)

        self.file_spacer = QSpacerItem(
            0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

    def set_layout(self):
        main_layout = QHBoxLayout()
        self.doc_layout = QVBoxLayout()
        self.doc_layout.setObjectName("doc_layout")

        layout = QHBoxLayout()
        layout.addWidget(self.back_btn)
        layout.addItem(self.back_btn_spacer)
        layout.addWidget(self.file_name)
        layout.addItem(self.file_name_spacer)
        layout.addWidget(self.minimize_btn)
        layout.addWidget(self.maximize_btn)
        layout.addWidget(self.exit_btn)
        self.title_bar.setLayout(layout)
        self.doc_layout.addWidget(self.title_bar)
        self.doc_layout.addWidget(self.title_bar_sep)

        self.doc_layout.addWidget(self.file_content)

        self.panel_layout = QVBoxLayout()
        self.panel_layout.setObjectName("panel_layout")

        layout = QHBoxLayout()
        layout.addWidget(self.doc_icon)
        layout.addWidget(self.doc_label)
        self.doc_head.setLayout(layout)
        self.panel_layout.addWidget(self.doc_head)

        self.panel_layout.addWidget(self.doc_head_sep)

        self.panel_layout.addWidget(self.file_icon)
        self.panel_layout.addWidget(self.file_icon_sep)

        layout = QHBoxLayout()
        layout.addWidget(self.file_word_count_label)
        layout.addWidget(self.file_word_count)
        self.panel_layout.addLayout(layout)
        layout = QHBoxLayout()
        layout.addWidget(self.file_sentence_count_label)
        layout.addWidget(self.file_sentence_count)
        self.panel_layout.addLayout(layout)

        layout = QHBoxLayout()
        layout.addWidget(self.file_time_created_label)
        layout.addWidget(self.file_time_created)
        self.panel_layout.addLayout(layout)

        layout = QHBoxLayout()
        layout.addWidget(self.file_date_created_label)
        layout.addWidget(self.file_date_created)
        self.panel_layout.addLayout(layout)

        layout = QHBoxLayout()
        layout.addWidget(self.file_time_modified_label)
        layout.addWidget(self.file_time_modified)
        self.panel_layout.addLayout(layout)

        layout = QHBoxLayout()
        layout.addWidget(self.file_date_modified_label)
        layout.addWidget(self.file_date_modified)
        self.panel_layout.addLayout(layout)
        self.panel_layout.addItem(self.file_spacer)

        main_layout.addLayout(self.doc_layout)
        main_layout.addLayout(self.panel_layout)

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

        doc_icon = QPixmap("icons/file.svg")
        doc_icon = doc_icon.scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio)
        mask = doc_icon.createMaskFromColor(QColor("black"), Qt.MaskOutColor)
        doc_icon.fill(QColor("#FE5D9F"))
        doc_icon.setMask(mask)
        self.doc_icon.setPixmap(doc_icon)
        self.doc_head_sep.setFrameShape(QFrame.HLine)

        file_icon = QPixmap("icons/file.svg")
        file_icon = file_icon.scaled(
            50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        mask = file_icon.createMaskFromColor(QColor("black"), Qt.MaskOutColor)
        file_icon.fill(QColor("#FE5D9F"))
        file_icon.setMask(mask)
        self.file_icon.setPixmap(file_icon)
        self.file_icon.setAlignment(Qt.AlignHCenter)
        self.file_icon_sep.setFrameShape(QFrame.HLine)

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
    window = Ui_Doc_Obs_View_Application_Panel()
    window.show()
    app.exec()
