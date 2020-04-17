from django.db import models

from authors.models import Author, Subdivision

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from dashboard.models import DashBoard


class ReasonNIR(models.Model):
    reason_name = models.CharField(max_length=255, verbose_name="Основание для проведения НИР")

    def __str__(self):
        return self.reason_name

    class Meta:
        ordering = ('reason_name',)
        verbose_name = 'Основание для проведения НИР'
        verbose_name_plural = 'Основания для проведения НИР'


class ResearchResults(models.Model):
    research_result_name = models.CharField(max_length=255, verbose_name="Результат исследования")

    def __str__(self):
        return self.research_result_name

    class Meta:
        ordering = ('research_result_name',)
        verbose_name = 'Результат исследования'
        verbose_name_plural = 'Результаты исследования'


class NIR(models.Model):
    nir_title = models.TextField()
    reason = models.ManyToManyField(ReasonNIR, verbose_name="Основания для проведения")
    plan_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Пункт плана для проведения")
    start_date = models.DateField(blank=True, null=True, verbose_name="Дата начала")
    end_date = models.DateField(blank=True, null=True, verbose_name="Дата окончания")
    result = models.ForeignKey(ResearchResults, on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name="Результат проведения НИР")
    approve_date = models.DateField(blank=True, null=True, verbose_name="Дата утверждения акта")
    authors = models.ManyToManyField(Author, verbose_name="Авторы НИР")
    subdivisions = models.ManyToManyField(Subdivision, verbose_name="Подразделения НИР")
    nir_leader = models.ForeignKey(Author, related_name="nir_leader", on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name="Научный руководитель")
    leader_subdivision = models.ForeignKey(Subdivision, related_name='nir_leader_subdivision', on_delete=models.SET_NULL, null=True, blank=True,
                                           verbose_name="Подразделение научного руководителя")
    date_added = models.DateTimeField(blank=True, null=True, verbose_name="Дата и время моследнего изменения")
    user_added = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Кем внесено/изменено")

    class Meta:
        ordering = ('nir_title',)
        verbose_name = 'Научно-исследовательская работа'
        verbose_name_plural = 'Научно-исследовательские работы'

    def __str__(self):
        return self.nir_title

    @property
    def get_authors(self):
        s = ''
        for author in self.authors.all():
            s += author.get_full_name
            s += ' '
        return s

    @property
    def get_reasons(self):
        s = ''
        for reason in self.reason.all():
            s += reason.reason_name
            s += ' '
        return s

    @property
    def get_subdivisions(self):
        s = ''
        for subdivision in self.subdivisions.all():
            s += subdivision.subdivision_name
            s += ' '
        return s


@receiver(post_save, sender=NIR)
def activity_handler(sender, instance, **kwargs):
    obj = NIR.objects.filter(pk=instance.id)[0]
    if obj.date_added is not None and obj.user_added is not None:
        dash_board = DashBoard(user=obj.user_added,
                               activity_date=obj.date_added,
                               activity_class=obj.__class__.__name__
                               )
        dash_board.save()
