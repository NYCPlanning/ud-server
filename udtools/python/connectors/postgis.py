import os
from dotenv import load_dotenv
from jinjasql import JinjaSql
from psycopg2.extras import DictCursor, NamedTupleCursor
import psycopg2

conn_default = os.environ.get("PG_CONN")

j = JinjaSql(param_style='pyformat')

# make a database connection
def connect(conn_string):
  conn = psycopg2.connect(conn_string, cursor_factory=NamedTupleCursor)
  return conn

# prepare a parameterized query from sql template in a file
def prepare_parameterized_query(p, params):
  with open(p, 'r') as f:
    template = f.read()
    query, bind_params = j.prepare_query(template, params)
    return (query, bind_params)

# prepare parameterized query from sql template in a string
def prepare_parameterized_query_from_string(template, params):
  query, bind_params = j.prepare_query(template, params)
  return (query, bind_params)

def run_query(template, params, conn_string=conn_default):
  (query, bind_params) = prepare_parameterized_query_from_string(template, params)
  conn = connect(conn_string)
  cursor = conn.cursor()
  cursor.execute(query, bind_params)
  results = cursor.fetchall()
  return results
