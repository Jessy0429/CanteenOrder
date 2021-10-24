import pymysql


class MyDB():
    def __init__(self, user, password, db_name):
        self.DB_conn = pymysql.connect(host='127.0.0.1', port=3306, user=user, password=password, db=db_name)
        print(self.DB_conn)

    def update_DB(self, sql):
        try:
            with self.DB_conn.cursor() as cursor:
                cursor.execute(sql)
            self.DB_conn.commit()
            return True
        except Exception as e:
            self.DB_conn.rollback()
            print(e)
            return False

    def get_data_DB(self, sql):
        try:
            with self.DB_conn.cursor() as cursor:
                cursor.execute(sql)
                res = cursor.fetchall()
            # print(res)
            return res
        except Exception as e:
            print(e)
            return False

db = MyDB('root', 'mysql', 'canteenorder')
if __name__ == '__main__':
    db = MyDB('root', 'mysql', 'canteenorder')
    # db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='mysql', db='canteenorder')
    userID = 0
    getUserInfo_sql = "select * from user where userID = '{}'".format(userID)


    userinfo = db.get_data_DB(getUserInfo_sql)
    if userinfo:
        for data in userinfo:
            print(data)
