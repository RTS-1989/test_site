from django.db import models


class Page(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=80)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField(verbose_name='Последнее обновление')
    body_text = models.CharField(verbose_name='Контент страницы', blank=True, max_length=500)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title
