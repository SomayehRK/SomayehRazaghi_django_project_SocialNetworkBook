from django.db import models


# Create your models here.

class User(models.Model):
    GENDER_CHOICES = [('F', 'Female'), ('M', 'Male')]
    first_name = models.CharField('first name', max_length=100, null=True)
    last_name = models.CharField('last name', max_length=100, null=True, blank=True)
    username = models.CharField('username', max_length=50, unique=True)
    # user_profile = models.TextField('user profile', max_length=100)
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES, default='M')
    phone_number = models.CharField('phone number', max_length=11, blank=True)
    biography = models.CharField('biography', max_length=100, null=True)
    country = models.CharField('country', max_length=50, null=True)
    website = models.URLField('website')
    email = models.EmailField('email')
    register_date = models.DateTimeField('register date', auto_now_add=True)
    update_date = models.DateTimeField('update date')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'user name is {self.full_name} and registered at {self.register_date}'



