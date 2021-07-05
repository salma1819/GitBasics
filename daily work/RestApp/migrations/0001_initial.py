# Generated by Django 3.2.4 on 2021-07-05 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rname', models.CharField(max_length=30)),
                ('Nitems', models.IntegerField()),
                ('timings', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('rsimg', models.ImageField(default='logo.jpg', upload_to='Restaurantimages/')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Itemlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=50)),
                ('icategory', models.CharField(choices=[('NV', 'Non-Veg'), ('VG', 'Veg'), ('Df', 'Select Item Type')], default='DF', max_length=12)),
                ('price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('iimage', models.ImageField(default='logo.jpg', upload_to='Itemimages/')),
                ('itavailability', models.CharField(choices=[('AV', 'Available'), ('NA', 'Not Available'), ('Sl', 'Select Availability')], default='Sl', max_length=20)),
                ('rsimg', models.ImageField(default='logo.jpg', upload_to='Itemimages/')),
                ('rsid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestApp.restaurant')),
            ],
        ),
    ]