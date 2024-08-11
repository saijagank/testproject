import psycopg2
import json
import databaseUtil
import yaml

conn = databaseUtil.getDatabaseConn("dev")
cur  = conn.cursor()
conn.autocommit = True

with open('queries.yml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)
    stmt = data['TestInsertstatement']
    cur.execute(stmt)
    cur.close()
    conn.close()