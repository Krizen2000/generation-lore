from threading import Lock
import datetime
import sqlite3
sqlite3.register_adapter(bool,int)
sqlite3.register_converter("BOOLEAN",lambda val: bool(int(val)))


class Db_Module:

    _instance = None
    _lock = Lock()

    def __init__(self):
        if self._instance:
            raise Exception("More than one instance of a Singleton class is not permitted!")

        # self._db_con = sqlite3.connect("content_records.db?mode=rw",uri=True,detect_types=sqlite3.PARSE_DECLTYPES)
        self._db_con = sqlite3.connect("content_records.db",detect_types=sqlite3.PARSE_DECLTYPES)
        print("[Database]: Connected successfully!")

        self._db_con.execute("CREATE TABLE IF NOT EXISTS STORY (TITLE TEXT, FAVOURITE BOOLEAN, CONTENT TEXT, MODIFIED TIMESTAMP, CREATED TIMESTAMP);")
        self._db_con.execute("CREATE TABLE IF NOT EXISTS SUMMARY (TITLE TEXT, FAVOURITE BOOLEAN, CONTENT TEXT, MODIFIED TIMESTAMP, CREATED TIMESTAMP);")

    def save_entry(self,title,is_favourite,content,table="STORY"):
        timestamp = datetime.datetime.now()
        cmd = f"INSERT INTO {table} VALUES (?,?,?,?,?);"
        self._db_con.execute(cmd,(title,is_favourite,content,timestamp,timestamp))
        self._db_con.commit()

    def update_entry(self,prev_title,title,is_favourite,content,table="story"):
        timestamp = datetime.datetime.now()
        cmd = f"UPDATE {table} SET TITLE = ?, FAVOURITE = ?, CONTENT = ?, MODIFIED = ? WHERE TITLE = ?;"
        self._db_con.execute(cmd,(title,is_favourite,content,timestamp,prev_title))

    def load_entry(self,title,table="STORY"):
        curr = self._db_con.cursor()
        cmd = f"SELECT * FROM {table} WHERE TITLE = ?;"
        curr.execute(cmd,(title,))
        result = curr.fetchone()
        return result

    def get_recent_entries(self,table="STORY"):
        curr = self._db_con.cursor()
        cmd = f"SELECT TITLE FROM {table} ORDER BY MODIFIED DESC;"
        curr.execute(cmd)
        result = curr.fetchall()
        return result

    def get_favourite_entries(self,table="STORY"):
        curr = self._db_con.cursor()
        cmd = f"SELECT TITLE FROM {table} WHERE FAVOURITE = ?;"
        curr.execute(cmd,(True,))
        result = curr.fetchall()
        return result
    
    def get_all_entries(self,table="STORY"):
        curr = self._db_con.cursor()
        cmd = f"SELECT TITLE FROM {table};"
        curr.execute(cmd)
        result = curr.fetchall()
        return result

    def exists(self,title,table="STORY"):
        curr = self._db_con.cursor()
        cmd = f"SELECT TITLE FROM {table} WHERE TITLE = ?;"
        curr.execute(cmd,(title,))
        result = curr.fetchone()
        if result is None:
            return False
        return True

    def remove_entry(self,title,table="STORY"):
        cmd = f"DELETE FROM {table} WHERE TITLE = ?;"
        self._db_con.execute(cmd,(title,))

    @classmethod
    def close(cls):
        cls._instance._db_con.close()
        cls._instance._db_con = None
        cls._instance = None
        print("[Database]: Disconnected successfully!")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance