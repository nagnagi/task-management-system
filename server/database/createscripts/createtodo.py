from pathlib import Path
import sqlite3

con = sqlite3.connect(str(Path(__file__).parent.parent) + '/data.sqlite')
cur = con.cursor()
cur.execute('create table todo (id integer primary key, task_id int)')
cur.close()
con.commit()
con.close()
