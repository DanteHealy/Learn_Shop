# Generated by Django 3.2.4 on 2021-07-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='enrolled',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=6),
            preserve_default=False,
        ),
    ]
