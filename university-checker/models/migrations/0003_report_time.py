# Generated by Django 4.1.5 on 2023-02-09 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("models", "0002_service_abbreviation"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="time",
            field=models.CharField(max_length=200, null=True, verbose_name="time"),
        ),
    ]
