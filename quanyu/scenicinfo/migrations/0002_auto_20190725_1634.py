# Generated by Django 2.2.3 on 2019-07-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenicinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenic',
            name='labels',
            field=models.CharField(max_length=50, verbose_name='标签'),
        ),
    ]
