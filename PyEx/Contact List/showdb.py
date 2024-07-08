import mysql.connector
conn = mysql.connector.connect(host="localhost", password="+C,+E}>{kk}$dO36", user="root", database="contactlist")  
from prettytable import PrettyTable

mycursor = conn.cursor()

query = "SELECT Nachname FROM contacts"
mycursor.execute(query)

rows = mycursor.fetchall()

column_names = [column[0] for column in mycursor.description]

table = PrettyTable(column_names)

for row in rows:
    table.add_row(row)

print(table)






