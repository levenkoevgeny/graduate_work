from django.db import models
from authors.models import Author, Subdivision
from dashboard.models import DashBoard
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Publicationkind(models.Model):
    publication_kind = models.CharField(max_length=255)

    def __str__(self):
        return self.publication_kind

    class Meta:
        ordering = ('publication_kind',)
        verbose_name = 'Вид публикации'
        verbose_name_plural = 'Виды публикации'


class Grif(models.Model):
    grif_name = models.CharField(max_length=255)

    def __str__(self):
        return self.grif_name

    class Meta:
        ordering = ('grif_name',)
        verbose_name = 'Гриф'
        verbose_name_plural = 'Грифы'


class Interest(models.Model):
    interest_name = models.CharField(max_length=255, verbose_name="В чьих интересах")

    def __str__(self):
        return self.interest_name

    class Meta:
        ordering = ('interest_name',)
        verbose_name = 'В чьих интересах'
        verbose_name_plural = 'В чьих интересах'


class InternationalBase(models.Model):
    base_name = models.CharField(max_length=255, verbose_name="Международная база научного цитирования")

    def __str__(self):
        return self.base_name

    class Meta:
        ordering = ('base_name',)
        verbose_name = 'Международная база научного тестирования'
        verbose_name_plural = 'Международные базы научного тестирования'


class Magazine(models.Model):
    magazine_name = models.CharField(max_length=255, verbose_name="Название журнала")
    in_vak = models.BooleanField(blank=True, null=True, verbose_name="В ВАК")
    in_international = models.ManyToManyField(InternationalBase,
                                              verbose_name="Международная база научного цитирования",
                                              blank=True)

    def __str__(self):
        return self.magazine_name

    class Meta:
        ordering = ('magazine_name',)
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

    @property
    def get_in_vak(self):
        return "{}".format("Да" if self.in_vak else "Нет")


class Digest(models.Model):
    digest_name = models.CharField(max_length=255, verbose_name="Название сборника статей")
    in_vak = models.BooleanField(blank=True, null=True, verbose_name="В ВАК")
    in_international = models.ManyToManyField(InternationalBase,
                                              verbose_name="Международная база научного цитирования",
                                              blank=True)

    def __str__(self):
        return self.digest_name

    class Meta:
        ordering = ('digest_name',)
        verbose_name = 'Сборник статей'
        verbose_name_plural = 'Сборники статей'

    @property
    def get_in_vak(self):
        return "{}".format("Да" if self.in_vak else "Нет")


class Statuskonf(models.Model):
    status_name = models.CharField(max_length=255, verbose_name="Статус научного форума")

    def __str__(self):
        return self.status_name

    class Meta:
        ordering = ('status_name',)
        verbose_name = 'Статус начного форума'
        verbose_name_plural = 'Статусы научных форумов'


class Kindkonf(models.Model):
    kind_name = models.CharField(max_length=255, verbose_name="Вид научного форума")

    def __str__(self):
        return self.kind_name

    class Meta:
        ordering = ('kind_name',)
        verbose_name = 'Вид научного форума'
        verbose_name_plural = 'Виды научных форумов'


class Organizatorforum(models.Model):
    org_name = models.CharField(max_length=255, verbose_name="Организатор форума")

    def __str__(self):
        return self.org_name

    class Meta:
        ordering = ('org_name',)
        verbose_name = 'Организатор форума'
        verbose_name_plural = 'Организаторы форумов'


class Cityforforum(models.Model):
    city_forum_title = models.CharField(max_length=100, verbose_name="Страна проведения форума")

    def __str__(self):
        return self.city_forum_title

    class Meta:
        ordering = ('city_forum_title',)
        verbose_name = 'Страна проведения форума'
        verbose_name_plural = 'Страны проведения форума'


class Conference(models.Model):
    conference_name = models.TextField(verbose_name="Название конференции")
    conference_name_short = models.TextField(verbose_name="Название конференции(сокращенное)", blank=True, null=True)
    forum_status = models.ForeignKey(Statuskonf, on_delete=models.SET_NULL, blank=True, null=True,
                                     verbose_name="Статус научного форума")
    kind_forum = models.ForeignKey(Kindkonf, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Вид научного форума")
    organizator_forum = models.ForeignKey(Organizatorforum, on_delete=models.SET_NULL, blank=True, null=True,
                                          verbose_name="Организатор научного форума")
    forum_date = models.DateField(blank=True, null=True, verbose_name="Дата проведения")
    forum_country = models.ForeignKey(Cityforforum, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="Страна проведения")
    moderators = models.ManyToManyField(Author, verbose_name="Модераторы научного форума/руководители секции", blank=True)

    def __str__(self):
        return str(self.conference_name_short)

    class Meta:
        ordering = ('conference_name',)
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255, verbose_name="Издатель")

    def __str__(self):
        return self.publisher_name

    class Meta:
        ordering = ('publisher_name',)
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Subspecies(models.Model):
    title = models.CharField(max_length=255, verbose_name="Подвид научного издания")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Подвид учебного издания'
        verbose_name_plural = 'Подвиды учебных изданий'


class Orgfounder(models.Model):
    org_name = models.CharField(max_length=255, verbose_name="Организация учредитель сборника")

    def __str__(self):
        return self.org_name

    class Meta:
        ordering = ('org_name',)
        verbose_name = 'Организация учредитель сборника'
        verbose_name_plural = 'Организации учредители сборников'


class Sciencework(models.Model):
    kind = models.ForeignKey(Publicationkind, on_delete=models.SET_NULL, null=True, verbose_name="Вид научной работы")
    year = models.IntegerField(verbose_name="Год издания")
    half_year = models.CharField(max_length=10, default="Не указано", verbose_name="Полугодие")
    output_data = models.TextField(verbose_name="Выходные данные")
    sheet_count = models.CharField(max_length=100, blank=True, null=True, verbose_name="Количество печатных листов")
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Издатель")
    grif = models.ForeignKey(Grif, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Гриф")
    magazine = models.ForeignKey(Magazine, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Журнал")
    digest = models.ForeignKey(Digest, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Сборник статей")
    in_vak = models.BooleanField(blank=True, null=True, verbose_name="Является работой ВАК")
    in_internationals = models.ManyToManyField(InternationalBase,
                                               verbose_name="Входит в международную базу научного цитирования", blank=True)
    interest = models.ForeignKey(Interest, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="В чьих интересах")
    conference = models.ForeignKey(Conference, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Конференция")
    work_is_foreignauthors = models.BooleanField(blank=True, null=True, verbose_name="Участие сторонних авторов")
    other_author_count = models.IntegerField(default=0, blank=True, null=True, verbose_name="Количество сторонних авторов")
    sciencework_student_participation = models.BooleanField(blank=True, null=True, default=False,
                                                            verbose_name="Участие обучающихся")
    authors = models.ManyToManyField(Author, verbose_name="Авторы")
    subdivisions = models.ManyToManyField(Subdivision, verbose_name="Подразделения")

    subspecies = models.ForeignKey(Subspecies, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Подвид учебного издания")
    org_founder = models.ForeignKey(Orgfounder, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name="Организация учредитель сборника")
    date_added = models.DateTimeField(blank=True, null=True, verbose_name="Дата и время моследнего изменения")
    user_added = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Кем внесено/изменено")

    class Meta:
        ordering = ('kind',)
        verbose_name = 'Научная работа'
        verbose_name_plural = 'Научная работа'

    def __str__(self):
        return self.output_data if self.output_data else "blank"


@receiver(post_save, sender=Sciencework)
def activity_handler(sender, instance, **kwargs):
    obj = Sciencework.objects.filter(pk=instance.id)[0]
    if obj.date_added is not None and obj.user_added is not None:
        dash_board = DashBoard(user=obj.user_added,
                               activity_date=obj.date_added,
                               activity_class=obj._meta.verbose_name
                               )
        dash_board.save()
