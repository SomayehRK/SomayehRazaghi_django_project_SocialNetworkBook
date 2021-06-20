from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField('book name', max_length=100)
