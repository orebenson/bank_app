# Generated by Django 4.1.7 on 2023-05-04 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConversionRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curr1', models.CharField(max_length=3)),
                ('curr2', models.CharField(max_length=3)),
                ('rate', models.IntegerField()),
            ],
        ),
    ]