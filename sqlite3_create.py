import sqlite3
from sqlite3 import Error
from sys import exit
def getConnection():
    '''A function to create connection to the database
       If the database is not there it will be created.
       If any error comes we will simply exit the program
    '''
    try:
        conn = sqlite3.connect('student.db')
        return conn
    except Error:
        '''Any error related to sqllite will be handled here'''
        print("Error while connecting to db",Error)
        exit(-1)
    except Exception as e:
        '''if any other occurs it will be handled here'''
        print("Another Error",e)
        exit(-1)


def createTable(conn):
    '''cursor is like a new session we create to make changes to the database''' 
    cursorObj = conn.cursor()

    '''the changes we want to make should be passed through the execute function
    We can have multiple execute commands one after the other like creating database then inserting values to it'''
    cursorObj.execute('CREATE TABLE student(name text,marks number)')

    '''finally we commit the changes to the database so that the database creates a checkpoint'''
    conn.commit()

'''Creating connection using the getconnection function and storing it in a variable'''
conn = getConnection()
'''We are passing the connection to create table function using which it will make changes to the database'''
createTable(conn)
'''Closing the connection we have made to the database'''
conn.close()