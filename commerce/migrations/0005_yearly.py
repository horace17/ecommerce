# Generated by Django 4.2 on 2025-01-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_watch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yearly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearly_title', models.CharField(max_length=100)),
                ('yearly_header', models.TextField(max_length=500)),
                ('yearly_button', models.CharField(max_length=100)),
            ],
        ),
    ]
