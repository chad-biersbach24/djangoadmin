# Generated by Django 3.1.3 on 2021-10-28 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataPurge', models.BooleanField(default=False)),
                ('dataReport', models.BooleanField(default=False)),
                ('dataRetrival', models.BooleanField(default=False)),
                ('radio1', models.BooleanField(default=False)),
                ('radio2', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(default='First name not given', max_length=300)),
                ('mName', models.CharField(default='Middle name not given', max_length=300)),
                ('lName', models.CharField(default='Last name not given', max_length=300)),
                ('SSN', models.DecimalField(decimal_places=0, default=0, max_digits=4)),
                ('phoneInfo', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('emailInfo', models.EmailField(default='No email provided', max_length=100)),
                ('address', models.CharField(default='no address', max_length=300)),
                ('address2', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(default='no city', max_length=300)),
                ('zip', models.DecimalField(blank=True, decimal_places=0, default='no zip', max_digits=5, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('dataMethods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.datamethod')),
            ],
        ),
    ]
