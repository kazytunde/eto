from django.db import models


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    amount = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
