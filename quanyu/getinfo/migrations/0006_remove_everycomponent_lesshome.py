# Generated by Django 2.2.3 on 2019-08-21 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getinfo', '0005_everycomponent_lesshome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='everycomponent',
            name='lesshome',
        ),
    ]