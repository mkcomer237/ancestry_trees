


def sql_tree_range(starttree, endtree):
  from sqlalchemy import *

  db = create_engine("postgresql+psycopg2://tableau:LineGraphMinionChart@10.211.26.100:5439/ancestry") 
  db_con=db.connect()
  
  query = "select * from a.max_prehint_nodes where treeid between 76063214 and 76064214"
  run = db_con.execute(query)

  rows = run.fetchall()

  return rows


output = sql_tree_range(1,1)

for row in output:
  print row
