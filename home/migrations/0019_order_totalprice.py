# Generated by Django 3.2.3 on 2021-09-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210926_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalPrice',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
