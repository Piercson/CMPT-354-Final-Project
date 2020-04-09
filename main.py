import psycopg2
import time
import datetime
from datetime import date
import getpass
import sys
def create_tables(conn):
    connection = conn
    try:
        cursor = connection.cursor()
        cursor.execute(open("create_tables.sql", "r").read())
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def drop_tables(conn):
        connection = conn
        try:
            cursor = connection.cursor()
            cursor.execute(open("drop_tables.sql", "r").read())
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
def insert_data(conn):
            connection = conn
            try:
                cursor = connection.cursor()
                cursor.execute(open("insert_researchers.sql", "r").read())
                cursor.execute(open("insert_call.sql", "r").read())
                cursor.execute(open("insert_proposal.sql", "r").read())
                cursor.execute(open("insert_collaborator.sql", "r").read())
                cursor.execute(open("insert_conflicts.sql", "r").read())
                cursor.execute(open("insert_review.sql", "r").read())
                connection.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
def main():
    if not sys.stdin.isatty():
        print("Use 'winpty python main.py' instead")
        return
    else:
        user1 = input("Username: ")
        password1 = getpass.getpass("Password: ")
        host1 = input("Host: ")
        database1 = input("Database: ")
    connection = None
    try:
        connection = psycopg2.connect(user = user1,
                                      password = password1,
                                      host = host1,
                                      database = database1)

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
        inp = None
        while(inp != 'q'):
            print("[1] to create Tables \n[2] to Drop Tables\n[3] to insert data\n[q] to exit")
            inp = input("Select a Command: ")
            print(inp)
            if(inp == '1'):
                create_tables(connection)
            elif(inp == '2'):
                drop_tables(connection)
            elif(inp == '3'):
                insert_data(connection)
            elif(inp == 'q' or input == 'Q'):
                print("goodbye :(")
            else:
                print("invalid input")
        #insert_data(connection);

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
if __name__ == '__main__':
    main()
