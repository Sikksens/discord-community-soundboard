# Generated by Django 3.0.4 on 2020-04-01 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discord_bot', '0002_auto_20200329_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundclip',
            name='creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='soundclip',
            name='duration',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='soundclip',
            name='plays',
            field=models.BigIntegerField(default=0),
        ),
    ]
