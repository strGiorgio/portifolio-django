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
class KnowledgesModel(Base):
    title = models.CharField("Title", max_length=64)
    desc = models.CharField("Description", max_length=525)

    def __str__(self):
        return f'{self.title}'


#Idioms
class IdiomsModel(Base):
    level_choices = (
        ('Advanced', 'Advanced'),
        ('Intermediary', 'Intermediary'),
        ('Basic', 'Basic')
    )
    lang = models.CharField('Language', max_length=64)
    level = models.CharField('Level', max_length=64, choices=level_choices)

    def __str__(self):
        return f'{self.lang}'


#My Skills
class SkillsModel(Base):
    percentage_choices = (
        ('5', '5%'), ('10', '10%'), ('15', '15%'), ('20', '20%'), ('25', '25%'), ('30', '30%'), ('35', '35%'),
        ('40', '40%'), ('45', '45%'), ('50', '50%'), ('55', '55%'), ('60', '60%'), ('65', '65%'), ('70', '70%'),
        ('75', '75%'), ('80', '80%'), ('85', '85%'),  ('90', '90%'), ('95', '95%'), ('100', '100%')
    )
    skill = models.CharField('Skill', max_length=64)
    percentage = models.CharField('Percentage', max_length=10, choices=percentage_choices)

    def __str__(self):
        return f'{self.skill}'


class UsersMessages(Base):
    name = models.CharField('Name', max_length=128)
    email = models.EmailField('Email', max_length=128)
    subject = models.CharField('Subject', max_length=24)
    message = models.CharField('Message', max_length=780)


    class Meta:
        verbose_name = 'UsersMessages'

    def __str__(self):
        return f'Message from: {self.name}'
