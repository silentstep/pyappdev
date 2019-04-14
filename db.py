import sqlite3

class Worker():

    def __init__(self):
        self.conn = sqlite3.connect('main.db')
        self.c = self.conn.cursor()

    def qry_insert(self, server, alarm, action):

        if self.c.execute("INSERT INTO alerts (server, alarm, action) VALUES(?, ?, ?)", (server, alarm, action)):
            self.conn.commit()
            print "Successful insert query"
            return True

        self.conn.close() 
        print "Failed insert query"
        return False

    def qry_select(self):
        
        if self.conn:
            result = self.c.execute("SELECT * FROM alerts ORDER BY ID DESC LIMIT 1")
            items = [dict(zip([key[0] for key in self.c.description], row)) for row in result]
            print "Successful select query"
            return items

        self.conn.close()
        print "Failed select query"
        return False
