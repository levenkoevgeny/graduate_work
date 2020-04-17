from django.db import models
from authors.models import Author, Subdivision
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from dashboard.models import DashBoard


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
    kind = models.ForeignKey(PLDKind, on_delete=models.SET_NULL, verbose_name="Вид ПЛД", null=True)
    pld_title = models.TextField(verbose_name="Название ПЛД")
    action_start = models.DateField(blank=True, null=True, verbose_name="Начало действия")
    registration_date = models.DateField(blank=True, null=True, verbose_name="Дата регистрации")
    request_date = models.DateField(blank=True, null=True, verbose_name="Дата подачи заявки")
    authors = models.ManyToManyField(Author, verbose_name="Авторы")
    subdivisions = models.ManyToManyField(Subdivision, verbose_name="Подразделения")
    patent_owner = models.ManyToManyField(PatentOwner, verbose_name="Патентообладатель")
    panent_number = models.CharField(max_length=255, verbose_name="Номер панетна", blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True, verbose_name="Дата и время моследнего изменения")
    user_added = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Кем внесено/изменено")

    def __str__(self):
        return self.pld_title

    class Meta:
        ordering = ('pld_title',)
        verbose_name = 'Патентно-лицензионная деятельность'
        verbose_name_plural = 'Патентно-лицензионные деятельности'

    @property
    def get_authors(self):
        result = ""
        for author in self.authors.all():
            result += author.get_full_name
            result += ' '
        return result

    @property
    def get_pld_owners(self):
        result = ""
        for owner in self.patent_owner.all():
            result += owner.owner_name
            result += ' '
        return result


@receiver(post_save, sender=PLD)
def activity_handler(sender, instance, **kwargs):
    obj = PLD.objects.filter(pk=instance.id)[0]
    if obj.date_added is not None and obj.user_added is not None:
        dash_board = DashBoard(user=obj.user_added,
                               activity_date=obj.date_added,
                               activity_class=obj.__class__.__name__
                               )
        dash_board.save()
