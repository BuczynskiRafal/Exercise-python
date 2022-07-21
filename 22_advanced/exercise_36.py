import sqlite3


conn = sqlite3.connect('app.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)''')

cur.executescript('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org');

INSERT INTO customer (first_name, last_name, email)
VALUES ('Joe', 'Doe', 'joe.doe@esmartdata.org');

INSERT INTO customer (first_name, last_name, email)
VALUES ('Mike', 'Smith', 'mike.smith@esmartdata.org');''')

# Enter your solution here
cur.execute('SELECT COUNT(*) FROM customer')
data = cur.fetchall()
print(data)

conn.commit()
conn.close()
