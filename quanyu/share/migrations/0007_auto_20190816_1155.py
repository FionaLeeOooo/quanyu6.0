# Generated by Django 2.2.3 on 2019-08-16 03:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0006_submmit_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submmit',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='提交时间'),
        ),
    ]
