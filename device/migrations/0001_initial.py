# Generated by Django 3.0.7 on 2020-06-12 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(blank=True, max_length=48, null=True, verbose_name='机器名称')),
                ('isactive', models.CharField(choices=[('a', '关闭'), ('b', '开启')], default='a', max_length=1, verbose_name='开启或关闭')),
                ('status', models.CharField(choices=[('a', '正常'), ('b', '异常'), ('c', '温度过高'), ('d', '损坏')], default='a', max_length=1, verbose_name='机器状态')),
                ('temperature', models.CharField(default='60', max_length=24, verbose_name='机器温度')),
                ('deviceRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room', verbose_name='机房')),
            ],
            options={
                'verbose_name': '设备',
                'verbose_name_plural': '设备',
            },
        ),
    ]
