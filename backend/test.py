import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users (id int, username text, password text)'
cursor.execute(create_table)

user = (1, 'jojo', 'asdf')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user)

connection.commit()

connection.close()