# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pymysql.cursors
from .base import BaseConnector


class MysqlConnector(BaseConnector):

    def __init__(self, user, password, database, host='localhost',
                 port=3306, charset='utf8mb4'):
        super(MysqlConnector, self).__init__(user, password, database,
                                             host=host,
                                             port=port, charset=charset)

    def connect(self):
        if not self.connection:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.database,
                charset=self.charset,
                cursorclass=pymysql.cursors.DictCursor)
        return self.connection

    def execute(self, sql, must_return=False, *args):
        connection = self.connect()
        sql_minor = ""
        try:
            with connection.cursor() as cursor:
                try:
                    part_of_sql = sql.decode('utf-8').split(';')
                except:
                    part_of_sql = sql.split(';')
                for sql_minor in part_of_sql:
                    sql_minor = sql_minor.strip()
                    if sql_minor:
                        cursor.execute(sql_minor, args=args)
                        if must_return:
                            return cursor.fetchone()
            connection.commit()
        except Exception as e:
            print("-----")
            print("Minor part of sql: ")
            print(sql_minor)
            raise e
        finally:
            connection.close()
            self.connection = None
