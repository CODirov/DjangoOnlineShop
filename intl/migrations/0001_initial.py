# Generated by Django 3.2.5 on 2021-08-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Fullname')),
                ('age', models.IntegerField(verbose_name='Age')),
            ],
        ),
    ]
