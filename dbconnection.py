import psycopg2
import sys

host='localhost'
user='mostafa'
password='123'
dbname='iti_db'
def connect():
    try:
        connection = psycopg2.connect(host=host,password=password,user=user,dbname=dbname)
        return connection
    except:
        print(sys.exc_info()[1])

def createtable(query):
    connect1=connect()
    try:
        cur=connect1.cursor()
        cur.execute(query)
        connect1.commit()
    except:
        print(sys.exc_info()[1])

def insert(query):
    connect1=connect()
    try:
        cur=connect1.cursor()
        cur.execute(query)
        connect1.commit()

    except:
        print(sys.exc_info()[1])

def select(query):
    connect1=connect()
    try:
        cur=connect1.cursor()
        cur.execute(query)
        return cur.fetchall()

    except:
        print(sys.exc_info()[1])


def update(query):
    connect1=connect()
    try:
        cur=connect1.cursor()
        cur.execute(query)
        connect1.commit()

    except:
        print(sys.exc_info()[1])