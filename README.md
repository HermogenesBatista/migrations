# migrations
Minimal package to manage migrations with old system

## Install

Clone this repository and install with pip:   
```pip install -U .```

## How to use

```shell
migrations -h
usage: migrations [-h] [-t CONNECTION_TYPE] [-u USER] [-p PASSWORD]
                  [-db DATABASE] [-H HOST] [--port PORT] [--charset CHARSET]
                  [-mg MIGRATIONS_PATH]

Command line to manage database transformations (migrations)

optional arguments:
  -h, --help            show this help message and exit
  -t CONNECTION_TYPE, --connection_type CONNECTION_TYPE
                        Type of connection (such as mysql, postegresql) you
                        want to connect
  -u USER, --user USER  User used on connection with database
  -p PASSWORD, --password PASSWORD
                        User used on connection with database
  -db DATABASE, --database DATABASE
                        Database used on connection with database
  -H HOST, --host HOST  Host used on connection with database
  --port PORT           Port used on connection with database
  --charset CHARSET     Charset of connection with database
  -mg MIGRATIONS_PATH, --migrations_path MIGRATIONS_PATH
                        Absolute path with files to execute migrations```   

```
migrations -t mysql -u root -p 123456 -db teste -H localhost --port 3306 -mg `pwd`/migrations```
