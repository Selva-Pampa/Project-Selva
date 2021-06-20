# Generated by Django 3.2.4 on 2021-06-13 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SelvaPampa', '0005_rename_sustrato_item_substratum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='design',
            name='picture',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]