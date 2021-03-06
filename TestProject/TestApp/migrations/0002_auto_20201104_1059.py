# Generated by Django 3.0.2 on 2020-11-04 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=100)),
                ('position_name', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('fire_date', models.DateField(default=None)),
                ('salary', models.IntegerField()),
                ('fraction', models.IntegerField()),
                ('base', models.IntegerField()),
                ('advance', models.IntegerField()),
                ('by_hours', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
