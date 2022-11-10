from django.db import models

# Create your models here.
class UserLogin(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    @staticmethod
    def verify_user(email):
        res = UserLogin.objects.filter(email= email)
        return res
    

    
class Products(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="uploads/products/", null=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all():
        return Products.objects.all()
    

class Messages(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.name