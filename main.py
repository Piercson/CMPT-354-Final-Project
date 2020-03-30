import psycopg2
import time
import datetime
from datetime import date
def insert_data(conn):
    entry_count = 0;
    print("INSERTING DATA...")
    connection = conn
    inset_id = None
    try:
        cursor = connection.cursor()
        #INSERT reseacher TABLE
        sql = """INSERT INTO researcher(id, firstname, lastname, email, organization)
                    VALUES (%s,%s,%s,%s,%s)"""
        insert_researcher_list = [
            (1,'Andrea','Le','andreale@sfu.ca','SFU'),
            (2,'Lori','Hoknes','LoriH@sfu.ca','SFU'),
            (3, 'Jeffery', 'Liam', 'jli@ubc.ca','UBC'),
            (4, 'Owen', 'Yuler', 'owyu@uofs', 'UofS'),
            (5, 'Thomas', 'John', 'ToJo@ubc.ca','UBC')
        ]
        print('insert researchers')
        cursor.executemany(sql,insert_researcher_list)
        #Print the researchers
        testsql = "SELECT * FROM researcher"
        cursor.execute(testsql)
        rows = cursor.fetchall()
        print("The number of parts: ", cursor.rowcount)
        entry_count += cursor.rowcount
        print("Printing querie")
        for row in rows:
            print(row)
        # INSERT call TABLE
        sql = """INSERT INTO call(id, title, deadline, description , area , status)
                    VALUES (%s,%s,%s,%s,%s,%s)"""
        today_date = date.today()
        insert_call_list = [
            (1, 'John student fund: looking for applicants',
                today_date + datetime.timedelta(weeks = 3) , 'NULL', 'Biology', 'closed'),
            (2, 'Looking for reseach of shortest paths',
                today_date + datetime.timedelta(weeks = 2) , 'NULL', 'Computer Science', 'open'),
            (3, 'Research for COVID-19',
                today_date + datetime.timedelta(weeks = 1) , 'NULL', 'Mircobiology', 'open'),
            (4, 'Need Research for Classical Conditioning',
                today_date + datetime.timedelta(weeks = 1) , 'NULL', 'Psycology', 'cancelled'),
            (5, 'Research Jacobi Iterations',
                today_date + datetime.timedelta(weeks = 2) , 'NULL', 'MATH', 'paused')
        ]
        cursor.executemany(sql,insert_call_list)
        sql = """SELECT * FROM call"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("The number of parts: ", cursor.rowcount)
        entry_count += cursor.rowcount
        print("Printing querie")
        for row in rows:
            print(row)
        #INSERT proposal TABLE
        print("insert proposal")
        sql = """INSERT INTO proposal(id, callid, pi, status , amount)
                    VALUES (%s,%s,%s,%s,%s)"""
        insert_proposal_list = [
            (1,1,1,'awarded',3600),
            (2,3,4,'submitted',0),
            (3,5,2,'denied',0)
        ]
        cursor.executemany(sql,insert_proposal_list)
        sql = """SELECT * FROM proposal"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("The number of parts: ", cursor.rowcount)
        entry_count += cursor.rowcount
        print("Printing querie")
        for row in rows:
            print(row)
        #INSERT collaborator TABLE
        print("insert collaborator")
        sql = """INSERT INTO collaborator(id, proposalid, researcherid, ispi)
                    VALUES (%s,%s,%s,%s)"""
        insert_collaborator_list = [
            (1,2,4,True)
        ]
        cursor.executemany(sql,insert_collaborator_list)
        sql = """SELECT * FROM collaborator"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("The number of parts: ", cursor.rowcount)
        entry_count += cursor.rowcount
        print("Printing querie")
        for row in rows:
            print(row)
        #INSERT conflict TABLE
        sql = """INSERT INTO conflict(id, researcher1, researcher2, reason, expiry)
                    VALUES (%s,%s,%s,%s,%s)"""
        insert_conflict_list = [
            (1,4,3,"Are collaborators", today_date + datetime.timedelta(weeks = 12))
        ]
        cursor.executemany(sql,insert_conflict_list)
        sql = """SELECT * FROM conflict"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("The number of parts: ", cursor.rowcount)
        entry_count += cursor.rowcount
        print("Printing querie")
        for row in rows:
            print(row)
        #INSERT review TABLE
        sql = """INSERT INTO review(id, reviewerid, proposalid , deadline, submitted )
                    VALUES (%s,%s,%s,%s,%s)"""
        insert_review_list = [
            (1,5,2, today_date + datetime.timedelta(weeks = 2), True)
        ]
        cursor.executemany(sql,insert_review_list)
        sql = """SELECT * FROM review"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("The number of parts: ", cursor.rowcount)
        entry_count += cursor.rowcount
        print("Printing querie")
        for row in rows:
            print(row)
        #-------------------------------------
        print("amount of entries:", entry_count)
        connection.commit()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    try:
        connection = psycopg2.connect(user = "pta36",
                                      password = "Boeing757!",
                                      host = "cs-db1.csil.sfu.ca",
                                      database = "cmpt354-pta36")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
        insert_data(connection);

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
