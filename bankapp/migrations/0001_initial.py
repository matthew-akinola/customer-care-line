# Generated by Django 4.0.5 on 2022-09-04 00:33

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('company_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('company_name', models.CharField(max_length=20, null=True)),
                ('Address', models.CharField(max_length=20, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Country', django_countries.fields.CountryField(max_length=2)),
                ('Password', models.CharField(max_length=20, null=True)),
                ('is_admin', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Helpline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Branch', models.CharField(max_length=500, null=True)),
                ('City', models.CharField(max_length=500, null=True)),
                ('Country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]