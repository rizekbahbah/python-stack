from django.shortcuts import render, redirect
from.models import dojo, ninjas


def index(request):
    context = {
        "all_ninjas": ninjas.objects.all(),
        "all_dojos": dojo.objects.all()
    }
    return render(request, "index.html", context)

def process_dojo(request):

    dojo_name = request.POST['name']
    dojo_city = request.POST['city']
    dojo_state = request.POST['state']
    dojo.objects.create(name=dojo_name, city=dojo_city, state=dojo_state)
    return redirect('/')
def process_user(request):
    ninja_fname = request.POST['first_name']
    ninja_lname = request.POST['last_name']
    
    
    dojo_var = dojo.objects.get(id=request.POST['dojo'])
    ninjas.objects.create(dojo=dojo_var, first_name=ninja_fname, last_name=ninja_lname)
    return redirect('/')