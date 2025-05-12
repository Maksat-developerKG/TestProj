from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.TextField(verbose_name='Описание')
    content = models.TextField(verbose_name='Контент')
    data_publish = models.DateField(auto_now_add=True, 
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(User, verbose_name='Пользователь',
                                on_delete=models.CASCADE)


    def __str__(self):
        return f'Автор {self.author} Дата пуб.{self.data_publish}'
    

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'