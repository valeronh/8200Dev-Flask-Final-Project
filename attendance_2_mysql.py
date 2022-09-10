import mysql.connector
import pandas as pd


def open_connection():
    mydb=mysql.connector.connect(
        host="localhost",
        user="valerys",
        password="V@le1988",
        database="valerydb"
    )
    return mydb

def select_owner():
    print("Contents of the table: ")
    mycursor.execute("SELECT * from owner")
    print(mycursor.fetchall())

def reset_owner():
    try:
        mycursor.execute("DELETE FROM owner")
        mydb.commit()
        mydb.flush()
    except:
        mydb.rollback()

def insert_owner(name, average):
    sql = "INSERT INTO owner (name, average) VALUES (%s, %s)"
    val = (name, average)
    mycursor.execute(sql, val)
    mydb.commit()

def read_csv(csvfile):
    df = pd.read_csv(csvfile)
    for i, row in df.iterrows():
        insert_owner(row['names'], row['average'])

mydb = open_connection()
mycursor = mydb.cursor()
if __name__ == "__main__":
    select_owner()
    reset_owner()
    read_csv('attendance.csv')
    select_owner()
    mydb.close()

