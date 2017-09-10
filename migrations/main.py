# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import argparse
import importlib
import os


def execute_command_line():
    parser = argparse.ArgumentParser(
        description='Command line to manage database transformations (migrations)')
    parser.add_argument('-t', '--connection_type', type=str,
                        help='Type of connection (such as mysql, postegresql)'
                             ' you want to connect')
    parser.add_argument('-u', '--user', type=str,
                        help='User used on connection with database')
    parser.add_argument('-p', '--password', type=str,
                        help='User used on connection with database')
    parser.add_argument('-db', '--database', type=str,
                        help='Database used on connection with database')
    parser.add_argument('-H', '--host', type=str, default='localhost',
                        help='Host used on connection with database')
    parser.add_argument('--port', type=int,
                        help='Port used on connection with database')
    parser.add_argument('--charset', type=str, default='utf8mb4',
                        help='Charset of connection with database')
    parser.add_argument('-mg', '--migrations_path', type=str,
                        help='Absolute path with files to execute migrations')

    args = parser.parse_args()
    connection_type = args.connection_type

    if not connection_type:
        raise Exception("You must set one connection type")
    try:
        module = importlib.import_module("{}.{}".format(
            'migrations.connection', connection_type.lower()
        ))
        ManagerClass = getattr(module, "{}Connector".format(
            connection_type.capitalize()))
    except ImportError as e:
        raise Exception("Connector not found")

    tmp_config = dict(
        user=args.user,
        password=args.password,
        database=args.database,
        host=args.host,
        port=args.port,
        charset=args.charset
    )

    required = ['user', 'password', 'database']

    # remove empty parameters
    config = {}
    for key, value in tmp_config.iteritems():
        if key in required and not value:
            raise Exception("You must set value for: '{}'".format(key))

        if value:
            config[key] = value

    migration_path = args.migrations_path or os.getcwd()

    manager = ManagerClass(**config)

    manager.manage_migrations_not_applied(migration_path)

if __name__ == '__main__':
    execute_command_line()
