import sqlite3  # модуль sqlite
conn = sqlite3.connect("Discord.db")  # или :memory:
cursor = conn.cursor()
cost = conn.row[2]