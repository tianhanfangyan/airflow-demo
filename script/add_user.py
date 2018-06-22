#!/usr/bin/python
#! coding:utf-8

# This little script creates users in an airflow instance so it can be open to the public.
# It gets the password in plain text so be careful where you run it.
# python add_user.py <username> <user@email.com> <password>

import airflow, sys
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

user = PasswordUser(models.User())
user.username = sys.argv[1]
user.email = sys.argv[2]
user.password = sys.argv[3]
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()