# Generated by Django 4.2.6 on 2023-10-31 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_pet_adopted'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='dt_request',
            field=models.DateField(auto_now=True),
        ),
    ]
