# Generated by Django 2.2.2 on 2019-11-02 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='empanotherdatamodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=10)),
                ('emp_color', models.CharField(max_length=10)),
                ('emp_height', models.IntegerField(max_length=5)),
                ('emp_ofc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'empanotherdata',
            },
        ),
    ]
