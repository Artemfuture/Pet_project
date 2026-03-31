from django.shortcuts import render
from .services import QueryService
from .utils import export_to_csv
from .models import *
from django.http import HttpResponse
from django.db.models import Count, Avg
from django.db.models.functions import ExtractYear
import csv

def drivers_view(request):
    drivers = QueryService.visits_by_driver()
    return render(request, "drivers.html", {"drivers": drivers})


def cars_view(request):
    cars = QueryService.visits_by_car()
    return render(request, "cars.html", {"cars": cars})


def garages_view(request):
    garages = QueryService.visits_by_garage()
    return render(request, "garages.html", {"garages": garages})


def visits_view(request):
    visits = QueryService.visits_flat()
    return render(request, "visits.html", {"visits": visits})


def visits_by_year_view(request):
    visits_year = QueryService.visits_by_year()
    return render(request, "visits_by_year.html", {"visits_year": visits_year})

def cards(request):
    cards = AccessCard.objects.select_related("driver").all().order_by("card_number")
    return render(request, "cards.html", {"cards": cards})


def parking(request):
    places = ParkingPlace.objects.select_related("garage").all().order_by("number_place")
    return render(request, "parking.html", {"places": places})

def cards_csv(request):
    cards = AccessCard.objects.select_related("driver").all()

    fields = [
        "id_card",
        "card_number",
        "driver",
        "is_active",
    ]

    return export_to_csv(cards, fields, "cards")

def parking_csv(request):
    places = ParkingPlace.objects.select_related("garage").all()

    fields = [
        "id_place",
        "number_place",
        "garage",
        "category",
        "place_description",
        "is_occupied",
    ]

    return export_to_csv(places, fields, "parking_places")
    
def visits_by_year_csv(request):
    data = (
        AccessLog.objects
        .annotate(year=ExtractYear("event_time"))
        .values("year")
        .annotate(
            visits_count=Count("id_log"),
            avg_duration=Avg("duration_minutes")
        )
        .order_by("year")
    )

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visits_by_year.csv"'

    writer = csv.writer(response)
    writer.writerow(["Year", "Visits count", "Average duration"])

    for row in data:
        writer.writerow([
            row["year"],
            row["visits_count"],
            round(row["avg_duration"] or 0, 2)
        ])

    return response

def cars_csv(request):
    cars = Car.objects.select_related("driver").all()

    fields = [
        "id_car",
        "number_auto",
        "vin",
        "brand",
        "year_release",
        "driver",
    ]

    return export_to_csv(cars, fields, "cars")

def drivers_csv(request):
    drivers = Driver.objects.all()

    fields = [
        "id_driver",
        "surname",
        "first_name",
        "phone",
        "email",
        "birth_date",
        "license_date",
        "driver_type",
    ]

    return export_to_csv(drivers, fields, "drivers")

def drivers_csv(request):
    drivers = Driver.objects.all()

    fields = [
        "id_driver",
        "surname",
        "first_name",
        "phone",
        "email",
        "birth_date",
        "license_date",
        "driver_type",
    ]

    return export_to_csv(drivers, fields, "drivers")

def cards_csv(request):
    cards = AccessCard.objects.select_related("driver").all()

    fields = [
        "id_card",
        "card_number",
        "driver",
        "is_active",
    ]

    return export_to_csv(cards, fields, "access_cards")


def visits_csv(request):
    logs = AccessLog.objects.select_related("car", "place", "card").all()

    fields = [
        "id_log",
        "car",
        "place",
        "card",
        "event_type",
        "event_time",
        "duration_minutes",
    ]

    return export_to_csv(logs, fields, "access_logs")

def garages_csv(request):
    garages = Garage.objects.all()

    fields = [
        "id_garage",
        "name",
        "address",
        "city",
        "floors_count",
    ]

    return export_to_csv(garages, fields, "garages")



def home_view(request):
    return render(request, "home.html")

