# Generated by Django 3.2.7 on 2021-09-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20210920_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
