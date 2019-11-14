import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

# default_args
default_args = {
    'owner': 'tianhanfangyan',                              # owner
    'depends_on_past': False,
    'start_date': datetime.today() - timedelta(days=1),     # job run start time
    'retries': 1,                                            # retry once
    'retry_delay': timedelta(minutes=5),                     # restry after five minutes
}

# this is my job's workdir
WORK_DIR = "./"

# dag
dag = DAG('hello_world', default_args=default_args, schedule_interval="@daily")

# templated_command
templated_command = "cd {work_dir}; python hello_world.py; bash run.sh;".format(work_dir=WORK_DIR)

# task
task = BashOperator(
    task_id='daily_hello_world',
    bash_command=templated_command,
    dag=dag
)

