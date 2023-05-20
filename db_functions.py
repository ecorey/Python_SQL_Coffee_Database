import db_config_file
from tkinter import messagebox
import pymysql

class DatabaseError(Exception):
    def __init__(self, e):
        super().__init__(e)


def open_database():
    try:
        con = pymysql.connect(host=db_config_file.DB_SERVER,
                              user=db_config_file.DB_USER,
                              password=db_config_file.DB_PASS,
                              database=db_config_file.DB,
                              port=db_config_file.DB_PORT)
        return con

    except pymysql.InternalError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.OperationalError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.NotSupportedError as e:
        print(e)
        raise DatabaseError(e)


def query_database(con, sql, values):
    try:
        cursor = con.cursor()
        cursor.execute(sql, values)
        rows = cursor.fetchall()
        num_of_rows = cursor.rowcount

    except pymysql.InternalError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.OperationalError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.ProgrammingError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.DataError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.IntegrityError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.NotSupportedError as e:
        print(e)
        raise DatabaseError(e)
    finally:
        cursor.close()
        con.close()
        return num_of_rows, rows


def insert_into_database(first_field, second_field):
    try:
        con = pymysql.connect(host=db_config_file.DB_SERVER,
                              user=db_config_file.DB_USER,
                              password=db_config_file.DB_PASS,
                              database=db_config_file.DB,
                              )
        sql = "INSERT INTO `sie557`.`coffee_name` (coffee_name_ID, name) VALUES (%s, %s)"
        vals = (first_field, second_field)
        cursor = con.cursor()
        cursor.execute(sql, vals)
        con.commit()
        cursor.close()
        con.close()

        messagebox.showinfo("Database", "Record Added to Database")

    except Exception as e:
        print(e)


def insert_database(con, sql, vals):
    try:
        cursor = con.cursor()
        cursor.execute(sql, vals)
        con.commit()
    except Exception as e:
        print(e)

