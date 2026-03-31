from django.db import models


class Driver(models.Model):
    id_driver = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=254, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    license_date = models.DateField(null=True, blank=True)
    driver_type = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.surname} {self.first_name or ''}"
    
    class Meta:
        db_table = 'drivers'
        managed = False
    
class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    number_auto = models.CharField(max_length=10)
    vin = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=50)
    year_release = models.IntegerField(null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, db_column='id_driver')

    def __str__(self):
        return self.number_auto
    class Meta:
        db_table = 'cars'  
        managed = False 
    
class Garage(models.Model):
    id_garage = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    floors_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'garages'
        managed = False
    

class ParkingPlace(models.Model):
    id_place = models.AutoField(primary_key=True)
    number_place = models.IntegerField()
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, db_column='id_garage')
    category = models.CharField(max_length=50, null=True, blank=True)
    place_description = models.CharField(max_length=100)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Place {self.number_place}"
    class Meta:
        db_table = 'parking_places'
        managed = False
    
class AccessCard(models.Model):
    id_card = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=50)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, db_column='id_driver')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.card_number
    class Meta:
        db_table = 'access_cards'
        managed = False
    

class CurrentParking(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, db_column='id_car', primary_key=True)
    place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE, db_column='id_place')
    start_time = models.DateTimeField()
    class Meta:
        db_table = 'current_parking'
        managed = False

class AccessLog(models.Model):
    id_log = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, db_column='id_car')
    place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE, db_column='id_place')
    card = models.ForeignKey(AccessCard, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_card')
    event_type = models.CharField(max_length=10)
    event_time = models.DateTimeField()
    duration_minutes = models.IntegerField(default=0)
    class Meta:
        db_table = 'access_logs'
        managed = False