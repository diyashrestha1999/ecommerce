# Generated by Django 4.0.5 on 2022-06-27 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='deliver_datee',
            new_name='deliver_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='prcing',
            new_name='pricing',
        ),
    ]
