from django.shortcuts import render,redirect
from . import models
# Create your views here.

def index(request):
    context = {
        "dojos": models.Dojo.objects.all(),
        "ninjas": models.Ninja.objects.all()
    }
    return render(request,'index.html', context)

def add_dojo(request):
    Dojo_name = request.POST['boxn']
    Dojo_city = request.POST['boxc']
    Dojo_state = request.POST['boxs']
    models.Dojo.objects.create(name=Dojo_name,city=Dojo_city,state=Dojo_state)
    return redirect("/")

def add_ninja(request):
    Ninja_first_name = request.POST['boxn1']
    Ninja_last_name= request.POST['boxc1']
    Dojo_name = request.POST['boxs1']
    dojo_foreign = models.Dojo.objects.get(name=Dojo_name)
    models.Ninja.objects.create(first_name=Ninja_first_name,last_name=Ninja_last_name, dojo=dojo_foreign)
    return redirect("/")
