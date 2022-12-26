from django.db import models
from django.urls import reverse


class Liblinks(models.Model):
    authors = models.CharField(max_length=150, verbose_name="Авторы")
    title = models.CharField(max_length=150, verbose_name='Наименование')
    num_izd = models.CharField(max_length=150, verbose_name="Номер издания")
    city = models.CharField(max_length=150, verbose_name="Город издания")
    izdatelstvo = models.CharField(max_length=150, verbose_name="Издательство")
    year = models.CharField(max_length=150, verbose_name="Год издания")
    total = models.CharField(max_length=150, verbose_name="Общее число страниц в книге")

    def __str__(self):
        return ("%s %s %s %s %s %s %s %s %s %s %s %s %s %s") % (
        self.authors, self.title, self.num_izd, self.city, self.izdatelstvo, self.year, self.total)
