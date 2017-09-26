import pymysql
db = pymysql.Connect('localhost','root','17600117243','test_db')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
db.close()