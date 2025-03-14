from django.db import models

# Create your models here.
class Usermodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phoneno = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "usermodel"

class requestdonorModels(models.Model):
    selleremail = models.CharField(max_length=100)
    cropname = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    date = models.DateTimeField(max_length=100)

    def __str__(self):
        return self.selleremail

    class Meta:
        db_table = "requestdonorModels"