from .models import Order
from django.forms import ModelForm


class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number']
        labels = {
            "name": "your name:",
            "surname": "your surname:",
            "phone_number": "your phone number:",
        }
