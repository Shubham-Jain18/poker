# Generated by Django 5.1.5 on 2025-01-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poker_tournament", "0009_alter_bot_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testmatch",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
