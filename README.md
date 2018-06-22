# Airflow_Demo


##### 1. explain this demo
> This is a test demo, first run the python job, then run the shell script.


##### 2. some userfull script fro add [user/password], delete dag.
> add [user/password]

```
python add_user.py <username> <user@email.com> <password>
```

> delete dag (only for default sqlite airflow.db)
```
python delete_dag.py <dag_id>
```