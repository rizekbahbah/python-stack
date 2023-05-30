from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def form(request):
    return render(request,"index.html")

def process(request):
    request.session['name'] = request.POST['name']
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['favorite_language'] = request.POST['favorite_language']
    request.session['comments'] = request.POST['comments']
    # context = {
    # 	'name' : request.session['name'],
    # 	'dojo_location' : request.session['dojo_location'],
    # 	'favorite_language' : request.session['favorite_language'],
    # 	'comments' : request.session['comments'],
    # }
    print(request.POST)
    return redirect('/results')
