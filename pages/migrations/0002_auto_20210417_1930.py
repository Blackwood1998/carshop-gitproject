# Generated by Django 3.0.7 on 2021-04-17 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='cerated_date',
            new_name='created_date',
        ),
    ]
