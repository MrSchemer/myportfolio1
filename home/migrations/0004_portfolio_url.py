# Generated by Django 5.1.3 on 2024-11-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_portfolio_catagory_alter_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(null=True),
        ),
    ]