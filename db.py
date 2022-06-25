import sqlite3  # модуль sqlite
conn = sqlite3.connect("Discord.db")  # или :memory:
cursor = conn.cursor()

def addmoney(money, date):
    cursor.execute(f"""INSERT INTO money (money, date)
                    VALUES ({money}, '{date}')""")
    conn.commit()


def balance():
    cursor.execute(f"""SELECT sum(money) FROM money""")
    data = cursor.fetchone()
    return data[0]
print(balance())