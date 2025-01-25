from pathlib import Path
import sqlite3

con = sqlite3.connect(str(Path(__file__).parent.parent) + '/data.sqlite')
cur = con.cursor()
cur.execute('create table todolist (id integer primary key, todo_id integer, add_date date)')
cur.close()
con.commit()
con.close()
