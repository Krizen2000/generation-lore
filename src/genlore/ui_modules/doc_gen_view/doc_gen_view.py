from src.genlore.ui_modules.doc_gen_view.ui_action_panel import Ui_Doc_Gen_View_Action_Panel
from src.genlore.ui_modules.doc_gen_view.ui_application_panel import Ui_Doc_Gen_View_Application_Panel
from src.genlore.ui_modules.doc_gen_view.action_functions import on_click_generate_btn
# from src.genlore.ui_modules.doc_gen_view.action_functions import on_click_clipboard_btn, on_click_generate_btn, on_click_save_btn, on_click_share_btn
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Doc_Gen_View:
    def __init__(self,action_panel: QStackedWidget,application_panel: QStackedWidget):
        self.prev_view_callback = None
        self.action_panel = action_panel
        self.application_panel = application_panel
        self.load_doc_gen_view_ui()
        # self.set_action_buttons()
    
    def load_doc_gen_view_ui(self):
        self.ui_action_panel = Ui_Doc_Gen_View_Action_Panel(self.action_panel)
        self.ui_application_panel = Ui_Doc_Gen_View_Application_Panel(self.application_panel)

        self.action_panel.addWidget(self.ui_action_panel)
        self.application_panel.addWidget(self.ui_application_panel)

    def set_focus(self,mode,prev_view_callback):
        if self.prev_view_callback is not None:
            self.ui_application_panel.back_btn.clicked.disconnect(self.prev_view_callback)
        self.prev_view_callback = prev_view_callback
        self.ui_application_panel.back_btn.clicked.connect(self.prev_view_callback)

        if mode == "story":
            self.ui_application_panel.file_name.setText("Story Generation")
        elif mode == "summary":
            self.ui_application_panel.file_name.setText("Summary Generation")

        self.action_panel.setCurrentWidget(self.ui_action_panel)
        self.application_panel.setCurrentWidget(self.ui_application_panel)
        self.mode = mode

    def set_view_buttons(self,set_focus_recent_view,set_focus_favourite_view,set_focus_list_view):
        self.set_focus_recent_view = set_focus_recent_view
        self.ui_action_panel.recent_view_btn.clicked.connect(lambda: set_focus_recent_view())
        self.ui_action_panel.recent_view_btn.clicked.connect(lambda: self.ui_application_panel.input_box.clear())
        self.ui_action_panel.recent_view_btn.clicked.connect(lambda: self.ui_application_panel.output_box.clear())
        self.ui_action_panel.favourite_view_btn.clicked.connect(lambda: set_focus_favourite_view())
        self.ui_action_panel.favourite_view_btn.clicked.connect(lambda: self.ui_application_panel.input_box.clear())
        self.ui_action_panel.favourite_view_btn.clicked.connect(lambda: self.ui_application_panel.output_box.clear())
        self.ui_action_panel.list_view_btn.clicked.connect(lambda: set_focus_list_view())
        self.ui_action_panel.list_view_btn.clicked.connect(lambda: self.ui_application_panel.input_box.clear())
        self.ui_action_panel.list_view_btn.clicked.connect(lambda: self.ui_application_panel.output_box.clear())
        # self.set_focus_doc_obs_view = set_focus_doc_obs_view

    def set_action_buttons(self,set_clipboard_content,set_clipboard_mime_data,set_focus_doc_obs_view):
        # self.ui_action_panel.save_btn.clicked.connect(lambda: on_click_save_btn(self.ui_application_panel,set_focus_doc_obs_view))
        # self.ui_action_panel.clipboard_btn.clicked.connect(lambda: on_click_clipboard_btn(set_clipboard_content,self.ui_application_panel))
        # self.ui_action_panel.share_btn.clicked.connect(lambda: on_click_share_btn(set_clipboard_mime_data,self.ui_application_panel))
        self.ui_application_panel.generate_btn.clicked.connect(
            lambda: on_click_generate_btn(self.ui_application_panel,set_focus_doc_obs_view,lambda: self.set_focus(self.mode,self.set_focus_recent_view))
        )

