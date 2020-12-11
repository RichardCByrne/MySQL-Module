import os
import pymysql

username = os.getenv("USER")

connection = pymysql.connect(
    host='localhost',
    user=username,
    password='',
    db='Chinook'
)

try:
    with connection.cursor() as cursor:
        sql = "Select * from Artist where Artist.Name = 'Amy Winehouse';"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

