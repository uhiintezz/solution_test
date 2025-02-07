from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, related_name='statuses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, related_name='types', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    type = models.ForeignKey(Type, related_name='categories', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, related_name='subcategories',on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='subcategories', on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.category.name} - {self.name}'


class Record(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, related_name='records', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='records', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='records', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='records', on_delete=models.CASCADE)
    write_comment = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)

