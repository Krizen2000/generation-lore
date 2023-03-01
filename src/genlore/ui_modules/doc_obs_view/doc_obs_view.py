from src.genlore.modules.db_module.db_module import Db_Module
from src.genlore.ui_modules.doc_obs_view.ui_action_panel import Ui_Doc_Obs_View_Action_Panel
from src.genlore.ui_modules.doc_obs_view.ui_application_panel import Ui_Doc_Obs_View_Application_Panel
from src.genlore.ui_modules.doc_obs_view.action_functions import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import datetime


class Doc_Obs_View:
    def __init__(self, action_panel: QStackedWidget, application_panel: QStackedWidget):
        self.prev_view_callback = None
        self.table_name = str()
        self.action_panel = action_panel
        self.application_panel = application_panel
        self.load_doc_obs_view_ui()

    def load_doc_obs_view_ui(self):
        self.ui_action_panel = Ui_Doc_Obs_View_Action_Panel(self.action_panel)
        self.ui_application_panel = Ui_Doc_Obs_View_Application_Panel(
            self.application_panel)

        self.action_panel.addWidget(self.ui_action_panel)
        self.application_panel.addWidget(self.ui_application_panel)

    def set_focus(self, entry_name, entry_table, prev_view_callback):
        db_context = Db_Module.get_instance()
        if not db_context.exists(entry_name, entry_table.upper()):
            msgbox = QMessageBox(
                QMessageBox.Icon.Critical,
                "No Entry",
                "No such entry exists in the database!",
                QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Close,
                parent=self.ui_application_panel
            )
            msgbox.show()
            return

        if self.prev_view_callback is not None:
            self.ui_application_panel.back_btn.clicked.disconnect(
                self.prev_view_callback)
        self.prev_view_callback = prev_view_callback
        self.ui_application_panel.back_btn.clicked.connect(
            self.prev_view_callback)

        self.table_name = entry_table
        self.action_panel.setCurrentWidget(self.ui_action_panel)
        self.application_panel.setCurrentWidget(self.ui_application_panel)

        entry = db_context.load_entry(entry_name, entry_table.upper())
        print(f"[entry]: {entry}")
        is_favourite: bool = entry[1]
        content: str = entry[2]
        date_created: datetime.datetime = entry[3]  # 3
        date_modified: datetime.datetime = entry[4]  # 4

        word_count = str(len(content.split()))
        sentence_count = str(len(content.split(".")))

        print(f"[Content]: {content}")
        if is_favourite:
            self.ui_action_panel.add_favourite_btn.setText("Remove Favourite")
        else:
            self.ui_action_panel.add_favourite_btn.setText("Add Favourite")

        self.ui_application_panel.file_content.clear()
        self.ui_application_panel.file_name.setText(entry_name)
        self.ui_application_panel.file_content.setPlainText(content)

        self.ui_application_panel.file_word_count.setText(word_count)
        self.ui_application_panel.file_sentence_count.setText(sentence_count)

        self.ui_application_panel.file_time_modified.setText(
            str(date_modified.time().isoformat("minutes")))
        self.ui_application_panel.file_date_modified.setText(
            str(date_modified.date()))
        self.ui_application_panel.file_time_created.setText(
            str(date_created.time().isoformat("minutes")))
        self.ui_application_panel.file_date_created.setText(
            str(date_created.date()))

    def set_view_buttons(self, set_focus_recent_view, set_focus_favourite_view, set_focus_list_view):
        self.ui_action_panel.recent_view_btn.clicked.connect(
            lambda: set_focus_recent_view())
        self.ui_action_panel.favourite_view_btn.clicked.connect(
            lambda: set_focus_favourite_view())
        self.ui_action_panel.list_view_btn.clicked.connect(
            lambda: set_focus_list_view())

    def set_action_buttons(self, set_clipboard_content, set_clipboard_mime_data):
        self.ui_action_panel.save_btn.clicked.connect(
            lambda: on_click_save_btn(self.ui_application_panel))
        self.ui_action_panel.clipboard_btn.clicked.connect(lambda: on_click_clipboard_btn(
            self.table_name, set_clipboard_content, self.ui_application_panel))
        self.ui_action_panel.share_btn.clicked.connect(lambda: on_click_share_btn(
            self.table_name, set_clipboard_mime_data, self.ui_application_panel))
        self.ui_action_panel.add_favourite_btn.clicked.connect(
            lambda: on_click_add_favourite_btn(self.table_name, self.ui_application_panel))
