from pyexpat import model
from django.db import models

# Create your models here.
class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active?', default=True)
    

#About Me
class AboutMeModel(Base):
    desc = models.CharField('Description', max_length=255)
#Knowledge

#Idioms

#My Skills