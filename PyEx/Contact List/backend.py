import mysql.connector
conn = mysql.connector.connect(host="localhost", password="+C,+E}>{kk}$dO36", user="root", database="contactlist")  


mycursor =  conn.cursor()
#vorname = str(input("Vorname: "))
#nachname = str(input("Nachname: "))
#telnum = int(input("Telefonnummer: "))
#mail = str(input("Mail-Adresse: "))
#adress = str(input("Wohnort: "))

def data_input(vorname, nachname, telnum, mail, adress):
    sql = "INSERT INTO contacts (Nachname, Vorname, Telefonnummer, Mail, Wohnort) VALUES (%s, %s, %s, %s, %s)"
    data = (nachname, vorname, telnum, mail, adress)

    mycursor.execute(sql, data)
    conn.commit()

    mycursor.close()
    conn.close()

    print("Success")


def data_output(Vorname, Nachname, Telefonnummer, Mail, Wohnort):
    query = "SELECT * FROM contacts"
    mycursor.execute(query)

    data = mycursor.fetchall()

    return data


    