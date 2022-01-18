# -*- coding: utf-8 -*-

from flask import Flask
import sqlite3

conn = sqlite3.connect("Iots.db")
print(conn)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS devices 
            (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                temp_sensor text,
                pressure_sensor integer 
            )
            """)
conn.commit()
cur.close()
conn.close()


app = Flask()


