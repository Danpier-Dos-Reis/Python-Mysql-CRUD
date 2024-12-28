# DAL (dal.py)
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="dorito",
        password="Dorit@Picant3",
        database="dbtest"
    )

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS testexcel (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        fecha DATE,
        linkurl VARCHAR(255),
        nulos VARCHAR(255)
    )''')
    conn.commit()
    conn.close()

def insert_item(nombre, fecha, linkurl, nulos):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO testexcel (nombre, fecha, linkurl, nulos) VALUES (%s, %s, %s, %s)", (nombre, fecha, linkurl, nulos))
    conn.commit()
    conn.close()

def get_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM testexcel")
    items = cursor.fetchall()
    conn.close()
    return items

def get_item_by_id(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM testexcel WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    conn.close()
    return item

def update_item(item_id, nombre, fecha, linkurl, nulos):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE testexcel SET nombre = %s, fecha = %s, linkurl = %s, nulos = %s WHERE id = %s", (nombre, fecha, linkurl, nulos, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM testexcel WHERE id = %s", (item_id,))
    conn.commit()
    conn.close()
