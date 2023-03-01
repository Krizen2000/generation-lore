from src.genlore.ui_main_window import Ui_Main_Window
from src.genlore.ui_modules.recent_view.recent_view import Recent_View
from src.genlore.ui_modules.favourite_view.favourite_view import Favourite_View
from src.genlore.ui_modules.list_view.list_view import List_View
from src.genlore.ui_modules.doc_gen_view.doc_gen_view import Doc_Gen_View
from src.genlore.ui_modules.doc_obs_view.doc_obs_view import Doc_Obs_View

from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Main_Window(Ui_Main_Window):
    def __init__(self,app_instance: QApplication):
        super().__init__()
        self.app_instance = app_instance
        self.action_panel.setObjectName("action_panel")
        self.application_panel.setObjectName("application_panel")
        self.load_ui_modules()
        self.connect_modules()

        with open("src/genlore/ui_main_window.qss","r") as qss_file:
            self.setStyleSheet(qss_file.read())

        self.recent_view.set_focus()

    def load_ui_modules(self):
        self.recent_view = Recent_View(self.action_panel,self.application_panel)
        self.favourite_view = Favourite_View(self.action_panel,self.application_panel)
        self.list_view = List_View(self.action_panel,self.application_panel)
        self.doc_gen_view = Doc_Gen_View(self.action_panel,self.application_panel)
        self.doc_obs_view = Doc_Obs_View(self.action_panel,self.application_panel)

    def connect_modules(self):
        self.recent_view.set_view_buttons(self.favourite_view.set_focus,self.list_view.set_focus)
        self.recent_view.set_action_buttons(
            lambda mode: self.doc_gen_view.set_focus(mode,self.recent_view.set_focus),
            lambda entry_name, entry_table: self.doc_obs_view.set_focus(entry_name,entry_table,self.recent_view.set_focus)
        )

        self.favourite_view.set_view_buttons(self.recent_view.set_focus,self.list_view.set_focus)
        self.favourite_view.set_action_buttons(
            lambda mode: self.doc_gen_view.set_focus(mode,self.recent_view.set_focus),
            lambda entry_name, entry_table: self.doc_obs_view.set_focus(entry_name,entry_table,self.recent_view.set_focus)
        )
        
        self.list_view.set_view_buttons(self.recent_view.set_focus,self.favourite_view.set_focus)
        self.list_view.set_action_buttons(
            lambda mode: self.doc_gen_view.set_focus(mode,self.recent_view.set_focus),
            lambda entry_name, entry_table: self.doc_obs_view.set_focus(entry_name,entry_table,self.recent_view.set_focus)
        )

        self.doc_gen_view.set_view_buttons(
            self.recent_view.set_focus,
            self.favourite_view.set_focus,
            self.list_view.set_focus,
        )
        self.doc_gen_view.set_action_buttons(
            (lambda txt: self.app_instance.clipboard().setText(txt)),
            (lambda mime_data: self.app_instance.clipboard().setMimeData(mime_data)),
            self.doc_obs_view.set_focus
        )

        self.doc_obs_view.set_view_buttons(
            self.recent_view.set_focus,
            self.favourite_view.set_focus,
            self.list_view.set_focus,
        )

        self.doc_obs_view.set_action_buttons(
            (lambda txt: self.app_instance.clipboard().setText(txt)),
            (lambda mime_data: self.app_instance.clipboard().setMimeData(mime_data))
        )