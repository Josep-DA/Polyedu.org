# Generated by Django 4.2.2 on 2023-09-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polyedu", "0013_alter_exercice_desc_forumpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="desc",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]