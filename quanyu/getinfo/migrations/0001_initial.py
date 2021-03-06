# Generated by Django 2.2.3 on 2019-08-15 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EveryComponent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='每一条评论的主键')),
                ('hotel_name', models.CharField(max_length=50, verbose_name='酒店名')),
                ('openid', models.CharField(max_length=50, verbose_name='用户唯一标识')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论时间')),
                ('username', models.CharField(max_length=50, verbose_name='用户昵称')),
                ('touxiang', models.CharField(max_length=200, verbose_name='用户头像')),
                ('target', models.CharField(default='0', max_length=50, verbose_name='上级评论的序号')),
            ],
        ),
    ]
