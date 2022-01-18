import sqlite3


class DatabaseOps(object):
    def __init__(self):
        conn = sqlite3.connect("Iots.db")
        cur = conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS temp_sensors 
                (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                temperature INTEGER,
                )
            """)
        self.conn.commit()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS pressure_sensors 
                (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                pressure INTEGER,
                )
            """)
        self.conn.commit()
        self.cur.execute(
                    """CREATE TABLE IF NOT EXISTS devices 
                        (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name text,
                        temp_sensor INTEGER FOREIGN KEY REFERENCES temp_sensors(Id),
                        pressure_sensor INTEGER FOREIGN KEY REFERENCES pressure_sensor(Id),
                        )
                    """)
        self.conn.commit()

    def read(self, table_name, columns, *args):
        self.cur.execute("select {} from {} ".format(columns, table_name))
        records = self.cur.fetchone()
        return records

    def update(self, table_name, column, value, *args):
        self.cur.execute("update {} set {}={} where {}".format(table_name, column, value, *args))
        self.cur.commit()
        return "value Updated"

    def delete(self, table_name, *args):
        self.cur.execute("delete from {} where {}".format(table_name, *args))
        self.cur.commit()
        return "value Updated"
