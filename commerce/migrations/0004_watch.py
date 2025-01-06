# Generated by Django 4.2 on 2025-01-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_mobile_remove_service_service_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_button', models.CharField(max_length=100)),
                ('watch_image', models.ImageField(upload_to='mobiles/')),
                ('watch_type', models.CharField(max_length=100)),
                ('watch_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
