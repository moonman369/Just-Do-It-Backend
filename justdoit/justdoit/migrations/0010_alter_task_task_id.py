# Generated by Django 5.0.3 on 2024-03-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justdoit', '0009_alter_task_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(auto_created=True, default='s5N5MyKvtAAYWQBwIIyoabfStxc6m5KBWuB6JkCAhNBpcdsyA9', max_length=50, primary_key=True, serialize=False),
        ),
    ]
