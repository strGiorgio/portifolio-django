from pyexpat import model
from django.db import models

# Create your models here.
class Meta(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active?', default=True)
    

#About Me

#Knowledge

#Idioms

#My Skills