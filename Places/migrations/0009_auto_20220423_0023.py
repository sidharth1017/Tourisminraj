# Generated by Django 3.2.3 on 2022-04-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0008_alter_touristspot_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='parking',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='touristspot',
            name='images',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
