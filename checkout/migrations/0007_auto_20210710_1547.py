# Generated by Django 3.2.4 on 2021-07-10 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_rename_full_name_order_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
    ]
