# Generated by Django 4.2.7 on 2023-11-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_menuitem_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppetizerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(default=0)),
                ('picture', models.ImageField(null=True, upload_to='menu_images')),
            ],
        ),
        migrations.CreateModel(
            name='DesertItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(default=0)),
                ('picture', models.ImageField(null=True, upload_to='menu_images')),
            ],
        ),
        migrations.CreateModel(
            name='DrinkItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(default=0)),
                ('picture', models.ImageField(null=True, upload_to='menu_images')),
            ],
        ),
        migrations.CreateModel(
            name='EntreeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(default=0)),
                ('picture', models.ImageField(null=True, upload_to='menu_images')),
            ],
        ),
    ]
