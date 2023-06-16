# Generated by Django 4.1.7 on 2023-06-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_contactusdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=300, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Category_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Image', models.ImageField(blank=True, null=True, upload_to='cartimages')),
            ],
        ),
    ]
