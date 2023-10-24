from django.shortcuts import render, redirect
from django.http import Http404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', default=None)

    if sort == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    elif not sort:
        phone_objects = Phone.objects.all()
    else:
        raise Http404

    template = 'catalog.html'
    context = {
        'phones': phone_objects,
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone_object, 
    }
    return render(request, template, context)
