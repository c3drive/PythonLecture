import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

create_history_query = """
CREATE TABLE IF NOT EXISTS History (
    Name TEXT,
    Age INTEGER
);
"""
cursor.execute(create_history_query)
target_name = input("whose 'age' do you want to update?: ")
new_age = input("Tell me new age: ")
update_query = 'UPDATE User SET age = ? WHERE name = ?;'
insert_history_query = 'INSERT INTO History VALUES (?, ?);'

try:
    cursor.execute(insert_history_query, (target_name,new_age))
    cursor.execute(update_query, (new_age, target_name))
except sqlite3.Error:
    print("sqlite3 erro occurred")
    con.rollback()
else:
    con.commit()