from django.db import models
from ckeditor.fields import RichTextField

class BookArrival(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='book_arrival_images/', verbose_name="Изображение")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Поступление книги"
        verbose_name_plural = "Поступления книг"

class MediaCoverage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    coverage_period = models.CharField(max_length=255, verbose_name="Период охвата")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='media_coverage_images/', verbose_name="Изображение")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Освещение в СМИ"
        verbose_name_plural = "Освещения в СМИ"

class NewsDetail(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='news_detail_images/', verbose_name="Изображение")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подробности новости"
        verbose_name_plural = "Подробности новостей"