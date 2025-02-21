from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=300, default='default')
    country = models.CharField(max_length=300, default='default')
    city = models.CharField(max_length=300, default='default')
    created_at = models.DateTimeField(blank=True, null=True)

    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name + " - " + self.city + ", " + self.country + " created at: " + str(self.created_at)

class WaterBottle(models.Model):
    sku = models.CharField(max_length=12, unique=True) #stock keeping unit usually have 8-12 digits
    brand = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100)
    mouth_size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    supplied_by = models.ForeignKey(Supplier,on_delete=models.SET_NULL, null=True, blank=True)
    current_quantity = models.IntegerField()

    def __str__(self):
        return f"SKU: {self.sku}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, {self.supplied_by}, {self.cost}: {self.current_quantity}"
    
