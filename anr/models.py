from django.db import models
from authors.models import Author, Subdivision
from sciencework.models import Sciencework
from dissertationresearch.models import DissertationResearch
from nir.models import NIR
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from dashboard.models import DashBoard


class DevelopmentKind(models.Model):
    kind_title = models.CharField(max_length=255, verbose_name="Вид внедренной разработки")

    def __str__(self):
        return self.kind_title

    class Meta:
        ordering = ('kind_title',)
        verbose_name = 'Вид внедренной разработки'
        verbose_name_plural = 'Виды внедренной разработки'


class IntroductionKind(models.Model):
    introduction_kind_title = models.CharField(max_length=255, verbose_name="Вид внедрения")

    def __str__(self):
        return self.introduction_kind_title

    class Meta:
        ordering = ('introduction_kind_title',)
        verbose_name = 'Вид внедрения'
        verbose_name_plural = 'Виды внедрения'


class IntroductionOrganization(models.Model):
    organization_name = models.CharField(max_length=255, verbose_name="Организация внедрения")

    def __str__(self):
        return self.organization_name

    class Meta:
        ordering = ('organization_name',)
        verbose_name = 'Организация внедрения'
        verbose_name_plural = 'Организации внедрения'


class ANR(models.Model):
    development_kind = models.ForeignKey(DevelopmentKind, on_delete=models.SET_NULL,
                                         verbose_name="Вид внедренной разработки", null=True)
    introduction_kind = models.ForeignKey(IntroductionKind, on_delete=models.SET_NULL, verbose_name="Вид внедрения", null=True)
    introduction_organization = models.ForeignKey(IntroductionOrganization, on_delete=models.CASCADE,
                                                  verbose_name="Организация внедрения")
    approve_date = models.DateField(verbose_name="Дата утверждения акта")
    year = models.IntegerField(verbose_name="Год внедрения", blank=True, null=True)
    half_year = models.CharField(max_length=1, blank=True, null=True, verbose_name="Полугодие внедрения")
    authors = models.ManyToManyField(Author, verbose_name="Авторы")
    subdivisions = models.ManyToManyField(Subdivision, verbose_name="Подразделения разработки")
    is_student_participation = models.BooleanField(verbose_name="Участие обучающихся")
    sciencework = models.ForeignKey(Sciencework, on_delete=models.CASCADE, verbose_name="Научная работа", blank=True, null=True)
    nir = models.ForeignKey(NIR, on_delete=models.CASCADE, verbose_name="Научно-исследовательская работа", blank=True, null=True)
    dissertation = models.ForeignKey(DissertationResearch, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name="Диссертационное исследование")
    date_added = models.DateTimeField(blank=True, null=True, verbose_name="Дата и время моследнего изменения")
    user_added = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Кем внесено/изменено")


    def __str__(self):
        return self.development_kind.kind_title

    class Meta:
        ordering = ('development_kind',)
        verbose_name = 'Апробация научных результатов'
        verbose_name_plural = 'Апробации научных результатов'

    @property
    def get_development_title(self):
        title = ""
        if str(self.development_kind.kind_title).__contains__("Научная"):
            title = self.sciencework.output_data
        elif str(self.development_kind.kind_title).__contains__("Диссер"):
            title = self.dissertation.dissertation_theme
        elif str(self.development_kind.kind_title).__contains__("Научно-исслед"):
            title = self.nir.nir_title
        return title

    @property
    def get_authors(self):
        result = ""
        for author in self.authors.all():
            result += author.get_full_name
            result += ' '
        return result

    @property
    def get_subdivisions(self):
        result = ""
        for subdivision in self.subdivisions.all():
            result += subdivision.subdivision_name
            result += ' '
        return result


@receiver(post_save, sender=ANR)
def activity_handler(sender, instance, **kwargs):
    obj = ANR.objects.filter(pk=instance.id)[0]
    if obj.date_added is not None and obj.user_added is not None:
        dash_board = DashBoard(user=obj.user_added,
                               activity_date=obj.date_added,
                               activity_class=obj._meta.verbose_name
                               )
        dash_board.save()
