# Generated by Django 4.1.7 on 2023-02-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=1000)),
                ('source_url', models.CharField(max_length=1000)),
            ],
        ),
    ]