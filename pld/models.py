from django.db import models
from authors.models import Author, Subdivision


class PLDKind(models.Model):
    kind_title = models.CharField(max_length=255, verbose_name="Вид ПЛД")

    def __str__(self):
        return self.kind_title

    class Meta:
        ordering = ('kind_title',)
        verbose_name = 'Вид патентно-лицензионной деятельности'
        verbose_name_plural = 'Виды патентно-лицензионной деятельности'


class PatentOwner(models.Model):
    owner_name = models.CharField(max_length=255, verbose_name="Патентообладатель")

    def __str__(self):
        return self.owner_name

    class Meta:
        ordering = ('owner_name',)
        verbose_name = 'Патентообладатель'
        verbose_name_plural = 'Патентообладатели'


class PLD(models.Model):
    kind = models.ForeignKey(PLDKind, on_delete=models.SET_NULL, verbose_name="Вид ПЛД", blank=True, null=True)
    pld_title = models.CharField(max_length=255, verbose_name="Название ПЛД")
    action_start = models.DateField(blank=True, null=True, verbose_name="Начало действия")
    registration_date = models.DateField(blank=True, null=True, verbose_name="Дата регистрации")
    request_date = models.DateField(blank=True, null=True, verbose_name="Дата подачи заявки")
    authors = models.ManyToManyField(Author, verbose_name="Авторы")
    subdivisions = models.ManyToManyField(Subdivision, verbose_name="Подразделения")
    patent_owner = models.ManyToManyField(PatentOwner, verbose_name="Патентообладатель")
    panent_number = models.CharField(max_length=255, verbose_name="Номер панетна", blank=True, null=True)

    def __str__(self):
        return self.pld_title

    class Meta:
        ordering = ('pld_title',)
        verbose_name = 'Патентно-лицензионная деятельность'
        verbose_name_plural = 'Патентно-лицензионные деятельности'
