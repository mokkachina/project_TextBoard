from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_user = models.SmallIntegerField(default=0)

    def update_rating(self):
        pass

class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    dataCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64),
    text = models.TextField()
    category = models.CharField(max_length=11, choices=TYPE, default='tank')
    image = models.ImageField(upload_to='images/')
    upload = models.FileField(upload_to='uploads/')
    # art = Article.objects.first()

    def __str__(self):
        return f'{self.image}'

# art.apload.url
class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    dataCreation = models.DateTimeField(auto_now_add=True)


