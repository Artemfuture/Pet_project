from django.contrib import admin
from .models import Driver, Car, Garage, ParkingPlace, AccessCard, CurrentParking, AccessLog

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Garage)
admin.site.register(ParkingPlace)
admin.site.register(AccessCard)
admin.site.register(CurrentParking)
admin.site.register(AccessLog)
