from django.db import models
from django.db.models.fields.related_lookups import RelatedIsNull


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название", db_index=True)
    description = models.CharField(max_length=300, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.CharField(max_length=300, verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    Category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категории",
        null=True,
        related_name="category",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
