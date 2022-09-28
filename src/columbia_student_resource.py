import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get("root")
        pw = os.environ.get("Zzjsqmm2022!")
        h = os.environ.get("ZZJ")

        # conn = pymysql.connect(
        #     user=usr,
        #     password=pw,
        #     host=h,
        #     cursorclass=pymysql.cursors.DictCursor,
        #     autocommit=True
        # )
        conn = pymysql.connect(
            host="localhost",
            #port=3306,
            user="root",
            password="Zzjsqmm2022!",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True)
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

