# Generated by Django 4.2.7 on 2023-11-13 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_appetizeritem_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreeitem',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
