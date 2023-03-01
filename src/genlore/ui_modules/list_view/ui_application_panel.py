from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Ui_List_View_Application_Panel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.prev_coords = None
        self.full_screened = False
        self.setObjectName("Ui_List_All_View_Application_Panel")
        self.load_widgets()
        self.set_layout()
        self.load_widget_assets()

        with open("src/genlore/ui_modules/list_view/ui_application_panel.qss", "r") as qss_file:
            self.setStyleSheet(qss_file.read())

    def load_widgets(self):
        self.title_bar = QWidget(parent=self)
        self.title_bar.setObjectName("title_bar")
        self.app_name = QLabel(parent=self, text="GenLore")
        self.app_name_left_spacer = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.app_name_right_spacer = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.minimize_btn = QPushButton(parent=self)
        self.minimize_btn.setObjectName("minimize_btn")
        self.maximize_btn = QPushButton(parent=self)
        self.maximize_btn.setObjectName("maximize_btn")
        self.exit_btn = QPushButton(parent=self)
        self.exit_btn.setObjectName("exit_btn")

        self.title_bar_sep = QFrame(parent=self)
        self.title_bar_sep.setFrameShape(QFrame.HLine)

        self.view_name = QLabel(parent=self, text="List All")
        self.view_name.setObjectName("view_name")
        self.view_name_sep = QFrame(parent=self)
        self.view_name_sep.setFrameShape(QFrame.HLine)

        # Can't be ported to set_ui_theme
        self.search_icon = QPixmap("icons/magnifying-glass.svg")
        mask = self.search_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        self.search_icon.fill(QColor("#FE5D9F"))
        self.search_icon.setMask(mask)
        self.story_label = QLabel(parent=self, text="Stories")
        self.story_search_bar = QLineEdit(parent=self)
        self.story_search_bar.addAction(
            self.search_icon, QLineEdit.LeadingPosition)
        self.story_search_bar_spacer = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.story_container = QListWidget(parent=self)
        self.story_container.setViewMode(QListWidget.ViewMode.IconMode)

        # Can't be ported to set_ui_theme
        new_doc_icon = QPixmap("icons/file-circle-plus.svg")
        mask = new_doc_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        new_doc_icon.fill(QColor("#FE5D9F"))
        new_doc_icon.setMask(mask)
        QListWidgetItem(new_doc_icon, "New Story", self.story_container)

        self.summary_label = QLabel(parent=self, text="Summaries")
        self.summary_search_bar = QLineEdit(parent=self)
        self.summary_search_bar.addAction(
            self.search_icon, QLineEdit.LeadingPosition)
        self.summary_search_bar_spacer = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.summary_container = QListWidget(parent=self)
        self.summary_container.setViewMode(QListWidget.ViewMode.IconMode)

        QListWidgetItem(new_doc_icon, "New Summary", self.summary_container)

    def set_layout(self):
        main_layout = QVBoxLayout()
        sec_layout = QVBoxLayout()

        layout = QHBoxLayout()
        layout.addItem(self.app_name_left_spacer)
        layout.addWidget(self.app_name)
        layout.addItem(self.app_name_right_spacer)
        layout.addWidget(self.minimize_btn)
        layout.addWidget(self.maximize_btn)
        layout.addWidget(self.exit_btn)
        layout.setContentsMargins(11, 0, 11, 0)
        self.title_bar.setLayout(layout)
        main_layout.addWidget(self.title_bar)
        main_layout.addWidget(self.title_bar_sep)

        sec_layout.addWidget(self.view_name)
        sec_layout.addWidget(self.view_name_sep)
        sec_layout.addWidget(self.story_label)

        layout = QHBoxLayout()
        layout.addWidget(self.story_search_bar)
        layout.addItem(self.story_search_bar_spacer)
        sec_layout.addLayout(layout)

        sec_layout.addWidget(self.story_container)
        sec_layout.addWidget(self.summary_label)

        layout = QHBoxLayout()
        layout.addWidget(self.summary_search_bar)
        layout.addItem(self.summary_search_bar_spacer)
        sec_layout.addLayout(layout)

        sec_layout.addWidget(self.summary_container)

        main_layout.addLayout(sec_layout)
        sec_layout.setContentsMargins(11, 11, 11, 11)
        main_layout.setContentsMargins(0, 11, 0, 11)

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
    window = Ui_List_View_Application_Panel()
    window.show()
    app.exec()
