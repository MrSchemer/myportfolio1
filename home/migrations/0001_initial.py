# Generated by Django 5.1.3 on 2024-11-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=122, unique=True)),
                ('catagory', models.CharField(choices=[('web', 'Web Design'), ('app', 'App Design'), ('graphic', 'Graphic Design'), ('video', 'Video Editing'), ('photo', 'Photography'), ('Education', 'Education'), ('other', 'others')], default='web', max_length=122)),
                ('image', models.ImageField(upload_to='images/blog')),
                ('slagan', models.CharField(max_length=122)),
                ('title', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=122, unique=True)),
                ('catagory', models.CharField(choices=[('web', 'Web Design'), ('app', 'App Design'), ('graphic', 'Graphic Design'), ('video', 'Video Editing'), ('photo', 'Photography'), ('Education', 'Education'), ('other', 'others')], default='web', max_length=122)),
                ('image', models.ImageField(upload_to='images/portfolio')),
                ('slogan', models.CharField(max_length=122)),
                ('title', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
