# Generated by Django 3.2.4 on 2021-07-07 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0003_auto_20210707_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rolereq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rltype', models.CharField(choices=[(2, 'Manager'), (3, 'User')], max_length=10)),
                ('pfe', models.ImageField(default='logo.jpg', upload_to='Rolereqpics/')),
                ('is_checked', models.BooleanField(default=False)),
                ('uname', models.CharField(max_length=50)),
                ('ud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
