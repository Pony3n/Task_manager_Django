from django.db import models

class Task(models.Model):
    title = models.CharField("Нзвание", max_length=50)
    description = models.TextField('Описание задачи')
    until = models.DateField('Закончить до...')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class User(models.Model):
    nick = models.CharField('Никнейм', max_length=20)
    email = models.EmailField('Почта')
    password = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return self.nick

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'