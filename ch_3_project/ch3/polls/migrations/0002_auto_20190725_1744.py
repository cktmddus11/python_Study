# Generated by Django 2.2.3 on 2019-07-25 08:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='choice',
            managers=[
                ('DoesNotExist', django.db.models.manager.Manager()),
            ],
        ),
    ]
