import sqlite3
con = sqlite3.connect('db.sqlite')
cursor = con.cursor()

def insert_penghuni():
    query = 'insert into penghuni(namapenghuni) VALUES (\'%s\');'
    query = query  % ('Alifia')
    cursor.execute(query)
    con.commit()


def select_penghuni():
    query = 'select * from penghuni'  
    cursor.execute(query)
    all_results = cursor.fetchall()
    con.commit()
    for result in all_results:
        print(result)

select_penghuni()
# insert_penghuni()