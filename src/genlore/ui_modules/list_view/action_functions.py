from src.genlore.ui_modules.list_view.ui_application_panel import Ui_List_View_Application_Panel
from src.genlore.modules.db_module.db_module import Db_Module

from PySide6.QtWidgets import *
from PySide6.QtGui import *


def load_qlist_items(cls: Ui_List_View_Application_Panel):
    db_context = Db_Module.get_instance()
    story_entries = db_context.get_all_entries("STORY")
    summary_entries = db_context.get_all_entries("SUMMARY")

    # Remove old items except creation item
    for index in range(cls.story_container.count()):
        item_text = cls.story_container.item(index).text()
        if item_text == "New Story":
            continue
        cls.story_container.takeItem(index)
    for index in range(cls.summary_container.count()):
        item_text = cls.summary_container.item(index).text()
        if item_text == "New Summary":
            continue
        cls.story_container.takeItem(index)

    file_icon = QPixmap("icons/file.svg")
    mask = file_icon.createMaskFromColor(QColor("transparent"), Qt.MaskInColor)
    file_icon.fill(QColor("#FE5D9F"))
    file_icon.setMask(mask)
    print(f"[Story_Entries]: {story_entries}")
    print(f"[Summary_Entries]: {summary_entries}")

    for story_entry in story_entries:
        story_item = QListWidgetItem(file_icon, story_entry[0])
        cls.story_container.addItem(story_item)

    for summary_entry in summary_entries:
        summary_item = QListWidgetItem(file_icon, summary_entry[0])
        cls.summary_container.addItem(summary_item)


def on_click_container(item: QListWidgetItem, container, on_focus_doc_gen_view, on_focus_doc_obs_view):
    item_text = item.text()
    print(f"[Container Name]: {container}")
    if item_text == f"New {container}":
        on_focus_doc_gen_view(container.lower())
        return
    # Make a function in Doc_obs_view where it takes the var while focusing
    on_focus_doc_obs_view(item_text, container)
