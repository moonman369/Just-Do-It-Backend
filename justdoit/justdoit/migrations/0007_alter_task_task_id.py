# Generated by Django 5.0.3 on 2024-03-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justdoit', '0006_alter_task_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(auto_created=True, default='VGgRimTH9zhaqVsKTYhNnxoWPKsd2KR3gmpyOyNtCnyx78vMmv', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
