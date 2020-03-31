# Generated by Django 3.0.4 on 2020-03-31 18:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20200331_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='firstname',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[A-ZА-Я]{1,1}[A-Za-zА-Яа-яЁё,-]{0,}', message='Введите корректное значение в поле - Фамилия')], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='lastname',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[A-ZА-Я]{1,1}[A-Za-zА-Яа-яЁё,-]{0,}', message='Введите корректное значение в поле - Фамилия')], verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='author',
            name='patronymic',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[A-ZА-Я]{1,1}[A-Za-zА-Яа-яЁё,-]{0,}', message='Введите корректное значение в поле - Фамилия')], verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='author',
            name='work_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.Workstatus', verbose_name='Рабочий статус'),
        ),
    ]
