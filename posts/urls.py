from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("drivers/", views.drivers_view, name="drivers"),
    path("garages/", views.garages_view, name="garages"),
    path("visits/", views.visits_view, name="visits"),
    path("visits_by_year/", views.visits_by_year_view, name="visits_by_year"),
    path("cars/", views.cars_view, name="cars"),
    path("cards/", views.cards, name="cards"),
    path("parking/", views.parking, name="parking"),
    path("cars/csv/", views.cars_csv, name="cars_csv"),
    path("drivers/csv/", views.drivers_csv, name="drivers_csv"),
    path("parking/csv/", views.parking_csv, name="parking_csv"),
    path("cards/csv/", views.cards_csv, name="cards_csv"),
    path("visits/csv/", views.visits_csv, name="visits_csv"),
    path("garages/csv/", views.garages_csv, name="garages_csv"),
    path("visits_by_year/csv/", views.visits_by_year_csv, name="visits_by_year_csv"),
]