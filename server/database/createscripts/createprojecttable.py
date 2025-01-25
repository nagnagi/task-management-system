from pathlib import Path
import sqlite3

con = sqlite3.connect(str(Path(__file__).parent.parent) + '/data.sqlite')
cur = con.cursor()
cur.execute('create table project (id integer primary key, name ntext, discription ntext, due_date date)')
cur.close()
con.commit()
con.close()