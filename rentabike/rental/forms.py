from django import forms
from .models import Reservation

class ReservationDateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date']
        widgets = {
            'date': ReservationDateInput(format=["%d-%m-%Y"]),
        }

class ReservationBikeForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['bike', 'client']
