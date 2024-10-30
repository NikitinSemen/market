from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Продукт")
    description = models.CharField(max_length=300, verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категории")
    description = models.CharField(max_length=300, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
