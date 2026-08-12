from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.country}"


class Trip(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='trips')
    traveler_name = models.CharField(max_length=200)
    traveler_email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.traveler_name} -> {self.destination.name}"
