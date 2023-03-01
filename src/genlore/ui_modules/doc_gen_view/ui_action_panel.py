from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Ui_Doc_Gen_View_Action_Panel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Ui_Doc_Gen_View_Action_Panel")
        self.load_widgets()
        self.set_layout()
        self.load_widget_assets()

        with open("src/genlore/ui_modules/doc_gen_view/ui_action_panel.qss", "r") as qss_file:
            self.setStyleSheet(qss_file.read())

    def load_widgets(self):
        self.logo = QLabel(parent=self)
        self.logo_sep = QFrame(parent=self)

        self.recent_view_btn = QPushButton(parent=self, text="Recents")
        self.favourite_view_btn = QPushButton(parent=self, text="Favourites")
        self.list_view_btn = QPushButton(parent=self, text="List all")

        self.view_sep = QFrame(parent=self)

        # self.save_btn = QPushButton(parent=self,text="Save")
        # self.clipboard_btn = QPushButton(parent=self,text="Copy")
        # self.add_favourite_btn = QPushButton(parent=self,text="Add Favourite")
        # self.share_btn = QPushButton(parent=self,text="Share")
#
        # self.back_btn = QPushButton(parent=self,text="Back")

        self.vertical_spacer = QSpacerItem(
            0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.setting_btn = QPushButton(parent=self, text="Settings")

    def set_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.logo)
        main_layout.addWidget(self.logo_sep)

        main_layout.addWidget(self.recent_view_btn)
        main_layout.addWidget(self.favourite_view_btn)
        main_layout.addWidget(self.list_view_btn)

        main_layout.addWidget(self.view_sep)

        # main_layout.addWidget(self.save_btn)
        # main_layout.addWidget(self.clipboard_btn)
        # main_layout.addWidget(self.add_favourite_btn)
        # main_layout.addWidget(self.share_btn)
        # main_layout.addWidget(self.back_btn)

        main_layout.addItem(self.vertical_spacer)

        main_layout.addWidget(self.setting_btn)
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
        list_view_icon.fill(QColor("#FE5D9F"))
        list_view_icon.setMask(mask)
        self.list_view_btn.setIcon(list_view_icon)

        self.view_sep.setFrameShape(QFrame.HLine)

        # save_icon = QPixmap("icons/floppy-disk.svg")
        # mask = save_icon.createMaskFromColor(QColor("transparent"),Qt.MaskInColor)
        # save_icon.fill(QColor("#A5C9CA"))
        # save_icon.setMask(mask)
        # self.save_btn.setIcon(save_icon)
#
        # clipboard_icon = QPixmap("icons/clipboard.svg")
        # mask = clipboard_icon.createMaskFromColor(QColor("transparent"),Qt.MaskInColor)
        # clipboard_icon.fill(QColor("#A5C9CA"))
        # clipboard_icon.setMask(mask)
        # self.clipboard_btn.setIcon(clipboard_icon)
#
        # favourite_icon = QPixmap("icons/star.svg")
        # mask = favourite_icon.createMaskFromColor(QColor("transparent"),Qt.MaskInColor)
        # favourite_icon.fill(QColor("#A5C9CA"))
        # favourite_icon.setMask(mask)
        # self.add_favourite_btn.setIcon(favourite_icon)
#
        # share_icon = QPixmap("icons/share-nodes.svg")
        # mask = share_icon.createMaskFromColor(QColor("transparent"),Qt.MaskInColor)
        # share_icon.fill(QColor("#A5C9CA"))
        # share_icon.setMask(mask)
        # self.share_btn.setIcon(share_icon)
#
        # back_icon = QPixmap("icons/chevron-left.svg")
        # mask = back_icon.createMaskFromColor(QColor("transparent"),Qt.MaskInColor)
        # back_icon.fill(QColor("#A5C9CA"))
        # back_icon.setMask(mask)
        # self.back_btn.setIcon(back_icon)

        setting_icon = QPixmap("icons/gear.svg")
        mask = setting_icon.createMaskFromColor(
            QColor("transparent"), Qt.MaskInColor)
        setting_icon.fill(QColor("#FE5D9F"))
        setting_icon.setMask(mask)
        self.setting_btn.setIcon(setting_icon)


if __name__ == "__main__":
    app = QApplication()
    window = Ui_Doc_Gen_View_Action_Panel()
    window.show()
    app.exec()
