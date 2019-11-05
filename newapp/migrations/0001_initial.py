# Generated by Django 2.2.2 on 2019-11-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empregmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=10)),
                ('emp_address', models.CharField(max_length=10)),
                ('emp_gender', models.CharField(max_length=10)),
                ('emp_number', models.CharField(max_length=10)),
                ('emp_salary', models.CharField(max_length=30)),
                ('empemail', models.CharField(max_length=20)),
                ('emp_photo', models.CharField(max_length=100)),
                ('emp_joindate', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'empreg',
            },
        ),
    ]