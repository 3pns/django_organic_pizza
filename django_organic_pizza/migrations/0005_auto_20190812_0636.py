# Generated by Django 2.2.4 on 2019-08-12 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_organic_pizza', '0004_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_type_id',
            new_name='pizza_type',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='pizza_id',
            new_name='pizza',
        ),
    ]
