from django.db import models


class AdvertisementModel(models.Model):
    idOnSite = models.IntegerField(name="Номер id на сайте")
    title = models.CharField(max_length=100, name="Заголовок")
    author = models.CharField(max_length=20, name="Автор")
    numberViews = models.IntegerField(default=0, name="Количество просмотров")
    position = models.IntegerField(name="Номер позиции")

    def __str__(self):
        return "Объявление"

    class Meta:
        verbose_name_plural = 'Объявления'

