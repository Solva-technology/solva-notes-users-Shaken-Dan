from django.db import models
from django.db.models import CASCADE, CharField
from django.contrib.auth import get_user_model


User = get_user_model()

# class User(models.Model):
#     name = models.CharField('Имя', max_length=100)
#     email = models.EmailField('Почта',unique=True)
#
#     class Meta:
#         verbose_name = 'пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('Биография',max_length=500)
    birth_date = models.DateField('Дата рождения')

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.user.username

class Note(models.Model):
    text = models.TextField('Текст', max_length=1000)
    created_at = models.DateTimeField('Дата' ,auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='Автор'
    )
    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='Статус'
    )
    categories = models.ManyToManyField('Category', verbose_name='Категории')

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural ='Заметки'

    def __str__(self):
        return str(self.author)

class Status(models.Model):
    name = CharField('Статус',max_length=20)
    is_final = models.BooleanField('Конечный статус')

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField('Название категории', max_length=50)
    description = models.TextField('Описание категории', max_length=500)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title