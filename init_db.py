import sqlite3
import json
import typing
import time

class Connection:
    def __init__(self, db : str) -> None:
        """
        :type db: str
        :rtype: None
        """
        
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def close(self) -> None:
        """
        :rtype: None
        
        - Terminates the connection to the database
        """
        self.conn.close()


    def init_db(self) -> None:
        """
        :rtype: None

        - Initializes tables for dungeons and mentor roulette instances
        """
        

        self.cur.execute("""CREATE TABLE IF NOT EXISTS dungeons (
                         id INTEGER PRIMARY KEY, 
                         expansionId INTEGER, 
                         contentTypeId INTEGER, 
                         levelRequired INTEGER, 
                         nameEn TEXT, 
                         descriptionEn TEXT)""")
        self.conn.commit()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS mentor (
                         
                         date INTEGER,
                         completed INTEGER, 
                         FOREIGN KEY(instance) REFERENCES dungeons(id), 
                         job INTEGER, 
                         progress INTEGER, 
                         first INTEGER, 
                         FOREIGN KEY(instance) REFERENCES dungeons(id))""")
        self.conn.commit()

    def import_data(self) -> None:
        """
        :rtype: None

        - Imports instance and class data into the database
        TODO: API calls and json conversion
        """
        return

    def insert_record(self, completed, instance, job, progress, first) -> None: 
        """
        TODO: figure out something better
        """
        date = None


if __name__ == '__main__':

    comm = Connection('mrtracker.db')
    comm.init_db()
    comm.close()
    