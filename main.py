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

def run_queries(conn):
    inp = None
    while (inp != 'q'):
        print("\nSelect a query to run (or q to return to the previous menu): ")
        print(  "[1] Find competitions open during a specific month \
                \n[2] Find competitions by area and PI \
                \n[3] Largest Proposal for an area \
                \n[4] Proposals submitted before a date awarded the largest amount of money \
                \n[5] Average discrepancy between requested amount and awarded ammount for an area \
                \n[6] Assign reviewers to a grant application \
                \n[7] Check if a meeting room is available \
                \n[q] Return")
        inp = input("Enter a menu option: ")
        print(inp)
        if(inp == '1'):
            print("Running query 1...")
            run_query1(conn)
        elif(inp == '2'):
            print("Running query 2...")
            run_query1(conn)
        elif(inp == '3'):
            print("Running query 3...")
            run_query2(conn)
        elif(inp == '4'):
            print("Running query 4...")
            run_query4(conn)
        elif(inp == '5'):
            print("Running query 5...")
            run_query5(conn)
        elif(inp == '6'):
            print("Running query 6...")
            run_query6(conn)
        elif(inp == '7'):
            print("Running query 7...")
            run_query7(conn)
        elif(inp == 'q' or inp == 'Q'):
            print("Returning to previous menu...\n")

def run_query1(conn):
    ### Insert code for query 1 here ###

    cur = conn.cursor()

    # run queries to get range of proposals for user and output it.
    cur.execute("SELECT call.deadline FROM call WHERE call.status = 'open' AND call.deadline <= ALL (SELECT c.deadline FROM call c WHERE c.status = 'open');")
    result = cur.fetchall()
    minDate = result[0][0] # result[0][0] == YYYY-MM-DD

    minDate1 = datetime.date(minDate.year, minDate.month, 1)
    
    cur.execute("SELECT call.deadline FROM call WHERE call.status = 'open' AND call.deadline >= ALL (SELECT c.deadline FROM call c WHERE c.status = 'open');")
    result = cur.fetchall()
    maxDate = result[0][0]

    if maxDate.month == 1 or maxDate.month == 3 or maxDate.month == 5 or maxDate.month == 7 or maxDate.month == 8 or maxDate.month == 10 or maxDate.month == 12:
        maxDateDay = 31
    elif maxDate.month == 4 or maxDate.month == 6 or maxDate.month == 9 or maxDate.month == 11:
        maxDateDay = 30
    elif maxDate.month == 2:
        maxDateDay = 28

    maxDate1 = datetime.date(maxDate.year, maxDate.month, maxDateDay)

    # ask user to enter a month in range and validate it
    validInp = False
    while(not validInp):
        print("Select a month and year to query between ", minDate.year, "-", minDate.month, " and ", maxDate.year, "-", maxDate.month)
        inpMonth = int(input("Enter an month (format: MM | integer from 1-12 | ex. 03): "))
        inpYear = int(input("Enter a year (format: YYYY | ex. 2020): "))
        inputDate = datetime.date(inpYear, inpMonth, 1)
        if inputDate >= minDate1 and inputDate <= maxDate1:
            validInp = True
        else:
            print("Invalid Date entered!")

    print(inputDate)

    # run query on month

    

    ### end of query 1 code ###
    pass

def run_query2(conn):
    ### Insert code for query 2 here ###

    ### end of query 2 code ###
    pass

def run_query3(conn):
    ### Insert code for query 3 here ###

    ### end of query 3 code ###
    pass

def run_query4(conn):
    ### Insert code for query 4 here ###

    ### end of query 4 code ###
    pass

def run_query5(conn):
    ### Insert code for query 5 here ###

    ### end of query 5 code ###
    pass

def run_query6(conn):
    ### Insert code for query 6 here ###

    ### end of query 6 code ###
    pass

def run_query7(conn):
    ### Insert code for query 7 here ###

    ### end of query 7 code ###
    pass

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
            print("What would you like to do? Enter: ")
            print("[1] to Create all Tables \n[2] to Drop all Tables\n[3] to Insert all Data\n[4] to Run Queries \n[q] to exit")
            inp = input("Select a Command: ")
            print(inp)
            if(inp == '1'):
                create_tables(connection)
            elif(inp == '2'):
                drop_tables(connection)
            elif(inp == '3'):
                insert_data(connection)
            elif(inp == '4'):
                run_queries(connection)
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
