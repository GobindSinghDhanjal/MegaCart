# Generated by Django 3.2.3 on 2021-09-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_dealsoftheday_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
