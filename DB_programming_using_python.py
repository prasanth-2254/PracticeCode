import mysql.connector
conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database='prasanth.db', auth_plugin='mysql_native_password')
if conn.is_connected():
    print('Successfully connected to the database')