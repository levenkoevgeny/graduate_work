# Generated by Django 3.0.4 on 2020-03-31 17:49

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
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.Position', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='author',
            name='rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.Rank', verbose_name='Звание'),
        ),
        migrations.AlterField(
            model_name='author',
            name='work_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.Workstatus', verbose_name='Рабочий статус'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.Subdivisiongroup', verbose_name='Группа подразделений'),
        ),
    ]