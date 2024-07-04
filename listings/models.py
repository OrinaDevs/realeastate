from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    property_type = models.CharField(max_length=100, choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Commercial', 'Commercial')])
    amenities = models.TextField()
    image = models.ImageField(upload_to='properties/')
    video_tour = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title