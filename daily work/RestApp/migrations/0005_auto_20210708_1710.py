# Generated by Django 3.2.4 on 2021-07-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0004_rolereq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rolereq',
            old_name='pfe',
            new_name='pfl',
        ),
        migrations.AlterField(
            model_name='rolereq',
            name='rltype',
            field=models.IntegerField(choices=[(2, 'Manager'), (3, 'User')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Guest'), (2, 'Manager'), (3, 'User')], default=1, max_length=10),
        ),
    ]
