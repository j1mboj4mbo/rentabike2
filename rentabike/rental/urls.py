from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    #strona główna
    path('', views.home, name='index'),
    #konkretny model
    path('bikes/<int:bike_id>', views.bike, name='bike'),
    #wybor terminu
    path('reservation', views.reservation, name='reservation'),
    #rezerwacja modelu
    path('reservation/bikes', views.reservation_bikes, name='reservation_bike')
]