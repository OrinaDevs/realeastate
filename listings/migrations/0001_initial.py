# Generated by Django 5.0.4 on 2024-07-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=200)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('property_type', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Commercial', 'Commercial')], max_length=100)),
                ('amenities', models.TextField()),
                ('image', models.ImageField(upload_to='properties/')),
                ('video_tour', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
