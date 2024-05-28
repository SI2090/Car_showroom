from django.http import Http404
from django.shortcuts import render
from .models import Car, Sale

def cars_list_view(request):
    cars = Car.objects.all()
    template_name = 'main/list.html'
    context = {
        'cars': cars,
    }
    return render(request, template_name, context)

def car_details_view(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404('Автомобиль не найден')
    template_name = 'main/details.html'
    context = {
        'car': car,
    }
    return render(request, template_name, context)

def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car)
    except Car.DoesNotExist:
        raise Http404('Автомобиль не найден')
    template_name = 'main/sales.html'
    context = {
        'car': car,
        'sales': sales,
    }
    return render(request, template_name, context)

