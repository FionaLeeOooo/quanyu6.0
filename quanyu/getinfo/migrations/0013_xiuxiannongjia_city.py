# Generated by Django 2.2.3 on 2019-08-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getinfo', '0012_xiuxiannongjia'),
    ]

    operations = [
        migrations.AddField(
            model_name='xiuxiannongjia',
            name='city',
            field=models.CharField(max_length=50, null=True, verbose_name='城市'),
        ),
    ]
