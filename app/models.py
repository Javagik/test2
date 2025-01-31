from django.db import models
from django.urls import reverse
from django.conf import settings

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Content(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.FloatField()
    pub_date = models.DateTimeField()
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("content_detail" , kwargs={"pk": self.pk})

class Unit(models.Model):
    name = models.CharField(max_length=50)
    content = models.ManyToManyField(Content)
