# Generated by Django 3.0.4 on 2020-04-30 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatentOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=255, verbose_name='Патентообладатель')),
            ],
            options={
                'verbose_name': 'Патентообладатель',
                'verbose_name_plural': 'Патентообладатели',
                'ordering': ('owner_name',),
            },
        ),
        migrations.CreateModel(
            name='PLDKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_title', models.CharField(max_length=255, verbose_name='Вид ПЛД')),
            ],
            options={
                'verbose_name': 'Вид патентно-лицензионной деятельности',
                'verbose_name_plural': 'Виды патентно-лицензионной деятельности',
                'ordering': ('kind_title',),
            },
        ),
        migrations.CreateModel(
            name='PLD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pld_title', models.TextField(verbose_name='Название ПЛД')),
                ('action_start', models.DateField(blank=True, null=True, verbose_name='Начало действия')),
                ('registration_date', models.DateField(blank=True, null=True, verbose_name='Дата регистрации')),
                ('request_date', models.DateField(blank=True, null=True, verbose_name='Дата подачи заявки')),
                ('panent_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер панетна')),
                ('date_added', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время моследнего изменения')),
                ('authors', models.ManyToManyField(to='authors.Author', verbose_name='Авторы')),
                ('kind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pld.PLDKind', verbose_name='Вид ПЛД')),
                ('patent_owner', models.ManyToManyField(to='pld.PatentOwner', verbose_name='Патентообладатель')),
                ('subdivisions', models.ManyToManyField(to='authors.Subdivision', verbose_name='Подразделения')),
                ('user_added', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кем внесено/изменено')),
            ],
            options={
                'verbose_name': 'Патентно-лицензионная деятельность',
                'verbose_name_plural': 'Патентно-лицензионные деятельности',
                'ordering': ('pld_title',),
            },
        ),
    ]
