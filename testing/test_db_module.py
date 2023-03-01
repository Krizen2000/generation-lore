from matplotlib.pyplot import title
from db_module import Db_Module
from genericpath import exists
import os


def clean_env():
    if exists("content_records.db"):
        os.remove("content_records.db")

def test_connection():
    clean_env()
    Db_Module.get_instance()
    Db_Module.close()

def test_save_entry():
    clean_env()
    Db_context = Db_Module.get_instance()
    title = "The Day is Bright"
    is_favourite = True
    content = "The morning of the day when the person woke had a sparkling rays of hope filled in it's atmosphere"

    Db_context.save_entry(title,is_favourite,content)
    curr = Db_context._db_con.cursor()
    curr.execute("SELECT * FROM STORY")
    result = curr.fetchone()
    print("[Save_Entry]:",result)
    Db_Module.close()

def test_load_entry():
    clean_env()
    Db_context = Db_Module.get_instance()
    title = "The Day is Bright"
    is_favourite = True
    content = "The morning of the day when the person woke had a sparkling rays of hope filled in it's atmosphere"

    Db_context.save_entry(title,is_favourite,content)
    result = Db_context.load_entry(title)
    print("[Load_Entry]:",result)
    Db_Module.close()

def test_update_entry():
    clean_env()
    Db_context = Db_Module.get_instance()
    title = "The Day is Bright"
    new_title = "Bright Morning"
    is_favourite = True
    content = "The morning of the day when the person woke had a sparkling rays of hope filled in it's atmosphere"
    Db_context.save_entry(title,is_favourite,content)

    Db_context.update_entry(title,new_title,False,content)
    result = Db_context.load_entry(new_title)
    print("[Update_Entry]:",result)
    Db_Module.close()

def test_get_favourite_entry():
    clean_env()
    Db_context = Db_Module.get_instance()
    title = "The Day is Bright"
    is_favourite = True
    content = "The morning of the day when the person woke had a sparkling rays of hope filled in it's atmosphere"
    Db_context.save_entry(title,is_favourite,content)

    result = Db_context.get_favourite_entries()
    print("[Get_Favourite_Entry]:",result)
    Db_Module.close()

def test_get_all_entry():
    clean_env()
    Db_context = Db_Module.get_instance()
    title = "The Day is Bright"
    is_favourite = True
    content = "The morning of the day when the person woke had a sparkling rays of hope filled in it's atmosphere"
    Db_context.save_entry(title,is_favourite,content)

    result = Db_context.get_all_entries()
    print("[Get_All_Entry]:",result)
    Db_Module.close()

def test_remove_entry():
    clean_env()
    Db_context = Db_Module.get_instance()
    title = "The Day is Bright"
    is_favourite = True
    content = "The morning of the day when the person woke had a sparkling rays of hope filled in it's atmosphere"
    Db_context.save_entry(title,is_favourite,content)

    Db_context.remove_entry(title)
    result = Db_context.load_entry(title)
    Db_Module.close()
    if result is None:
        print("[Remove_Entry]: Removed successfully!")
    else:
        raise Exception("Couldn't delete the entry")

def test_exists():
    clean_env()
    Db_context = Db_Module.get_instance()
    title = "The Day is Bright"
    is_favourite = True
    content = "The morning of the day when the person woke had a sparkling rays of hope filled in it's atmosphere"
    Db_context.save_entry(title,is_favourite,content)

    status = Db_context.exists(title)
    Db_context.close()
    print("[Exists]: ",status)


if __name__ == "__main__":
    test_connection()
    test_save_entry()
    test_load_entry()
    test_update_entry()
    test_get_favourite_entry()
    test_get_all_entry()
    test_remove_entry()
    test_exists()