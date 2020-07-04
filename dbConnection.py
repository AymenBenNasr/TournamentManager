import mysql.connector
import sys
class MyDBTest():

    def __init__(self):
        self.db = mysql.connector.connect(host="localhost", user="root", password="", database="projectdb")
        self.cursor = self.db.cursor(buffered=True)
