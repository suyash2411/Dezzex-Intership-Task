# Generated by Django 3.0.8 on 2020-07-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_signup_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='img',
            field=models.ImageField(default='', upload_to='media/log/images'),
        ),
    ]
