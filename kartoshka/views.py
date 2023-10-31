from django.shortcuts import render
from . import models

def vivod_price_potatoes(request):
    data = models.Kartoshka.objects.all()
    return render(request, 'index.html', {'posts': data} )


