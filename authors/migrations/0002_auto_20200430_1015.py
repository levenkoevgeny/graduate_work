# Generated by Django 3.0.4 on 2020-04-30 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.Position', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='author',
            name='rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.Rank', verbose_name='Звание'),
        ),
    ]
