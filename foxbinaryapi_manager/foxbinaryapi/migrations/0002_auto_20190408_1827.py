# Generated by Django 2.2 on 2019-04-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foxbinaryapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickhistory',
            old_name='created_at',
            new_name='accessed_at',
        ),
        migrations.RenameField(
            model_name='tickhistory',
            old_name='prices',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='tickhistory',
            old_name='times',
            new_name='time',
        ),
    ]
