
from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension



class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0002_products_featured_alter_products_description'),
    ]
    operations = [TrigramExtension()]