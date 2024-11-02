from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=100)
    exported_to = models.JSONField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    img = models.URLField(max_length=500, blank=True, null=True)  # Add image URL field here

    def __str__(self):
        return self.name
