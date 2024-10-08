# Generated by Django 4.2.5 on 2023-12-20 19:52

import brand.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa_name', models.CharField(max_length=100, verbose_name='Persian Name')),
                ('en_name', models.CharField(max_length=100, verbose_name='English Name')),
                ('brief_explamations', models.TextField()),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Description About Brand')),
                ('country', models.CharField(max_length=100)),
                ('logo_1th', models.ImageField(upload_to=brand.models.BrandLogoImagePath)),
                ('logo_blured', models.ImageField(blank=True, null=True, upload_to=brand.models.BrandLogoBluredImagePath)),
                ('logo_2th', models.ImageField(blank=True, null=True, upload_to=brand.models.BrandLogoSecImagePath)),
                ('logo_slider', models.ImageField(blank=True, null=True, upload_to=brand.models.BrandLogoSliderImagePath)),
                ('number_of_products', models.IntegerField(default=0)),
                ('number_of_employees', models.IntegerField(default=0)),
                ('founded_date', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
