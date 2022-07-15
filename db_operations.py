import mysql.connector

class db_operations():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "34.132.37.188",
            user = "root",
            password = "Nikki1108",
            database = "cpsc408"
        )
        self.cursor = self.connection.cursor()
        print("connection made...")

    # function for inserting multiple rows
    # (single query inserts a single record, executemany runs query multiple times)
    def bulk_insert(self, query, data):
         self.cursor.executemany(query, data)
         self.connection.commit()

    # function for running a single query that returns a single value
    # (retrieves the ID from another table -> foreign key)
    def getID(self, query, value):
        self.cursor.execute(query, [value])
        result = self.cursor.fetchone()
        return result[0]
