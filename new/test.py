import facebook
import requests
import sqlite3


"""cur.execute('INSERT INTO users (id, existence) VALUES("100001103449059", "?")')
con.commit()
print (cur.lastrowid)

cur.execute('SELECT * FROM users')
print (cur.fetchall())
con.close()"""
def check_exist_user_by_id(db_witd_ids):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id VARCHAR(100), existence VARCHAR(15))')
    con.commit()
    cur.executescript("""
     insert into users values ('100001103449059', 'null');
     insert into users values ('000001103449059', 'null');
     insert into users values ('zuck', 'null');
     insert into users values ('4', 'null');
     insert into users values ('nasksadj.masd', 'null');
     insert into users values ('501012028', 'null');
    """)
    """out = open('out_ids.txt', 'w')"""
    graph = facebook.GraphAPI('1938851329475559|9N7KF0F4LokFujG_oTibHwz3YwM')
    with open(db_witd_ids, 'r') as f:
        ids = f.readlines()
        for id in ids:
            id = id.strip()
            if id.isdigit():
                try:
                    graph.get_object(id)
                    out.write('Exist {}\n'.format(id))
                    print(id)
                except Exception as e:
                    out.write('Not Exist {}\n'.format(id))
                    print(id)
                    print(e)
            else:
                resp = requests.get('https://www.facebook.com/{}'.format(id))
                if 'не найдена' in resp.text:
                    out.write('Not Exist {}\n'.format(id))
                    print(id)
                else:
                    out.write('Exist {}\n'.format(id))
                    print(id)
    con.close()
    out.close()
    return

check_exist_user_by_id('ids')