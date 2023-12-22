from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Chefs(models.Model):

    class Status(models.TextChoices):
        HEAD_CHEF = 'HEAD CHEF', 'HEAD CHEF'
        ASSISTENT = 'ASSISTENT', 'ASSISTENT'
    
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=Status.choices, default=Status.ASSISTENT)
    insta = models.CharField(max_length=255, default='https://www.instagram.com/')
    teleg = models.CharField(max_length=255, default='https://www.instagram.com/')

    def __str__(self):
        return f"{self.fname} {self.lname}"

class PublishedManager_Products(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Products.Status.PUBLISHED)

class Category(models.Model):
    name = models.CharField(max_length=255)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Products(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISHED = 'PB', 'PUBLISHED'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Chefs, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    barcode = models.IntegerField(unique=True)
    amount = models.IntegerField(default=0)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager() # The default manager.
    published = PublishedManager_Products() # Our custom manager.
    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("product", args=[self.publish.year,
                                              self.publish.month,
                                              self.publish.day,
                                              self.slug])

    

    

class PageAbout(models.Model):
    year = models.IntegerField(null=True)
    dateofstart = models.DateField(null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return f"{self.year}"