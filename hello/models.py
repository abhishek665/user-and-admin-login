from django.db import models
# Create your  models here.


class Registration(models.Model):
    Firstname = models.CharField(max_length=10)
    Lastname = models.CharField(max_length=10)
    #num = models.IntegerField(default=0)
    Image = models.ImageField(upload_to='media', default=0)


    def __str__(self):
        return self.Firstname
