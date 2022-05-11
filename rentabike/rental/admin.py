from django.contrib import admin
from .models import BikeType, Bike, Reservation

admin.site.register(BikeType)
admin.site.register(Bike)
admin.site.register(Reservation)

