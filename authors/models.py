from django.db import models
from .validators import *


class Subdivisiongroup(models.Model):
    subdivisiongroup_name = models.CharField(max_length=255, verbose_name="Группа подразделений")

    def natural_key(self):
        return (self.subdivisiongroup_name)

    def __str__(self):
        return self.subdivisiongroup_name

    class Meta:
        ordering = ('subdivisiongroup_name',)
        verbose_name = 'Группа подразделений'
        verbose_name_plural = 'Группы подразделений'


class Subdivision(models.Model):
    subdivision_name = models.CharField(max_length=255, verbose_name="Наименование подразделения")
    subdivision_short_name = models.CharField(max_length=70, verbose_name="Сокращенное наименование подразделения",
                                              blank=True, null=True)
    group = models.ForeignKey(Subdivisiongroup, on_delete=models.SET_NULL, null=True, verbose_name="Группа подразделений")

    def __str__(self):
        return self.subdivision_name

    class Meta:
        ordering = ('subdivision_name',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Position(models.Model):
    position_name = models.CharField(max_length=255, verbose_name="Должность")

    def __str__(self):
        return self.position_name

    class Meta:
        ordering = ('position_name',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Candidatespecialty(models.Model):
    candidate_specialty_title = models.CharField(max_length=255, verbose_name="Название кандидатской диссертации")

    def __str__(self):
        return self.candidate_specialty_title

    class Meta:
        ordering = ('candidate_specialty_title',)
        verbose_name = 'Кандидатская специальность'
        verbose_name_plural = 'Кандидатские специальности'


class Doctorspecialty(models.Model):
    doctor_specialty_title = models.CharField(max_length=255, verbose_name="Название докторской диссертации")

    def __str__(self):
        return self.doctor_specialty_title

    class Meta:
        ordering = ('doctor_specialty_title',)
        verbose_name = 'Докторская специальность'
        verbose_name_plural = 'Докторские специальности'


class Rank(models.Model):
    rank = models.CharField(max_length=100, verbose_name="Звание")

    def __str__(self):
        return self.rank

    class Meta:
        ordering = ('id',)
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'


class Workstatus(models.Model):
    status = models.CharField(max_length=100, verbose_name="Рабочий статус")

    def __str__(self):
        return self.status

    class Meta:
        ordering = ('id',)
        verbose_name = 'Рабочий статус'
        verbose_name_plural = 'Рабочие статусы'


class Author(models.Model):
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, null=True, verbose_name="Подразделение")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия", validators=[name_validator])
    firstname = models.CharField(max_length=100, verbose_name="Имя", validators=[name_validator])
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", validators=[name_validator])
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Звание")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Должность")
    position_date = models.DateField(blank=True, null=True, verbose_name="Дата назначения на должность")
    is_docentvak = models.BooleanField(default=False, verbose_name="Является доцентом ВАК")
    docentvak_date = models.DateField(blank=True, null=True, verbose_name="Дата присовения доцента ВАК")
    is_professor = models.BooleanField(default=False, verbose_name="Является профессором")
    professor_date = models.DateField(blank=True, null=True, verbose_name="Дата присвоения профессороской степени")
    is_candidate = models.BooleanField(default=False, verbose_name="Является кандидатом наук")
    candidate_date = models.DateField(blank=True, null=True, verbose_name="Дата присвоения кандидата наук")
    candidate_title = models.TextField(blank=True, null=True, verbose_name="Название кандидатской диссертации")
    candidate_specialty = models.ForeignKey(Candidatespecialty, on_delete=models.SET_NULL, blank=True, null=True,
                                            verbose_name="Кандидатская специальность")
    is_doctor = models.BooleanField(default=False, verbose_name="Является доктором наук")
    doctor_date = models.DateField(blank=True, null=True, verbose_name="Дата присвоения доктора наук")
    doctor_title = models.TextField(blank=True, null=True, verbose_name="Название докторской диссертации")
    doctor_specialty = models.ForeignKey(Doctorspecialty, on_delete=models.SET_NULL, blank=True, null=True,
                                         verbose_name="Докторская специальность")
    extra_data = models.TextField(blank=True, null=True, verbose_name="Дополнительные данные")
    work_status = models.ForeignKey(Workstatus, on_delete=models.SET_NULL, null=True,
                                    verbose_name="Рабочий статус")

    def __str__(self):
        return self.lastname + ' ' + self.firstname + ' ' + self.patronymic + ' ' + str(self.subdivision)

    class Meta:
        ordering = ('lastname',)
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    @property
    def get_full_name(self):
        return "{} {}.{}".format(self.lastname, self.firstname[0], self.patronymic[0])

    @property
    def get_is_docent_vak(self):
        return "{}".format("Да" if self.is_docentvak else "Нет")

    @property
    def get_is_professor(self):
        return "{}".format("Да" if self.is_professor else "Нет")

    @property
    def get_is_candidate(self):
        return "{}".format("Да" if self.is_candidate else "Нет")

    @property
    def get_is_doctor(self):
        return "{}".format("Да" if self.is_doctor else "Нет")
