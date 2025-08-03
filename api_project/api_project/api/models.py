from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField()
    cover_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

#model for farm produce for an Agric marketplace: name, type, quantity, shelf_life, price, farmer, available"
class FarmProduce(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    shelf_life = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    farmer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# class FarmProduce(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity_available = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    
