# Generated by Django 2.2.3 on 2019-08-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getinfo', '0008_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xiuxianyule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=50, verbose_name='店名')),
                ('star', models.CharField(max_length=10, verbose_name='星级')),
                ('pinfen', models.CharField(max_length=10, verbose_name='评分')),
                ('customer', models.CharField(max_length=10, verbose_name='人均消费')),
                ('location', models.CharField(max_length=50, verbose_name='地址')),
                ('phone', models.CharField(max_length=50, verbose_name='电话')),
                ('open_time', models.CharField(max_length=50, verbose_name='营业时间')),
                ('image', models.CharField(max_length=500, verbose_name='图片')),
            ],
        ),
    ]
