# This file contains functions used by the Class Doc_Obs_View
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import weasyprint
import os
import platform

from src.genlore.ui_modules.doc_obs_view.ui_application_panel import Ui_Doc_Obs_View_Application_Panel
from src.genlore.modules.db_module.db_module import Db_Module

# ? Should shift to MainWindow
if platform.system() == "Windows":
    if platform.release() != "11":
        print("[ERROR]: Application supports Windows 11 or newer only!!!")
        QMessageBox.critical(None, "Not supported current Windows version",
                             "Module used for making pdf requires Windows 11 or above to work!", QMessageBox.StandardButton.Ok)

    else:
        if not os.path.exists(r"C:\\Program Files\\GTK3-Runtime Win64"):
            print("[ERROR]: Please install GTK3 Runtime for Windows!!!")
            QMessageBox.critical(None, "GTK3 Runtime not installed",
                                 "Please install GTK3 Runtime for Windows!!!", QMessageBox.StandardButton.Ok)
        else:
            os.add_dll_directory(r"C:\\Program Files\\GTK3-Runtime Win64\bin")


def on_click_clipboard_btn(table_name: str, set_clipboard_content, cls: Ui_Doc_Obs_View_Application_Panel):
    print("[Clicked]:on_click_clipboard_btn")
    title = cls.file_name.text()
    db_context = Db_Module.get_instance()
    entry = db_context.load_entry(title, table_name)
    is_favourite = entry[1]
    content = entry[2]

    t_content = cls.file_content.toPlainText()
    if content != t_content:
        result = QMessageBox.question(cls, "Unsaved Changes", "Do you want to save the document?",
                                      QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        if result == QMessageBox.StandardButton.Yes:
            db_context.update_entry(
                title, title, is_favourite, t_content, table_name)
            content = t_content
        else:
            QMessageBox.information(
                cls, "Alert", "Will use the last saved document.", QMessageBox.StandardButton.Ok)

    set_clipboard_content(content)

    QMessageBox.information(
        cls, "Alert", "Copied text to clipboard!", QMessageBox.StandardButton.Ok)


def on_click_add_favourite_btn(table_name: str, cls: Ui_Doc_Obs_View_Application_Panel):
    print("[Clicked]:on_click_add_favourite_btn")
    title = cls.file_name.text()

    if title == "File_Name":
        QMessageBox.warning(cls, "Warning", "Please save the text first!",
                            QMessageBox.StandardButton.Ok)
        return

    db_context = Db_Module.get_instance()

    entry = db_context.load_entry(title, table_name)

    is_favourite = entry[1]
    content = entry[2]

    t_content = cls.file_content.toPlainText()
    if content != t_content:
        result = QMessageBox.question(cls, "Unsaved Changes", "Do you want to save the document?",
                                      QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        if result == QMessageBox.StandardButton.Yes:
            db_context.update_entry(
                title, title, is_favourite, t_content, table_name)
            content = t_content
        else:
            QMessageBox.information(
                cls, "Alert", "Will use the last saved document.", QMessageBox.StandardButton.Ok)

    display_msg: str = ""
    if is_favourite:
        db_context.update_entry(title, title, False, content, table_name)
        display_msg = "Removed from Favorites!"
    else:
        db_context.update_entry(title, title, True, content, table_name)
        display_msg = "Added to Favourites!"

    QMessageBox.information(
        cls, "Alert", display_msg, QMessageBox.StandardButton.Ok)


def on_click_share_btn(table_name: str, set_clipboard_mime_data, cls: Ui_Doc_Obs_View_Application_Panel):
    print("[Clicked]:on_click_share_btn")
    title = cls.file_name.text()
    print(f"file_name: \"{title}\"")
    if title == "File_Name":
        print("Inside the if statement")
        QMessageBox.warning(
            cls, "Warning", "Please save the text first!", QMessageBox.StandardButton.Ok)
        return

    db_context = Db_Module.get_instance()

    entry = db_context.load_entry(title, table_name)
    is_favourite = entry[1]
    content = entry[2]
    modified_timestamp = entry[3]
    creation_timestamp = entry[4]

    t_content = cls.file_content.toPlainText()
    if content != t_content:
        result = QMessageBox.question(cls, "Unsaved Changes", "Do you want to save the document?",
                                      QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        if result == QMessageBox.StandardButton.Yes:
            db_context.update_entry(
                title, title, is_favourite, t_content, table_name)
            content = t_content
        else:
            QMessageBox.information(
                cls, "Alert", "Will use the last saved document.", QMessageBox.StandardButton.Ok)

    html_string = f"""
    <html>
    <body>
        <h1>{title}</h1>
        <p><i>Creation Timestamp: {creation_timestamp}</i></p>
        <p><i>Modified Timestamp: {modified_timestamp}</i></p>
        <p>{content}</p>
    <body>
    </html>
    """
    html_file = weasyprint.HTML(string=html_string)
    filename: str = QFileDialog.getSaveFileName(
        cls, "Save file as", f"{title}.pdf", "PDF Files (*.pdf)")[0]
    print(f"[filename]: {filename}")

    with open(filename, "wb") as file:
        file_content = html_file.write_pdf(
            stylesheets=["src/genlore/ui_modules/doc_gen_view/page.css"])
        file.write(file_content)

    # Windows Support Only
    mime_data = QMimeData()
    # mime_data.setText(filename)
    mime_data.setUrls([QUrl.fromLocalFile(filename), ])
    set_clipboard_mime_data(mime_data)


def on_click_save_btn(cls: Ui_Doc_Obs_View_Application_Panel):
    print("[Clicked]:on_click_save_btn")
    title = cls.file_name.text()
    res = QMessageBox.question(
        cls,
        "Save",
        "Are you sure you want to make changes?",
        QMessageBox.StandardButton.Yes |
        QMessageBox.StandardButton.No,
    )

    if res == QMessageBox.StandardButton.No:
        print("Reached Here")
        QMessageBox.information(
            cls,
            "Aborted",
            "Didn't save the content",
            QMessageBox.StandardButton.Ok,
        )
        return

    db_context = Db_Module.get_instance()
    content = cls.file_content.toPlainText()
    db_context.update_entry(title, title, True, content)

    QMessageBox.information(
        cls,
        "Save",
        "Data updated successfully!",
        QMessageBox.StandardButton.Ok,
    )
