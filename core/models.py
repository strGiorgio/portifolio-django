from pyexpat import model
from django.db import models

# Create your models here.
class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True
    

#About Me
class AboutMeModel(Base):
    desc = models.CharField('Description', max_length=525)

    def __str__(self):
        return 'My Description'
#Knowledge

#Idioms
class IdiomsModel(Base):
    level_choices = (
        ('Advanced', 'Advanced'),
        ('Intermediary', 'Intermediary'),
        ('Basic', 'Basic')
    )
    lang = models.CharField('Language', max_length=64)
    level = models.CharField('Level', max_length=64, choices=level_choices)

#My Skills