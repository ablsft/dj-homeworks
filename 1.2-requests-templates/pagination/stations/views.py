from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

import csv


class Station:
    def __init__(self, name, street, district):
        self.Name = name
        self.Street = street
        self.District = district


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = []

    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bus_stations.append(Station(row['Name'], row['Street'], row['District']))

    page_number = int(request.GET.get('page', default=1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    
    context = {
        'bus_stations': page,
        'page': page,
    }

    return render(request, 'stations/index.html', context)
