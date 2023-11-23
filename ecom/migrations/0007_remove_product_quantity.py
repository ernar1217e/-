
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
