# Generated by Django 3.0.7 on 2020-06-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(blank=True, max_length=48, null=True)),
                ('room_status', models.CharField(choices=[('a', '正常'), ('b', '异常'), ('c', '停电'), ('d', '着火')], default='a', max_length=1)),
            ],
        ),
    ]
