from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Pizza)
admin.site.register(models.toppings)
admin.site.register(models.Lead)
admin.site.register(models.Agent)
