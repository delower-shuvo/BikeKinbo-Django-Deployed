# Generated by Django 4.2.5 on 2024-01-22 18:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_phone_number', models.CharField(max_length=255)),
                ('company_address', models.CharField(max_length=100)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_fax', models.CharField(max_length=255)),
                ('facebook_link', models.CharField(max_length=150)),
                ('twitter_link', models.CharField(max_length=150)),
                ('instagram_link', models.CharField(max_length=150)),
                ('youtube_link', models.CharField(max_length=150)),
                ('linkedin_link', models.CharField(max_length=150)),
                ('index_banner_heading', models.CharField(max_length=200)),
                ('index_banner_sub_heading', models.CharField(max_length=200)),
                ('services_heading', models.CharField(max_length=150)),
                ('services_text', ckeditor.fields.RichTextField()),
                ('services_video_link', models.CharField(max_length=250)),
                ('footer_company_text', ckeditor.fields.RichTextField()),
                ('about_us_text', ckeditor.fields.RichTextField()),
                ('about_us_photo_1', models.ImageField(blank=True, upload_to='Photos/about_us/%y/%m/%d')),
                ('about_us_photo_2', models.ImageField(blank=True, upload_to='Photos/about_us/%y/%m/%d')),
                ('about_us_photo_3', models.ImageField(blank=True, upload_to='Photos/about_us/%y/%m/%d')),
                ('about_us_photo_4', models.ImageField(blank=True, upload_to='Photos/about_us/%y/%m/%d')),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/teams/%y/%m/%d')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
