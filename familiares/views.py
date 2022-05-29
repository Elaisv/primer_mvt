from django.shortcuts import render
from django.template import context
from familiares.models import Familia
# Create your views here.

def mostrarfamilia(request):
    familiares = Familia.objects.all()
    context = {
        "familiares" : familiares
    }
    return render(request, "familia.html", context)