# Generated by Django 3.2.6 on 2021-08-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("help", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="help",
            name="test",
            field=models.CharField(default="", max_length=300),
        ),
    ]
