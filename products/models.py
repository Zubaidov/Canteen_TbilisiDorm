from django.db import models

class Menu(models.Model):
    barcode = models.IntegerField(unique=True)
    amount = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
