from django.db import models

# Create your models here.
class Declaration(models.Model):
    directorinst = models.CharField(max_length=255, verbose_name="Директор")
    directorfiliala = models.CharField(max_length=255, verbose_name="Дирекция института")
    group = models.CharField(max_length=30, verbose_name="Номер группы")
    fio = models.CharField(max_length=30, verbose_name="ФИО студента(ки)")
    vsvazy = models.CharField(max_length=30, verbose_name="Причина заявления")
    doc1 = models.CharField(max_length=30, verbose_name="Допумент 1")
    doc2 = models.CharField(max_length=30, verbose_name="Документ 2")
    doc3 = models.CharField(max_length=30, verbose_name="Документ 3")
    d = models.CharField(max_length=30, verbose_name="День")
    month = models.CharField(max_length=30, verbose_name="Месяц")
    year = models.CharField(max_length=30, verbose_name="Год")
    nasnachits = models.CharField(max_length=30, verbose_name="Первый день")
    nasnachitpo = models.CharField(max_length=30, verbose_name="Последний день")
    nasnachenas = models.CharField(max_length=30, verbose_name="Первый день до заявления")
    nasnachenapo = models.CharField(max_length=30, verbose_name="Последний день до заявления")
    dp = models.CharField(max_length=30, verbose_name="День приказа")
    monthp = models.CharField(max_length=30, verbose_name="Месяц приказа")
    yearp = models.CharField(max_length=30, verbose_name="Год приказа")
    directorinstf = models.CharField(max_length=30, verbose_name="Дирекция")
    fio2 = models.CharField(max_length=30, verbose_name="ФИО директора")
    d2 = models.CharField(max_length=30, verbose_name="Дата согласования")
    month2 = models.CharField(max_length=30, verbose_name="Месяц согласования")
    year2 = models.CharField(max_length=30, verbose_name="Год согласования")

    def __str__(self):

        return ("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s") % (self.directorinst, self.directorfiliala, self.group, self.fio, self.vsvazy, self.group, self.doc1,
         self.doc2, self.doc3, self.d, self.month, self.year, self.nasnachits, self.nasnachitpo, self.nasnachenas, self.nasnachenapo, self.dp, self.monthp, self.yearp, self.directorinstf
                                                                , self.fio2, self.d2, self.month2, self.year2)
