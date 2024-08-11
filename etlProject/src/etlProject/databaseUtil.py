import psycopg2
import json
import yaml

def getDatabaseConn(database):
    with open('config.json') as config_file:
        data = json.load(config_file)['stockprediction']['properties']['dbconnection'][database]
        database = data['database']
        user = data['user']
        host = data['host']
        password = data['password']
        port = data['port']

    conn = psycopg2.connect(database=database,
                        user=user,
                        host=host,
                        password=password,
                        port=port)

    return conn

def executeDatabaseStatement(database , statement):
    conn = getDatabaseConn(database)
    cur = conn.cursor()
    conn.autocommit = True
    with open('queries.yml', 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        stmt = data[statement]
        cur.execute(stmt)
        cur.close()
        conn.close()

