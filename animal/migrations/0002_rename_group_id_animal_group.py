# Generated by Django 3.2.5 on 2021-07-28 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='group_id',
            new_name='group',
        ),
    ]
