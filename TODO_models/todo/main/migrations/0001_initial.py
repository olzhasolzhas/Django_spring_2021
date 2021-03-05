# Generated by Django 3.1.7 on 2021-03-05 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.date.today)),
                ('due_on', models.DateTimeField(default=datetime.date(2021, 3, 8))),
                ('user', models.TextField(verbose_name='Name')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]