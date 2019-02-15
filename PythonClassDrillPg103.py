import sqlite3
import logging

'''
Drill Description:
    For this drill, you will need to write a script that creates a database and adds new data into that database.

Requirements:
    1) Your script will need to use Python 3 and the sqlite3 module.
    2) Your database will require 2 fields, an auto-increment primary integer field and a field with the data type of 
        string.
    3) Your script will need to read from the supplied list of file names at the bottom of this page and determine only
        the files from the list which ends with a “.txt” file extension.
    4) Next, your script should add those file names from the list ending with “.txt” file extension within your
        database.
    5) Finally, your script should legibly print the qualifying text files to the console.

Additional Setup Instructions:
    The following is the list of file names to use for this drill:

    fileList = ('information.docx','Hello.txt','myImage.png', 'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
'''


def createDB(name = 'test.db'):
    conn = sqlite3.connect(name)
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_TextFiles (\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_FileName TEXT)")
        conn.commit()
    return conn

#It's not efficient to create connections in a loop, so I'm passing the connection


def insertFilenameRow(conn, filename):
    #print("In the insert function >>{}<<".format(filename))
    fileNameTuple = [filename]
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_TextFiles (col_FileName) VALUES (?)", fileNameTuple)
        conn.commit()


def getFilenames(conn):
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_FileName FROM tbl_TextFiles")
        fileNames = cur.fetchall()
        return fileNames


fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = None

try:

    conn = createDB('CMT_PythonPg103.db')

    for fileName in fileList:
        if fileName.endswith(".txt"):
            insertFilenameRow(conn, fileName)

    fileNames = getFilenames(conn)

    for file in fileNames:
        print("File: {} was in the DB".format(file[0]))

except Exception as e:
    logging.exception('Failed')
finally:
    conn.close()
