#!/usr/bin/python
#! coding:utf-8

# when you use it, please careful.
#python delete_dag.py <dag_id>

import sqlite3
import sys

conn = sqlite3.connect('airflow.db')
c = conn.cursor()

dag_input = sys.argv[1]

for t in ["xcom", "task_instance", "sla_miss", "log", "job", "dag_run", "dag" ]:
    query = "delete from {} where dag_id='{}'".format(t, dag_input)
    print query
    c.execute(query)

conn.commit()
conn.close()