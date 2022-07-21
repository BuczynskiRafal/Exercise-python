import sqlite3


conn = sqlite3.connect('app.db')

cur = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS category (
    category_id INTEGER PRIMARY KEY,
    category_name  TEXT NOT_NULL
);'''

cur.execute(sql)

vals = '''INSERT INTO category (category_name) VALUES ('technology');
INSERT INTO category (category_name) VALUES ('e-commerce');
INSERT INTO category (category_name) VALUES ('gaming')
'''
cur.executescript(vals)

categories = cur.execute('SELECT * FROM category').fetchall()
print(categories)

conn.commit()

conn.close()