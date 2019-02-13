import sqlite3


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons (\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT, \
                col_lname TEXT, \
                col_email)")
    conn.commit()
conn.close()

'''
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons (col_fname,col_lname,col_email) VALUES (?,?,?)",
                ("Joe", "Blow", "JoeBlow@joeblow.com"))
    cur.execute("INSERT INTO tbl_persons (col_fname,col_lname,col_email) VALUES (?,?,?)",
                ("Sara", "Blow", "SaraBlow@joeblow.com"))
    cur.execute("INSERT INTO tbl_persons (col_fname,col_lname,col_email) VALUES (?,?,?)",
                ("Moe", "Blow", "MoeBlow@joeblow.com"))
    cur.execute("INSERT INTO tbl_persons (col_fname,col_lname,col_email) VALUES (?,?,?)",
                ("Doe", "Blow", "DoeBlow@joeblow.com"))
    cur.execute("INSERT INTO tbl_persons (col_fname,col_lname,col_email) VALUES (?,?,?)",
                ("Kevin", "Bacon", "kbacon@joeblow.com"))

    conn.commit()
conn.close()
'''

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sara'")
    people = cur.fetchall()
    for person in people:
        print("First Name: {}\nLast Name: {}\nEmail: {}".format(person[0], person[1], person[2]))






    conn.commit()
conn.close()