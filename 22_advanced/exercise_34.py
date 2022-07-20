import sqlite3


conn = sqlite3.connect('app.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)''')

vals = '''
INSERT INTO customer (first_name, last_name, email) 
VALUES ('John', 'Smith', 'john.smith@mail.org');
INSERT INTO customer (first_name, last_name, email)
VALUES ('Joe', 'Doe', 'joe.doe@esmartdata.org');
 
INSERT INTO customer (first_name, last_name, email)
VALUES ('Mike', 'Smith', 'mike.smith@esmartdata.org');
'''

cur.executescript(vals)
conn.commit()
conn.close()
