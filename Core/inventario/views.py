"""importando render"""
from django.shortcuts import render
from .models import Mantenimiento, MemoriaRam
# Create your views here.

def home(request):
    """este es el home"""
    mantenimiento = Mantenimiento.objects.all()
    ram = MemoriaRam.objects.all()
    return render(request,'home.html',{'mantenimientos': mantenimiento,
                                       'ram': ram})