# Generated by Django 4.2 on 2023-05-23 14:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
