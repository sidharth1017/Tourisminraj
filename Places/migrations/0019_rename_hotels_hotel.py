# Generated by Django 3.2.3 on 2022-04-24 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0018_hotels'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotels',
            new_name='Hotel',
        ),
    ]