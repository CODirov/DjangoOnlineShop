# Generated by Django 3.2.5 on 2021-08-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_alter_coupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='redused_price',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
