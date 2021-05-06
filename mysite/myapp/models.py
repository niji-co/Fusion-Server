from django.db import models

# class Dreamreal(models.Model):

#    website = models.CharField(max_length = 50)
#    mail = models.CharField(max_length = 50)
#    name = models.CharField(max_length = 50)
#    phonenumber = models.IntegerField()

#    class Meta:
#       db_table = "dreamreal"

class Hero(models.Model):
   name = models.CharField(max_length=60)
   alias = models.CharField(max_length=60)

   def __str__(self):
      return self.name