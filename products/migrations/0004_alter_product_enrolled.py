# Generated by Django 3.2.4 on 2021-07-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_enrolled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='enrolled',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]