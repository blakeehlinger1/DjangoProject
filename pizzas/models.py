from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
#error with pizza cant find pizzas_pizza

    def __str__(self):
        return self.text


class Topping(models.Model):
    #topic = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)

    

    def __str__(self):
        return f"{self.text[:50]}..."