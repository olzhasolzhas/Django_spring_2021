from django.db import models
import datetime


class Task(models.Model):
    created = models.DateTimeField(default=datetime.datetime.today)
    due_on = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=2))
    user = models.TextField('Name')
    status = models.BooleanField(default=False)
