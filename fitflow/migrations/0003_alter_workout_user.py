# Generated by Django 4.2.3 on 2024-03-22 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitflow', '0002_fituser_activation_link_sent_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
