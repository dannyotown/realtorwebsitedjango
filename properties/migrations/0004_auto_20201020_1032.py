# Generated by Django 3.1.2 on 2020-10-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0003_auto_20201019_1806"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name="PropertySerializer",
        ),
    ]