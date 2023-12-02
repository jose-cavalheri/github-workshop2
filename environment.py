import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE your_table_name (
        column1 datatype,
        column2 datatype,
        column3 datatype
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()