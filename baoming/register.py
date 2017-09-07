 #!/usr/bin/env python3
#-*- encoding: utf-8 -*-

import sys
import argparse
import pymysql
import hashlib

g_db = {"host":"127.0.0.1", "user":"root", "passwd":"", "db":"db_user", "charset":"utf8", "cursorclass":pymysql.cursors.DictCursor}

def get_passwd(passwd):
    m = hashlib.md5()
    m.update(passwd.encode("utf8"))
    v = m.hexdigest()
    m = hashlib.md5()
    m.update((passwd+"GN100"+v).encode("utf8"))
    v = m.hexdigest()
    return v

def register_one(cursor, phone):
    sql = "select * from t_user_mobile where mobile='{mobile}'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row:
        return 0
    sql = "insert ignore into t_user set name='测试-{phone}', password='{passwd}', gender=1, status=1, type=7, verify_status=65537, thumb_big='1,0266abcef015', thumb_med='7,0267cfa88872', thumb_small='5,0268d69726e7', register_ip='2071236780'".format(phone=phone, passwd=get_passwd(str(phone)))
    #sql = "insert ignore into t_user set name='测试-{phone}', password='{passwd}', gender=1, status=1, type=7, verify_status=65537, source=0, thumb_big='1,0266abcef015', thumb_med='7,0267cfa88872', thumb_small='5,0268d69726e7', register_ip='2071236780'".format(phone=phone, passwd=get_passwd(str(phone)))
    cursor.execute(sql)
    user_id = cursor.lastrowid
    sql = "insert into t_user_mobile set fk_user={user_id}, mobile='{phone}', supplier='中国电信', province='北京', city='北京'".format(user_id=user_id, phone=phone)
    try:
        cursor.execute(sql)
        return 1
    except Exception:
        sql = "delete from t_user where pk_user={}".format(user_id)
        cursor.execute(sql)
        return 0

def register(num, start):
    conn = pymysql.connect(**g_db)
    conn.autocommit(True)
    cursor = conn.cursor()
    success = 0
    for i in range(num):
        success += register_one(cursor, start+i)
    cursor.close()
    conn.close()
    print("success={}".format(success))

if "__main__" == __name__:
    parser = argparse.ArgumentParser(description="批量注册新学生")
    parser.add_argument("num", type=int, help="学生个数")
    parser.add_argument("start_phone", type=int, help="开始手机号")
    args = parser.parse_args()
    register(args.num, args.start_phone)

