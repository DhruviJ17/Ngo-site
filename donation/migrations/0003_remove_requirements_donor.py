# Generated by Django 3.1.1 on 2020-09-27 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_donated_requirements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirements',
            name='donor',
        ),
    ]