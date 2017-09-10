# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import glob


class BaseConnector(object):
    migration_table = 'migrations'
    connection = None
    sql_create_migration_table = '''
    CREATE TABLE IF NOT EXISTS `migrations` (
      `id` INT NOT NULL AUTO_INCREMENT,
      `filename` VARCHAR(100) NOT NULL,
      PRIMARY KEY (`id`));
    '''
    sql_check_applied = '''
    SELECT * FROM migrations WHERE filename=%s'''
    sql_insert_migration_applied = '''
    INSERT INTO migrations(filename) VALUES (%s)'''

    def __init__(self, user, password, database, host='localhost',
                 port=3306, charset='utf8mb4'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port
        self.charset = charset
        self.create_migration_table()

    def connect(self):
        raise NotImplementedError("Connect not implemented")

    def create_migration_table(self):
        self.connect()
        self.execute(self.sql_create_migration_table)

    def execute(self, sql, must_return=False, *args):
        raise NotImplementedError("Execute queries was not implemented")

    def manage_migrations_not_applied(self, filepath):
        files = glob.glob("{}/*.sql".format(filepath))
        for file in files:
            filename = file.split('/')[-1].replace('.sql', '')
            with open(file, 'r') as reader:
                # Execute it only with trusted code
                content = reader.read()
                if not self.check_if_already_applied(filename):
                    self.apply_migrations(content, filename)
                else:
                    # raise Exception("Migration already applied")
                    continue

    def check_if_already_applied(self, filename):
        result = self.execute(
            self.sql_check_applied, True, filename)
        return result

    def apply_migrations(self, content, filename):
        print 'Applying migration: {}'.format(filename)
        self.execute(content)
        self.execute(self.sql_insert_migration_applied, False, filename)
