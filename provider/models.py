from django.contrib.gis.db import models


class Provider(models.Model):
    """Поставщик"""

    name = models.CharField("Название организации", max_length=255)
    mail = models.CharField("Емейл", max_length=255)
    phone = models.CharField("Телефон", max_length=255)
    address = models.CharField("Адрес", max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    """Услуга"""
    name = models.CharField("Название услуги", max_length=255)

    def __str__(self):
        return self.name


class Area(models.Model):
    """"Зона обслуживания"""

    name = models.CharField("Название области", max_length=255)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name="Поставщик")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    price = models.DecimalField("Цена обслуживания", max_digits=10, decimal_places=2)
    polygon = models.GeometryField()

    def __str__(self):
        return self.name


