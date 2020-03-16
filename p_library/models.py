from django.db import models

# Create your models here.

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)


class Publisher(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    publisher = models.ForeignKey(Publisher, to_field="name", default="AST", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


