from django.db import models

# Create your models here.
class Kurs(models.Model):
    kaf = models.CharField(max_length=255, verbose_name="Кафедра")
    name_work = models.CharField(max_length=255, verbose_name="Название работы")
    num_list = models.CharField(max_length=30, verbose_name="Номер листов")
    podp1 = models.CharField(max_length=30, verbose_name="Подпись 1")
    prepod = models.CharField(max_length=30, verbose_name="Препод")
    group = models.CharField(max_length=30, verbose_name="Группа")
    d1 = models.CharField(max_length=30, verbose_name="День проверки")
    m1 = models.CharField(max_length=30, verbose_name="Месяц проверки")
    year1 = models.CharField(max_length=30, verbose_name="Год проверки")
    podp2 = models.CharField(max_length=30, verbose_name="Подпись 2")
    student = models.CharField(max_length=30, verbose_name="Студент")
    d2 = models.CharField(max_length=30, verbose_name="День сдачи")
    m2 = models.CharField(max_length=30, verbose_name="Месяц сдачи")
    year2 = models.CharField(max_length=30, verbose_name="Год сдачи")

    def __str__(self):

        return ("%s %s %s %s %s %s %s %s %s %s %s %s %s %s") % (self.kaf, self.name_work, self.num_list, self.podp1, self.prepod, self.group, self.d1,
         self.m1, self.year1, self.podp2, self.student, self.d2, self.m2, self.year2)
