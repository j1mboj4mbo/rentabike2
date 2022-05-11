from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BikeType, Bike, Reservation
from .forms import ReservationForm, ReservationBikeForm

def home(request):
    context = {
        'bikes': BikeType.objects.all()
    }
    return render(request, "rental/index.html", context)

def bike(request, bike_id):
    bike = BikeType.objects.get(id=bike_id)
    context = {"bike": bike}
    return render(request, 'rental/bike.html', context)

def reservation(request):
    if request.method != 'POST':
        form = ReservationForm()
    else:
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental:reservation_bike')
    context = {'form': form, 'date': request.POST}
    return render(request, 'rental/reservation.html', context)

def reservation_bikes(request):
    bikes = BikeType.objects.all()
    # if request.method != 'POST':
    #     form = ReservationBikeForm()
    # else:
    #     form = ReservationBikeForm(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('rental:index')
    context = {'bikes': bikes}
    return render(request, 'rental/reservation_bikes.html', context)

