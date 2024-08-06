import psycopg2
# Connect to the PostgreSQL database
conn = psycopg2.connect(database="lessons", user="postgres", password="Ghjcnj202", host="localhost", port="5432")
# Create a cursor object to execute SQL queries
#cur = conn.cursor()
# Execute a SELECT query to retrieve data
#cur.execute("SELECT name FROM monday ")
# Fetch all the rows returned by the query
#rows = cur.fetchall()
# Iterate over the rows and print the data
# c=0
# for row in rows:
#     c+=1
#     print(c,"Name: "+str(row)[2:-3])
# curt = conn.cursor()
# curt.execute("SELECT id FROM monday ")
# rows = curt.fetchall()
# c=0
# for row in rows:
#     c+=1
#     print(c,"id: "+str(row)[1:-2])
cu = conn.cursor()
cu.execute("SELECT id FROM monday")
rows = cu.fetchall()
c=0
for row in rows:
    print(c,"id: "+str(row))
#create new table
#cur.execute("CREATE TABLE students (id serial PRIMARY KEY, name varchar, age integer)")
#insert data
#cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("John", 25))
#commit
conn.commit()

# Close the cursor and the connection
#cur.close()
#curt.close()
cu.close()
conn.close()