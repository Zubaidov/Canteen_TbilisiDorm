from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedMenuManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Menu.Status.PUBLISHED)

class Menu(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISHED = 'PB', 'PUBLISHED'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    barcode = models.IntegerField(unique=True)
    amount = models.IntegerField(default=0)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager() # The default manager.
    published = PublishedMenuManager() # Our custom manager.
    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return f"{self.title}"
