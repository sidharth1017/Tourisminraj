# Generated by Django 3.2.3 on 2022-04-24 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0013_rename_comment_comment_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
    ]
