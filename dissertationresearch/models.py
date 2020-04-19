from django.db import models
from authors.models import Author, Subdivision
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from dashboard.models import DashBoard


class ResearchKind(models.Model):
    kind_name = models.CharField(max_length=255, verbose_name="Вид диссертационного исследования")

    def __str__(self):
        return self.kind_name

    class Meta:
        ordering = ('kind_name',)
        verbose_name = 'Вид исследования'
        verbose_name_plural = 'Виды исследований'


class ResearchStatus(models.Model):
    status_name = models.CharField(max_length=255, verbose_name="Статус исследователя")

    def __str__(self):
        return self.status_name

    class Meta:
        ordering = ('status_name',)
        verbose_name = 'Статус исследователя'
        verbose_name_plural = 'Статусы исследователей'


class ResearchPlace(models.Model):
    place = models.CharField(max_length=255, verbose_name="Место проведения")

    def __str__(self):
        return self.place

    class Meta:
        ordering = ('place',)
        verbose_name = 'Место проведения исследования'
        verbose_name_plural = 'Места проведения исследований'


class Reason(models.Model):
    reason = models.CharField(max_length=255, verbose_name="Основание")

    def __str__(self):
        return self.reason

    class Meta:
        ordering = ('reason',)
        verbose_name = 'Основание для проведения исследования'
        verbose_name_plural = 'Основания для проведения исследования'


class DissertationResearch(models.Model):
    kind = models.ForeignKey(ResearchKind, on_delete=models.SET_NULL, null=True, verbose_name="Вид исследования")
    status = models.ForeignKey(ResearchStatus, on_delete=models.SET_NULL, null=True, verbose_name="Статус исследователя")
    date_begin = models.IntegerField(verbose_name="Год начала", null=True, blank=True)
    date_end = models.IntegerField(verbose_name="Год окончания", null=True, blank=True)
    date_protect = models.DateField(verbose_name="Дата защиты", null=True, blank=True)
    dissertation_theme = models.TextField(verbose_name="Тема исследования")
    reason = models.ForeignKey(Reason, on_delete=models.SET_NULL, null=True, verbose_name="Основание для проведения исследования")
    result = models.CharField(max_length=255, null=True, blank=True, verbose_name="Результат исследования")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="author", null=True, verbose_name="Автор исследования")
    leader = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="leader", null=True, verbose_name="Научный руководитель")
    leader_subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, related_name="leader_subdivision", null=True, blank=True,
                                           verbose_name="Подразделение научного руководителя")
    research_place = models.ForeignKey(ResearchPlace, on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name="Место проведения исследования")
    research_place_subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, related_name="research_place_subdivision", null=True, blank=True,
                                                   verbose_name="Подразделение Академии МВД РБ (место проведения)")
    date_added = models.DateTimeField(blank=True, null=True, verbose_name="Дата и время моследнего изменения")
    user_added = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Кем внесено/изменено")

    class Meta:
        ordering = ('id',)
        verbose_name = 'Диссертационное исследование'
        verbose_name_plural = 'Диссертационные исследования'

    def __str__(self):
        return self.dissertation_theme


@receiver(post_save, sender=DissertationResearch)
def activity_handler(sender, instance, **kwargs):
    obj = DissertationResearch.objects.filter(pk=instance.id)[0]
    dash_board = DashBoard(user=obj.user_added,
                           activity_date=obj.date_added,
                           activity_class=obj._meta.verbose_name
                           )
    dash_board.save()

