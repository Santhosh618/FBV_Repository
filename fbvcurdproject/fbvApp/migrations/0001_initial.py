# Generated by Django 2.2.4 on 2019-08-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ename', models.CharField(max_length=30)),
                ('Eid', models.IntegerField()),
                ('Epostion', models.CharField(max_length=30)),
                ('Eaddress', models.CharField(max_length=30)),
            ],
        ),
    ]
