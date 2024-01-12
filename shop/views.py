from django.shortcuts import render, redirect
from django.views import View, generic
from django.views.generic.detail import DetailView
from .models import *
from .forms import OrderModelForm
from django.views.generic.edit import FormView

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'shop/bikes.html'
    context_object_name = 'bikes'

    def get_queryset(self):
        return Bike.objects.all()


class BikeView(View):
    # Global form to use in methods
    form = OrderModelForm

    def get(self, request, pk, *args, **kwargs):
        # Set up
        pk = self.kwargs['pk']
        form = self.form
        bike = Bike.objects.filter(id=pk).first()

        # Check if available, render with form anyway but pass a boolean to the context
        frames = Frame.objects.filter(color=bike.frame.color).first()
        seats = Seat.objects.filter(color=bike.seat.color).first()
        tires = Tire.objects.filter(type=bike.tire.type).first()
        baskets = Basket.objects.all().first()
        check_list = [frames, seats, baskets]

        is_available = True
        for item in check_list:
            if item.quantity < 1:
                is_available = False
                break

        if is_available:
            if tires.quantity < 2:
                is_available = False

        context = {'bike': bike, 'form': form, 'is_available': is_available}
        return render(request, 'bikedetails.html', context=context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        pk = self.kwargs['pk']

        if form.is_valid():
            bike = Bike.objects.filter(id=pk).first()
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            phone_number = form.cleaned_data['phone_number']

            # Substract the used materials
            frames = Frame.objects.filter(color=bike.frame.color).first()
            seats = Seat.objects.filter(color=bike.seat.color).first()
            tires = Tire.objects.filter(type=bike.tire.type).first()
            baskets = Basket.objects.all().first()

            frames.quantity -= 1
            frames.save()
            seats.quantity -= 1
            seats.save()
            tires.quantity -= 2
            tires.save()
            baskets.quantity -= 1
            baskets.save()

            # Order creation
            order = Order.objects.create(
                bike=bike, name=name, surname=surname, phone_number=phone_number, status='P'
            )
            order_no = order.pk

            # Go to order/order_no/
            return redirect(f'/order/{order_no}/')


class OrderView(View):
    def get(self, request, order_no, *args, **kwargs):
        order_no = self.kwargs['order_no']
        context = {'order_no': order_no}
        return render(request, 'orderdetails.html', context=context)
