# Generated by Django 2.2.4 on 2019-08-19 16:30

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20190817_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=13, null=True, region='IN', unique=True),
        ),
    ]