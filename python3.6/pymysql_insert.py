import pymysql
db = pymysql.Connect('localhost','root','17600117243','test_db')
cursor = db.cursor()
#sql = """INSERT INTO ENPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
#VALUES('mac','molan',20,'m',2000)"""
#try:
#   cursor.execute(sql)
#   db.commit()
#except:
#    db.rollback()
#db.close()
# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()