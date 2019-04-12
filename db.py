import sqlite3

conn = sqlite3.connect('main.db')
c = conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS alerts(ID INTEGER PRIMARY KEY, asset TEXT, beep TEXT, desc TEXT, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP); """)
conn.commit()
conn.close() 

def insert_method(server, alarm, action):
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    if c.execute("INSERT INTO alerts (asset, beep, desc) VALUES(?, ?, ?)", (server, alarm, action)):
        conn.commit()
        conn.close() 
        print "Success"
    else:
        conn.close() 
        print "Failed"

def select_method():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    if c.execute("SELECT * FROM alerts"):
        conn.commit()
        print "select output:", c.fetchall()
        conn.close()
        return True
    else:
        conn.close()
        return False
