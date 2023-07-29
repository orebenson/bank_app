# Generated by Django 4.1.7 on 2023-05-03 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashTransfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('direction', models.CharField(choices=[('Received From', 'Received'), ('Sent To', 'Sent')], max_length=20)),
                ('other_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfers_other_users', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CashRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('other_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests_other_users', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
