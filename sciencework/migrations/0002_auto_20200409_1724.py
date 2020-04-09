# Generated by Django 3.0.4 on 2020-04-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciencework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digest',
            name='in_international',
            field=models.ManyToManyField(blank=True, to='sciencework.InternationalBase', verbose_name='Международная база научного цитирования'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='in_international',
            field=models.ManyToManyField(blank=True, to='sciencework.InternationalBase', verbose_name='Международная база научного цитирования'),
        ),
    ]
