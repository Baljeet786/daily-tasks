# Generated by Django 4.0.6 on 2022-07-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_user_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='message',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
