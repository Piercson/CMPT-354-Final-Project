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
        cursor.execute(open("HaitKiewThomas-Schema.sql", "r").read())
        connection.commit()
        print("Tables successfully created!\n")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def drop_tables(conn):
    connection = conn
    try:
        cursor = connection.cursor()
        cursor.execute(open("HaitKiewThomas-Drop.sql", "r").read())
        connection.commit()
        print("Tables successfully dropped!\n")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_data(conn):
    connection = conn
    try:
        cursor = connection.cursor()
        cursor.execute(open("HaitKiewThomas-Insert.sql", "r").read())
        connection.commit()
        print("Data successfully inserted!\n")
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
        inp = input("\nEnter a menu option: ")
        #print(inp)
        if(inp == '1'):
            print("Running query 1...\n")
            run_query1(conn)
        elif(inp == '2'):
            print("Running query 2...\n")
            run_query2(conn)
        elif(inp == '3'):
            print("Running query 3...\n")
            run_query3(conn)
        elif(inp == '4'):
            print("Running query 4...\n")
            run_query4(conn)
        elif(inp == '5'):
            print("Running query 5...\n")
            run_query5(conn)
        elif(inp == '6'):
            print("Running query 6...\n")
            run_query6(conn)
        elif(inp == '7'):
            print("Running query 7...\n")
            run_query7(conn)
        elif(inp == 'q' or inp == 'Q'):
            print("Returning to previous menu...\n")
        else:
            print("invalid input")

def run_query1(conn):
    ### Insert code for query 1 here ###

    cur = conn.cursor()

    # run queries to get range of proposals for user and output it.
    cur.execute("   SELECT call.deadline \
                    FROM call \
                    WHERE call.status = 'open' AND call.deadline <= ALL (   SELECT c.deadline \
                                                                            FROM call c \
                                                                            WHERE c.status = 'open');")
    result = cur.fetchall()
    minDate = result[0][0] # result[0][0] == YYYY-MM-DD
    minDate1 = datetime.date(minDate.year, minDate.month, 1)

    cur.execute("   SELECT call.deadline \
                    FROM call \
                    WHERE call.status = 'open' AND call.deadline >= ALL (   SELECT c.deadline \
                                                                            FROM call c \
                                                                            WHERE c.status = 'open');")
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
        inpMonth = int(input("Enter a month (format: MM | integer from 1-12 | ex. 03): "))
        if inpMonth < 0 or inpMonth > 12:
            print("Invalid month!")
            continue

        inpYear = int(input("Enter a year (format: YYYY | ex. 2020): "))
        inputDate = datetime.date(inpYear, inpMonth, 1)
        if inputDate >= minDate1 and inputDate <= maxDate1:
            validInp = True
        else:
            print("Invalid Date entered!")

    # run query on month
    query =    "SELECT C.id, C.title \
                FROM Call C \
                WHERE C.deadline >= %s AND C.status = 'open' AND EXISTS (   SELECT * \
                                                                            FROM proposal P \
                                                                            WHERE P.callid = C.id AND P.status = 'submitted' AND (P.requestedamount > 20000 OR 10 < (   SELECT COUNT(col.researcherid) \
                                                                                                                                                                        FROM collaborator col \
                                                                                                                                                                        WHERE col.proposalid = p.id \
                                                                                                                                                                        GROUP BY col.researcherid) ) );"
    cur.execute(query, [inputDate])
    results = cur.fetchall()

    print("\nID, Title:")
    for row in results:
        print(row)

    ### end of query 1 code ###
    input("\n==============================\nPress [ENTER] to continue... ")

def run_query2(conn):
    ### Insert code for query 2 here ###

    ### end of query 2 code ###
    input("\n==============================\nPress [ENTER] to continue... ")

def run_query3(conn):
    ### Insert code for query 3 here ###
    cur = conn.cursor()
    Q3_AREA = input("Please enter the area of study: ")

    query = "SELECT narrowed1.id, narrowed1.requestedamount \
            FROM ( \
                SELECT p1.* \
                FROM (SELECT * \
                    FROM call c1 \
                    WHERE c1.area = %s) as c2 \
               JOIN proposal p1 ON p1.callid = c2.id) as narrowed1 \
            INNER JOIN ( \
                SELECT MAX(p3.requestedamount) as max_req \
                FROM ( \
                    SELECT * \
                    FROM call c3 \
                    WHERE c3.area = %s) as c4 \
                JOIN proposal p3 ON p3.callid = c4.id) as narrowed2 \
            ON narrowed1.requestedamount = narrowed2.max_req;"
    data = (Q3_AREA, Q3_AREA)
    cur.execute(query,data)
    results = cur.fetchall()
    print("Proposal id: ", results[0][0], " Requested amount: ", results[0][1])
    ### end of query 3 code ###
    input("\n==============================\nPress [ENTER] to continue... ")

def run_query4(conn):
    ### Insert code for query 4 here ###
    cur = conn.cursor()
    Q4_DATE = input("Please enter the date (YYYY-MM-DD): ")

    query = "SELECT narrowed1.id, narrowed1.awardedamount \
            FROM ( \
                SELECT p1.* \
                FROM ( \
                    SELECT * \
                    FROM call c1 \
                    WHERE c1.deadline < %s) as c2 \
                JOIN proposal p1 ON p1.callid = c2.id) as narrowed1 \
            INNER JOIN ( \
                SELECT MAX(p3.awardedamount) as max_req \
                FROM ( \
                    SELECT * \
                    FROM call c3 \
                    WHERE c3.deadline < %s) as c4 \
                JOIN proposal p3 ON p3.callid = c4.id) as narrowed2 \
            ON narrowed1.awardedamount = narrowed2.max_req;"
    data = (Q4_DATE, Q4_DATE)
    cur.execute(query,data)
    results = cur.fetchall()
    for row in results:
        print(row)
    ### end of query 4 code ###
    input("\n==============================\nPress [ENTER] to continue... ")

def run_query5(conn):
    ### Insert code for query 5 here ###
    cur = conn.cursor()
    Q5_AREA = input("Please enter the area of study: ")

    cur.execute(
    "SELECT AVG(a.diff) FROM (SELECT ABS(p1.requestedamount - p1.awardedamount) as diff FROM (SELECT * FROM call c1 WHERE c1.area = %s) as c2 JOIN proposal1 p1 ON p1.callid = c2.id WHERE p1.status = 'awarded') as a;", (Q5_AREA))
    results = cur.fetchall()
    for row in results:
        print(row)
    ### end of query 5 code ###
    input("\n==============================\nPress [ENTER] to continue... ")

def run_query6(conn):
    ### Insert code for query 6 here ###
    cur = conn.cursor()
    Q6_PROPOSALID = input("Please enter the proposalid: ")

    query = "SELECT r4.id AS available_researchers \
            FROM researcher r4 \
            EXCEPT \
            (SELECT a.* \
            FROM (SELECT c1.researcher1 \
            FROM ( \
            SELECT r2.reviewerid \
            FROM review r2 \
            WHERE r2.proposalid = %(iv)s) as conflict1 \
            JOIN conflict c1 ON c1.researcher2 = conflict1.reviewerid \
            UNION \
            SELECT c2.researcher2 \
            FROM (SELECT r3.reviewerid \
            FROM review r3 \
            WHERE r3.proposalid = %(iv)s) as conflict2 \
            JOIN conflict c2 ON c2.researcher1 = conflict2.reviewerid \
            UNION \
            SELECT r1.reviewerid \
            FROM (SELECT r.reviewerid, COUNT(r.id) AS review_count \
            FROM review r \
            WHERE r.submitted = 'false' \
            GROUP BY r.reviewerid) as r1 \
            WHERE r1.review_count >= 3 \
            UNION \
            SELECT r5.reviewerid \
            FROM review r5 WHERE r5.proposalid = %(iv)s) as a) \
            ORDER BY available_researchers;"
    data = {'iv': int(Q6_PROPOSALID)}
    cur.execute(query, data)

    Q6_REVIEWERID = input ("Please select from one of the above available researchers: ")

    query = "INSERT INTO review VALUES(DEFAULT, %s, %s, now() + interval '2 week', false);"
    data = (int(Q6_REVIEWERID), int(Q6_PROPOSALID))
    cur.execute(query, data)
    results = cur.fetchall()
    for row in results:
        print(row)
    ### end of query 6 code ###
    input("\n==============================\nPress [ENTER] to continue... ")

def run_query7(conn):
    ### Insert code for query 7 here ###
    cur = conn.cursor()
    Q7_DATE = input("Please enter the date for the meeting (YYYY-MM-DD): ")
    Q7_ROOM = input("Please enter the room for the meeting: ")
    query = "SELECT * FROM meeting m1 WHERE m1.meetdate = %s AND m1.room = %s;"
    data = (Q7_DATE, int(Q7_ROOM))
    cur.execute(query,data)
    if cur.rowcount>=1:
    	print("The selected room on the specified date is unavailable. Sorry!")
    else:
    	Q7_CALLID1 = input("Please enter the first callid to be discussed: ")
    	query = "SELECT * FROM meeting m2 WHERE m2.meetdate = %(udate)s AND (m2.callid1 = %(cid1)s OR m2.callid2 = %(cid1)s OR m2.callid3 = %(cid1)s;"
    	data = {'udate':Q7_DATE, 'cid1':int(Q7_CALLID1)}
    	cur.execute(query, data)
    	if cur.rowcount>=1:
    		print("Scheduling a discussion on this competition is impossible on this day.")
    	else:
    		Q7_CALLID2 = input("Please enter the second callid to be discussed: ")
    		query = "SELECT * FROM meeting m2 WHERE m2.meetdate = %(udate)s AND (m2.callid1 = %(cid2)s OR m2.callid2 = %(cid2)s OR m2.callid3 = %(cid2)s;"
    		data = {'udate':Q7_DATE, 'cid2':int(Q7_CALLID2)}
    		cur.execute(query, data)
    		if cur.rowcount>=1:
    			print("Scheduling a discussion on this competition is impossible on this day.")
    		else:
    			Q7_CALLID3 = input("Please enter the third callid to be discussed: ")
    			query = "SELECT * FROM meeting m2 WHERE m2.meetdate = %(udate)s AND (m2.callid1 = %(cid3)s OR m2.callid2 = %(cid3)s OR m2.callid3 = %(cid3)s;"
    			data = {'udate':Q7_DATE, 'cid2':int(Q7_CALLID3)}
    			cur.execute(query, data)
    			if cur.rowcount>=1:
    				print("Scheduling a discussion on this competition is impossible on this day.")
    			else:
    				query = "INSERT INTO meeting VALUES (DEFAULT, %s, %s, %s, %s, %s);"
    				data = (int(Q7_ROOM), Q7_DATE, int(Q7_CALLID1), int(Q7_CALLID2), int(Q7_CALLID3))
    				cur.execute(query, data)
    results = cur.fetchall()
    for row in results:
        print(row)
    ### end of query 7 code ###
    input("\n==============================\nPress [ENTER] to continue... ")

def main():
    if not sys.stdin.isatty():
        print("Use 'winpty python main.py' instead")
        return
    else:
        # user1 = input("Username: ")
        # password1 = getpass.getpass("Password: ")
        # host1 = input("Host: ")
        # database1 = input("Database: ")
        user1 = "pta36"
        password1 = "Boeing757!"
        host1 = "cs-db1.csil.sfu.ca"
        database1 = "cmpt354-pta36"
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
            print("What would you like to do? Select: ")
            print("[1] to Create all Tables \n[2] to Drop all Tables\n[3] to Insert all Data\n[4] to Run Queries \n[q] to exit")
            inp = input("\nEnter a Command: ")
            #print(inp)
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
