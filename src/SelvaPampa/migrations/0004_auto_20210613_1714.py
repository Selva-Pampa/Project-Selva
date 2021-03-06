# Generated by Django 3.2.4 on 2021-06-13 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SelvaPampa', '0003_auto_20210613_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Substratum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_type', models.IntegerField(choices=[(1, 'Taza'), (2, 'Gorra'), (3, 'Remera')])),
                ('material', models.IntegerField(choices=[(1, 'Ceramica'), (2, 'Vidrio'), (3, 'Plastico'), (4, 'Papel'), (5, 'Metal'), (6, 'Tela')])),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='design',
            name='color',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='design',
            name='style',
            field=models.CharField(default='None', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='design',
            name='theme',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='design',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SelvaPampa.design'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='sustrato',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SelvaPampa.substratum'),
            preserve_default=False,
        ),
    ]
