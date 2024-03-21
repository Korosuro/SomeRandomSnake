import mysql.connector
conn = mysql.connector.connect(host="localhost", password="+C,+E}>{kk}$dO36", user="root", database="contactlist")

mycursor =  conn.cursor()
vorname = str(input("Vorname: "))
nachname = str(input("Nachname: "))
telnum = int(input("Telefonnummer: "))
mail = str(input("Mail-Adresse: "))

sql = "INSERT INTO contacts (Nachname, Vorname, Telefonnummer, Mail) VALUES (%s, %s, %s, %s)"
data = (vorname, nachname, telnum, mail)

mycursor.execute(sql, data)
conn.commit()

mycursor.close()
conn.close()

print("Success")