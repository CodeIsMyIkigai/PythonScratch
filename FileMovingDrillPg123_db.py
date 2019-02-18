#!/usr/bin/python3

import sqlite3

def createDB():
    conn = sqlite3.connect('FileMoveTracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_file_mtimes (\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_batch TEXT, \
                    col_fname TEXT, \
                    col_mtime TEXT)")
        conn.commit()
    conn.close()

def logMove(batch, fname, mtime):
    conn = sqlite3.connect('FileMoveTracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_file_mtimes (col_batch, col_fname, col_mtime) VALUES (?,?,?)", (batch, fname, mtime))
        conn.commit()
    conn.close()

def printLogs(batch):
    conn = sqlite3.connect('FileMoveTracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_fname, col_mtime from tbl_file_mtimes where col_batch=?", [batch])
        files = cur.fetchall()
        for file in files:
            print("File Name: {}  mtime: {}".format(file[0], file[1]))

if __name__ == "__main__":
    createDB()
    logMove("batch", "file name", "mtime")
    printLogs("batch")


