# database connection

# making connnection with database
import mysql.connector # importing mysql connector pakcage

mydb = mysql.connector.connect(host="localhost", user = "root", passwd = "12345")

# creating an object or var to store all databases by fun cursor()
data = mydb.cursor() # cursor() will give access to all databases 

data.execute("use hamza") # execute() use to run quries
data.execute("select *from data") # here data is table of database hamza

print("data by fetch()")
# use fetch() to fetch data automcticaly
result = data.fetchall()
print(result)
print()

print("data by loop")
# fetching data from database hamza
for i in result:
    print(i)