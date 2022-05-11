from django.db import models

class BikeType(models.Model):
    """Typy rowerów, które są dostępne do wypożyczenia"""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def find_free_bike_for_date(self, date):
        return Bike.objects.filter(biketype=self).exclude(reservation__date=date).first()

class Bike(models.Model):
    """Konkretne modele rowerów"""
    biketype = models.ForeignKey(BikeType, on_delete=models.CASCADE)
    serialnumber = models.CharField(max_length=100)

    def __str__(self):
        return str(self.serialnumber)


class Reservation(models.Model):
    """Terminy rezerwacji z numerem seryjnym i datą"""
    bike = models.ForeignKey(Bike, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField()
    client = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bike} zarezerwowany na {self.date} przez {self.client}."
