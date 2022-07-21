import sqlite3

conn = sqlite3.connect('app.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS category')

cur.execute('''CREATE TABLE category (
    category_id   INTEGER,
    category_name TEXT    NOT NULL,
    PRIMARY KEY (category_id)
)''')

cur.execute('''INSERT INTO category (category_name) VALUES ('technology')''')
cur.execute('''INSERT INTO category (category_name) VALUES ('e-commerce')''')
cur.execute('''INSERT INTO category (category_name) VALUES ('gaming')''')
conn.commit()

# Enter your solution here
conn.execute("UPDATE category SET category_name = 'online shop' "
             "WHERE category_id == 2").fetchall()
for row in conn.execute('SELECT * FROM category').fetchall():
    print(row)

conn.close()

conn.close()