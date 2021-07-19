# Generated by Django 3.2.5 on 2021-07-19 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210719_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='cupon',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]