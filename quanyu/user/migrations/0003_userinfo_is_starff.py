# Generated by Django 2.2.3 on 2019-08-08 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190724_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_starff',
            field=models.CharField(default=0, max_length=1, verbose_name='是否为管理员'),
        ),
    ]
