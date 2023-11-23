
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecom", "0007_remove_product_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="profile_pic",
            field=models.ImageField(
                null=True, upload_to="profile_pic/CustomerProfilePic/"
            ),
        ),
    ]
