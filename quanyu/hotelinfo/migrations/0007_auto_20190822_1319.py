# Generated by Django 2.2.3 on 2019-08-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelinfo', '0006_auto_20190822_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelinfo',
            name='boss_name',
            field=models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='商家名'),
        ),
        migrations.AddField(
            model_name='hotelinfo',
            name='left_home',
            field=models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='剩余房间数量'),
        ),
    ]