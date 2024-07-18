from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

# Create your models here.
class Pizza(models.Model):
    PizzaFlavor = models.CharField(max_length=50)
    topping = models.ForeignKey("toppings", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.PizzaFlavor
    
class toppings(models.Model):
    topping_name = models.CharField(max_length=50)
    ingredients =  models.CharField(max_length=50)
    
    def __str__(self):
        return self.topping_name
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstName
    def __del__(self):
        return f"{self.firstName} is deleted"
    
class Lead(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField(blank = True, null = True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        # return self.agent.firstName
        return self.firstName

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)