# Generated by Django 4.2.4 on 2023-08-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quoteapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
