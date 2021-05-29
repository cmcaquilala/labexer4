from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name

class Book(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=False)
    year = models.CharField(max_length=6, null=True, blank=False)
    category = models.CharField(max_length=100, null=True, blank=False)
    price = models.IntegerField(null=True)
    pages = models.IntegerField(null=True)
    language = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.title