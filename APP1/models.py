from django.db import models

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
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstName
    
class Lead(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField(blank = True, null = True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.agent.firstName
    

    
