# This file contains functions used by the Class Doc_Gen_View
from src.genlore.ui_modules.doc_gen_view.ui_application_panel import Ui_Doc_Gen_View_Application_Panel
from src.genlore.modules.story_module.story_module import Story_Module
from src.genlore.modules.summary_module.summary_module import Summary_Module
from src.genlore.modules.db_module.db_module import Db_Module

from PySide6.QtWidgets import *
from PySide6.QtCore import *


def generate_unique_name(category="STORY"):
    db_context = Db_Module.get_instance()
    name = str("")
    for no in range(1, 1000):
        name = category.lower() + "_" + str(no)
        if not db_context.exists(name, category):
            return name


def on_click_generate_btn(cls: Ui_Doc_Gen_View_Application_Panel, set_focus_doc_obs_view, set_focus_doc_gen_view):
    print("[Clicked]:on_click_generate_btn")
    category = str("STORY")
    if cls.file_name.text() == "Summary Generation":
        category = "SUMMARY"
    if cls.file_name.text() == "Story Generation":
        category = "STORY"

    print(f"[text_title_input]: {cls.text_title_input.text()}")
    if (cls.text_title_input.text() is None) or (cls.text_title_input.text() == ""):
        name = generate_unique_name(category)
        print(f"[name]: {name}")
        cls.text_title_input.setText(name)

    # Check if name is unique
    db_context = Db_Module.get_instance()
    if db_context.exists(cls.text_title_input.text(), category):
        msgbox = QMessageBox.warning(
            cls, "Title already exist", "Please make sure you are using a unique name or leave the box empty to auto generate it", QMessageBox.StandardButton.Ok)
        return

    # ? Make some Loading View Here

    output_content = None
    # Stub for testing
    # if cls.file_name.text() == "Story Generation":
    # output_content = "This is a dummy paragraph."
    # elif cls.file_name.text() == "Summary Generation":
    # output_content = "This is a dummy summary."

    # Real Usage of Modules
    if cls.file_name.text() == "Story Generation":
        story_mod = Story_Module()
        input = cls.user_input_box.toPlainText()
        output_content = story_mod.generate_story(input)
    elif cls.file_name.text() == "Summary Generation":
        story_mod = Summary_Module()
        input = cls.user_input_box.toPlainText()
        output_content = story_mod.generate_summary(input)

    title = cls.text_title_input.text()
    content = output_content
    db_context.save_entry(title, False, content, category)

    set_focus_doc_obs_view(title, category, set_focus_doc_gen_view)
    pass

# def on_click_clipboard_btn(set_clipboard_content, cls: Ui_Doc_Gen_View_Application_Panel):
    # print("[Clicked]:on_click_clipboard_btn")
    # set_clipboard_content(cls.output_box.toPlainText())
    #
    # msgbox = QMessageBox(
    # QMessageBox.Icon.Information,
    # "Alert",
    # "Copied text to clipboard!",
    # QMessageBox.StandardButton.Ok,
    # parent=cls
    # )
    # msgbox.show()
#
# def on_click_add_favourite_btn(cls: Ui_Doc_Gen_View_Application_Panel):
    # print("[Clicked]:on_click_add_favourite_btn")
    # title = cls.file_name.text()
    # if title == "File_Name":
    # msgbox = QMessageBox(
    # QMessageBox.Icon.Warning,
    # "Warning",
    # "Please save the text first!",
    # QMessageBox.StandardButton.Ok,
    # parent=cls
    # )
    # msgbox.show()
    # return
    #
    # db_context = Db_Module.get_instance()
    # content = cls.output_box.toPlainText()
    # db_context.update_entry(title,title,True,content)
#
    # msgbox = QMessageBox(
    # QMessageBox.Icon.Information,
    # "Alert",
    # "Added to Favourites!",
    # QMessageBox.StandardButton.Ok,
    # parent=cls
    # )
    # msgbox.show()
#
# def on_click_share_btn(set_clipboard_mime_data, cls: Ui_Doc_Gen_View_Application_Panel):
    # print("[Clicked]:on_click_share_btn")
    # title = cls.file_name.text()
    # print(f"file_name: \"{title}\"")
    # if title == "File_Name":
    # print("Inside the if statement")
    # msgbox = QMessageBox(
    # QMessageBox.Icon.Warning,
    # "Warning",
    # "Please save the text first!",
    # QMessageBox.StandardButton.Ok,
    # parent=cls
    # )
    # msgbox.show()
    # return
#
    # table = str("STORY")
    # if cls.action_label.text() == "Summary Generation":
    # table = "SUMMARY"
    # if cls.action_label.text() == "Story Generation":
    # table = "STORY"
#
    # db_context = Db_Module.get_instance()
#
    # content = db_context.load_entry(title,table)
    # html_string = f"""
    # <html>
    # <body>
    # <h1>{title}</h1>
    # {content[-1]}
    # <body>
    # </html>
    # """
    # html_file = weasyprint.HTML(string=html_string)
    # filename: str = QFileDialog.getSaveFileName(cls,"Save file as",f"{title}.pdf","PDF Files (*.pdf)")[0]
    # print(f"[filename]: {filename}")
#
    # with open(filename,"wb") as file:
    # file_content = html_file.write_pdf(stylesheets=["src/genlore/ui_modules/doc_gen_view/page.css"])
    # file.write(file_content)
#
    # mime_data = QMimeData()
    # # mime_data.setText(filename)
    # mime_data.setUrls([QUrl.fromLocalFile(filename),])
    # set_clipboard_mime_data(mime_data)
