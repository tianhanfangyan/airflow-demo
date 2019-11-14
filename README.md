# airflow-demo
job contaions the demo job, first run the python job, then run the shell script.
script contains some useful script, add user and delete dag.


## Getting Started

### add a user

```
python add_user.py <username> <user@email.com> <password>
```

### delete dag (only for default sqlite airflow.db)
```
python delete_dag.py <dag_id>
```