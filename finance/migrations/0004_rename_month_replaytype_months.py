# Generated by Django 3.2.22 on 2023-10-11 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20231011_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replaytype',
            old_name='month',
            new_name='months',
        ),
    ]
