# Generated by Django 3.2.8 on 2021-10-30 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music_data", "0005_remove_external_fks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="parent_id",
            field=models.IntegerField(default=None, null=True),
        ),
    ]
