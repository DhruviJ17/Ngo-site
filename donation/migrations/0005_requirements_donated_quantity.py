# Generated by Django 3.1.1 on 2020-09-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0004_auto_20200928_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirements',
            name='donated_quantity',
            field=models.IntegerField(null=True),
        ),
    ]