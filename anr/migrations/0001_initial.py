# Generated by Django 3.0.4 on 2020-04-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nir', '0002_delete_organization'),
        ('authors', '0004_auto_20200409_1718'),
        ('sciencework', '0006_auto_20200409_1929'),
        ('dissertationresearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopmentKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_title', models.CharField(max_length=255, verbose_name='Вид внедренной разработки')),
            ],
            options={
                'verbose_name': 'Вид внедренной разработки',
                'verbose_name_plural': 'Виды внедренной разработки',
                'ordering': ('kind_title',),
            },
        ),
        migrations.CreateModel(
            name='IntroductionKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction_kind_title', models.CharField(max_length=255, verbose_name='Вид внедрения')),
            ],
            options={
                'verbose_name': 'Вид внедрения',
                'verbose_name_plural': 'Виды внедрения',
                'ordering': ('introduction_kind_title',),
            },
        ),
        migrations.CreateModel(
            name='IntroductionOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255, verbose_name='Организация внедрения')),
            ],
            options={
                'verbose_name': 'Организация внедрения',
                'verbose_name_plural': 'Организации внедрения',
                'ordering': ('organization_name',),
            },
        ),
        migrations.CreateModel(
            name='ANR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve_date', models.DateField(verbose_name='Дата внедрения')),
                ('half_year', models.CharField(blank=True, max_length=1, null=True, verbose_name='Полугодие внедрения')),
                ('is_student_participation', models.BooleanField(verbose_name='Участие обучающихся')),
                ('authors', models.ManyToManyField(to='authors.Author', verbose_name='Авторы')),
                ('development_kind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='anr.DevelopmentKind', verbose_name='Вид внедренной разработки')),
                ('dissertation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dissertationresearch.DissertationResearch', verbose_name='Диссертационное исследование')),
                ('introduction_kind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='anr.IntroductionKind', verbose_name='Вид внедрения')),
                ('introduction_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anr.IntroductionOrganization', verbose_name='Организация внедрения')),
                ('nir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nir.NIR', verbose_name='Научно-исследовательская работа')),
                ('sciencework', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sciencework.Sciencework', verbose_name='Научная работа')),
                ('subdivisions', models.ManyToManyField(to='authors.Subdivision', verbose_name='Подразделения разработки')),
            ],
            options={
                'verbose_name': 'Апробация научных результатов',
                'verbose_name_plural': 'Апробации научных результатов',
                'ordering': ('development_kind',),
            },
        ),
    ]