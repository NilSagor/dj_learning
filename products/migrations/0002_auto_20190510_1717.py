# Generated by Django 2.2.1 on 2019-05-10 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptin',
            new_name='description',
        ),
    ]
