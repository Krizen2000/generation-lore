from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Ui_List_View_Action_Panel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Ui_List_All_View_Action_Panel")
        self.load_widgets()
        self.set_layout()
        self.load_widget_assets()

        with open("src/genlore/ui_modules/list_view/ui_action_panel.qss", "r") as qss_file:
            self.setStyleSheet(qss_file.read())

    def load_widgets(self):
        self.logo = QLabel(parent=self)

        self.logo_sep = QFrame(parent=self)

        self.recent_view_btn = QPushButton(parent=self, text="Recents")
        self.favourite_view_btn = QPushButton(parent=self, text="Favourites")
        self.list_view_btn = QPushButton(parent=self, text="List all")
        self.list_view_btn.setObjectName("list_all_view_btn")

        self.view_sep = QFrame(parent=self)

        self.share_btn = QPushButton(parent=self, text="Share")

        self.action_button_spacer = QSpacerItem(
            0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.help_view_btn = QPushButton(parent=self, text="Help")
        self.info_view_btn = QPushButton(parent=self, text="Info")
        self.setting_view_btn = QPushButton(parent=self, text="Settings")

    def set_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.logo)

        main_layout.addWidget(self.logo_sep)

        main_layout.addWidget(self.recent_view_btn)
        main_layout.addWidget(self.favourite_view_btn)
        main_layout.addWidget(self.list_view_btn)

        main_layout.addWidget(self.view_sep)

        main_layout.addWidget(self.share_btn)

        main_layout.addItem(self.action_button_spacer)

        main_layout.addWidget(self.help_view_btn)
        main_layout.addWidget(self.info_view_btn)
        main_layout.addWidget(self.setting_view_btn)

        self.setLayout(main_layout)

    def load_widget_assets(self):
        logo_icon = QPixmap("icons/logo.svg")
        mask = logo_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        logo_icon.fill(QColor("#FE5D9F"))
        logo_icon.setMask(mask)
        # self.logo.setPixmap(logo_icon.scaled(
        # self.logo.width(), self.height(), Qt.KeepAspectRatio))
        self.logo.setPixmap(logo_icon.scaled(
            60, 60, Qt.AspectRatioMode.KeepAspectRatio))
        self.logo.setAlignment(Qt.AlignHCenter)

        self.logo_sep.setFrameShape(QFrame.HLine)

        recent_view_icon = QPixmap("icons/rotate-left.svg")
        mask = recent_view_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        recent_view_icon.fill(QColor("#FE5D9F"))
        recent_view_icon.setMask(mask)
        self.recent_view_btn.setIcon(recent_view_icon)

        favourite_view_icon = QPixmap("icons/star.svg")
        mask = favourite_view_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        favourite_view_icon.fill(QColor("#FE5D9F"))
        favourite_view_icon.setMask(mask)
        self.favourite_view_btn.setIcon(favourite_view_icon)

        list_view_icon = QPixmap("icons/list.svg")
        mask = list_view_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        list_view_icon.fill(QColor("#F3F3F3"))
        list_view_icon.setMask(mask)
        self.list_view_btn.setIcon(list_view_icon)

        self.view_sep.setFrameShape(QFrame.HLine)

        share_icon = QPixmap("icons/share-nodes.svg")
        mask = share_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        share_icon.fill(QColor("#FE5D9F"))
        share_icon.setMask(mask)
        self.share_btn.setIcon(share_icon)

        help_view_icon = QPixmap("icons/question.svg")
        mask = help_view_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        help_view_icon.fill(QColor("#FE5D9F"))
        help_view_icon.setMask(mask)
        self.help_view_btn.setIcon(help_view_icon)

        info_view_icon = QPixmap("icons/info.svg")
        mask = info_view_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        info_view_icon.fill(QColor("#FE5D9F"))
        info_view_icon.setMask(mask)
        self.info_view_btn.setIcon(info_view_icon)

        setting_view_icon = QPixmap("icons/gear.svg")
        mask = setting_view_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        setting_view_icon.fill(QColor("#FE5D9F"))
        setting_view_icon.setMask(mask)
        self.setting_view_btn.setIcon(setting_view_icon)

        pass


if __name__ == "__main__":
    app = QApplication()
    window = Ui_List_View_Action_Panel()
    window.show()
    app.exec()
