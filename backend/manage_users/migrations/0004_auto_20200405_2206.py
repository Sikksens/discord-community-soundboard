# Generated by Django 3.0.4 on 2020-04-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_users', '0003_auto_20200329_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
