import mysql
import mysql.connector
cnn = mysql.connector.connect(
            host= "localhost",
            user="root",
            passwd="Password",
            database="world"
)


cur = cnn.cursor()
cur.execute("SELECT * FROM titanic_real.titanic_lista1 WHERE Survived = '1'")
datos = cur.fetchall()

for fila in datos:
    print(fila)


#print(cnn)



        