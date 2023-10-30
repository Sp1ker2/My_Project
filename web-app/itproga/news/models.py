from django.db import models


# Create your models here .
class Artiles(models.Model):
    title = models.CharField('Name', max_length=50, default='')
    anons = models.CharField('Anons', max_length=250, default='')
    full_text = models.TextField('Text')
    date=models.DateTimeField('Data')


    def __str__(self):
        return f'News'
    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"