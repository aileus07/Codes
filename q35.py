import mysql.connector as ms

mydb = ms.connect(
    host = 'localhost',
    user = 'root',
    passwd = '77289874'
)
cur = mydb.cursor()
query = "UPDATE fees SET STATUS PAID WHERE amount >= 20000;"