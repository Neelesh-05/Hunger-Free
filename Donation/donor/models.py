from django.db import models

# Create your models here.
class donormodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phoneno = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "donormodel"   

class donorModels(models.Model):
    selleremail = models.CharField(max_length=100)
    cropname = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    location = models.CharField(max_length=100000)
    file = models.FileField(upload_to='post_images/')
    cdate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = "donorstable"

class Acceptmodel(models.Model):
    uid = models.IntegerField()
    email = models.EmailField()
    associated_email=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'Acceptmodel'


class OurAchivements(models.Model):
    file = models.FileField(upload_to='post_images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'OurAchivements'
