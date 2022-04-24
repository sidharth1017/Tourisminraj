# Generated by Django 3.2.3 on 2022-04-20 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0007_auto_20220420_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='category',
            field=models.CharField(choices=[('Forts', 'Forts'), ('Wildlife', 'Wildlife'), ('Palaces', 'Palaces'), ('Lakes', 'Lakes'), ('Museum', 'Museum'), ('Religious Places', 'Religious Places'), ('Others', 'Others')], default=1, max_length=30),
        ),
    ]
