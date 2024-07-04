from django.shortcuts import render
from .models import Property

def homepage(request):
    featured_listings = Property.objects.all()[:5]
    return render(request, 'listings/homepage.html', {'featured_listings': featured_listings})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'listings/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})
