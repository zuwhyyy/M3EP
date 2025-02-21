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