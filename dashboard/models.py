from django.db import models
from django.contrib.auth.models import User


class DashBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Пользователь")
    activity_date = models.DateTimeField(null=True, verbose_name="Дата активности")
    activity_class = models.CharField(max_length=100, null=True, verbose_name="Класс")

    def __str__(self):
        return str(self.user.last_name) + ' ' + str(self.activity_date) + ' ' + self.activity_class

    class Meta:
        ordering = ('-activity_date',)
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'

