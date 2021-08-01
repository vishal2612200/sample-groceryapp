# Generated by Django 2.2.23 on 2021-08-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('quantity', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('NOT AVAILABLE', 'NOT AVAILABLE'), ('BOUGHT', 'BOUGHT')], default='PENDING', max_length=100)),
                ('added_date', models.DateField()),
            ],
        ),
    ]
