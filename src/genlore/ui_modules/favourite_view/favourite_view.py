from src.genlore.ui_modules.favourite_view.ui_action_panel import Ui_Favourite_View_Action_Panel
from src.genlore.ui_modules.favourite_view.ui_application_panel import Ui_Favourite_View_Application_Panel
from src.genlore.ui_modules.favourite_view.action_functions import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Favourite_View:
    def __init__(self,action_panel: QStackedWidget,application_panel: QStackedWidget):
        self.action_panel = action_panel
        self.application_panel = application_panel
        self.load_favourite_view_ui()
    
    def load_favourite_view_ui(self):
        self.ui_action_panel = Ui_Favourite_View_Action_Panel(self.action_panel)
        self.ui_application_panel = Ui_Favourite_View_Application_Panel(self.application_panel)

        self.action_panel.addWidget(self.ui_action_panel)
        self.application_panel.addWidget(self.ui_application_panel)

    def set_focus(self):
        self.action_panel.setCurrentWidget(self.ui_action_panel)
        self.application_panel.setCurrentWidget(self.ui_application_panel)

        load_qlist_items(self.ui_application_panel)

    def set_view_buttons(self,set_focus_recent_view,set_focus_list_view):
        self.ui_action_panel.recent_view_btn.clicked.connect(lambda: set_focus_recent_view())
        self.ui_action_panel.list_view_btn.clicked.connect(lambda: set_focus_list_view())

    def set_action_buttons(self,set_focus_doc_gen_view,set_focus_doc_obs_view):
        container_func = lambda item, container: on_click_container(
            item,
            container,
            set_focus_doc_gen_view,
            set_focus_doc_obs_view,
        )
        self.ui_application_panel.story_container.itemClicked.connect(lambda item: container_func(item,"Story"))
        self.ui_application_panel.summary_container.itemClicked.connect(lambda item: container_func(item,"Summary"))