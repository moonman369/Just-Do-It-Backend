# Generated by Django 5.0.3 on 2024-03-14 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justdoit', '0008_alter_task_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(auto_created=True, default='da9yQ7C6QUlPjOYJHhxgAGgBBtxWdx9XP3cMvMQvTZIomPjKA1', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
