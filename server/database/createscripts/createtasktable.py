from pathlib import Path
import sqlite3

con = sqlite3.connect(str(Path(__file__).parent.parent) + '/data.sqlite')
cur = con.cursor()
cur.execute('create table task (id integer primary key, fin bit, priority smallint, add_date date, fin_date date, name ntext, discription ntext, project_id int)')
cur.close()
con.commit()
con.close()
