from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    # bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField(null=False, blank=False)
    # isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title