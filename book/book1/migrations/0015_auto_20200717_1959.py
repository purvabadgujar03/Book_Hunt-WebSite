# Generated by Django 3.0.8 on 2020-07-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book1', '0014_auto_20200717_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book2',
            name='Book_genre',
            field=models.CharField(choices=[('1', 'Thriller'), ('2', 'Romance'), ('3', 'Fiction')], default='1', max_length=20),
        ),
    ]