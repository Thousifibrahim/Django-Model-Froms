from django.shortcuts import render,redirect

# view.py
from .models import Movie
from .forms import MovieForm

def display(request):
    tb = Movie.objects.all()
    return render(request, 'display.html', {'table': tb})


def addmovie(request):
    add = MovieForm()
    context = {
        'ad': add
    }
    if request.method == 'POST':
        add = MovieForm(data=request.POST)
        if add.is_valid():
            add.save()
            return redirect('table')
    return render(request, 'addmovie.html', context)



def update(request, id):
    obj = Movie.objects.get(id=id)
    if request.method == 'POST':
        fm = MovieForm(instance=obj, data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('table')
    else:
        fm = MovieForm(instance=obj)
    return render(request, 'update.html', {'updateforms': fm})



def delete(request, id):
    dl = Movie.objects.get(id=id)
    dl.delete()
    return redirect('table')