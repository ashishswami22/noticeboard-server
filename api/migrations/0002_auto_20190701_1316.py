# Generated by Django 2.2.2 on 2019-07-01 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orguser',
            name='password_hash',
        ),
        migrations.AddField(
            model_name='orguser',
            name='org',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Organization'),
        ),
        migrations.AddField(
            model_name='orguser',
            name='system_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
