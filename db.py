import sqlite3 
from datetime import datetime

conn = sqlite3.connect("Discord.db")
cursor = conn.cursor()

def addmoney(money):
    cursor.execute(f"""INSERT INTO money (money, date)
                    VALUES ({money}, '{datetime.now().strftime('%Y-%m-%d')}')""")
    conn.commit()


def balance():
    cursor.execute(f"""SELECT sum(money) FROM money""")
    data = cursor.fetchone()
    return data[0]