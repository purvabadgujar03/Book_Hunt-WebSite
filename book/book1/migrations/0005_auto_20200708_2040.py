# Generated by Django 3.0.8 on 2020-07-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book1', '0004_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
