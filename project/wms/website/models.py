from django.db import models

user_types = (
    (0, "manager"),
    (1, "worker"),
    (2, "Customer"))

categories=(
        (0,"Photographic products"),
        (1,"Writing Tools"),)

class user(models.Model):
    

    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50)
    role=models.IntegerField(choices=user_types, default=3)
    status=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} is a {self.role}"

    def role_redirect(self):
        return user_types[self.role][1]

class products(models.Model):
    
    sku=models.IntegerField(unique=True)
    name=models.CharField(max_length=50 ,unique=True)
    price=models.FloatField()
    descprition=models.CharField(max_length=200)
    category=models.IntegerField(categories)

