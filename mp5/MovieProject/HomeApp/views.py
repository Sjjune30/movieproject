from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm
from HomeApp.models import movie
# Create your views here.
def home(request):
    moviee = movie.objects.all()
    context= {
    'key':moviee }
    return render(request,'home.html',context)
def details(request,movie_id):
    moviee = movie.objects.get(id=movie_id)
    context = {'key':moviee}
    return render(request,'details.html',context)
def add_data(request):
    if request.method =='POST':
        name = request.POST['name']
        details=request.POST['details']
        year = request.POST['year']
        image = request.FILES['image']
        moviee = movie(name = name ,details = details , year = year, image= image)
        moviee.save()
    return render(request,'add.html')
def update(request,id):
    moviee= movie.objects.get(id=id)
    form = MovieForm(request.POST or None,request.FILES,instance=moviee)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'moviee':moviee,'form':form})
def delete(request,id):
    if request.method == 'POST':
        moviee = movie.objects.get(id=id)
        moviee.delete()
        return redirect('/')
    return render(request,'delete.html')