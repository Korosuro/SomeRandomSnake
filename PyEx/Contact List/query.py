import mysql.connector
conn = mysql.connector.connect(host="localhost", password="+C,+E}>{kk}$dO36", user="root", database="contactlist") 

mycursor = conn.cursor()

query = "DELETE FROM contacts WHERE Nachname='Test'"
mycursor.execute(query)

conn.commit()
