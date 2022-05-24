import sqlite3
from log_pass import x

try:
    base = sqlite3.connect('resources.db')
    cur = base.cursor()
    name = 'data'
    base.execute(f'CREATE TABLE IF NOT EXISTS {name}(login PRIMARY KEY, password)')

    '''
    base.commit()
    
    cur.execute('INSERT INTO data VALUES(?, ?)', ('denis', '6547123'))
    base.commit()
    
    cur.executemany('INSERT INTO data VALUES(?, ?)', x)
    base.commit()
    
    r = cur.execute('SELECT * FROM data').fetchall()
    r = cur.execute('SELECT login FROM data').fetchall()
    r = cur.execute('SELECT password FROM data WHERE login == ?', ('user10', )).fetchone()
    
    
    cur.execute('UPDATE data SET password == ? WHERE login == ?', ('123456789', 'user7'))
    
    cur.execute('UPDATE data SET password == ? WHERE password == ?', ('999', '1001'))
    '''

    cur.execute('DELETE FROM data WHERE password == ?', ('999',))
    base.commit()
    cur.close()

except sqlite3.Error as error:
    print('Ошибка подключения к бд ', error)

finally:

    if base:
        base.close()
    # base.execute('DROP TABLE IF EXISTS data') Удаление таблицы
