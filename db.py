import sqlite3
import pickle
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def add_user(self, userid):
        with self.connection:
            user = self.get_user_userid(userid)
            if user is None:
                return self.cursor.execute("INSERT INTO users (userid) VALUES (?)", (userid,))
    
    def get_user_userid(self,userid):
        with self.connection:
            return self.cursor.execute("SELECT * FROM users WHERE userid = ?", (userid,)).fetchone()
    def get_users_with_timesub(self):
        with self.connection:
            return self.cursor.execute(
                "SELECT * FROM users WHERE timesub IS NOT NULL AND timesub != ''"
            ).fetchall()

    def set_user_timesub(self,userid, timesub):
        with self.connection:
            return self.cursor.execute("UPDATE users SET timesub = ? WHERE userid LIKE ?",
                                        (timesub, userid)).fetchone()

