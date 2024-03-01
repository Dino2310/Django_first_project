from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    def __str__(self):
        return self.title
    #CharField - короткое текстовое поле с максимальной длиной в 255 символов
    title = models.CharField(max_length = 255)
    #TextField - длинное текстовове поле без ограничений в длине
    content = models.TextField()
    #SlugField - это поле состоящее из символов и чисел. нужно для генерации ссылок
    slug = models.SlugField(unique = True)
    #DateField  - поле хранящее дату
    date_created = models.DateField(auto_now_add = True)
    #DateTimeField  - поле хранящее дату и время
    update_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    image = models.ImageField(default="image.jpg", blank= True)



    def slice(self):
        return " ".join(self.content.split()[:3]) + "..."
    
    def slice_100(self):
        return "".join(self.content[:100]) + "..."

    # auto_now - снимок и автоматическое сохранение времеи при любом сохранении таблицы
    # auto_now_add - снимок и автоматическое схораниение времени только один раз
    # unique - указывает на обязательную уникальность занчения в стобце



class Product (models.Model):
    name = models.CharField(max_length = 150)
    price = models.FloatField()
    production_date= models.DateField()
    descreption = models.TextField()
