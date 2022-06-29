from django.db import models


class Task(models.Model):
    title = models.TextField('Название')
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'