from django.db import models


class Owner(models.Model):
    name = models.CharField(max_lenght=128)


    def __str__(self):
        return f'{self.race} {self.name}'




class Dog(models.Model):
    SEX_CHOICES = (
        ('M', 'pies'),
        ('f', 'suczka'),
        ('x', 'nieznane'),
    )
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    race = models.CharField(max_length=128)
    sex = models.CharField(max_length=1,default='x')
    owner = models.ForeignKey(Owner,null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.race} {self.name}'


