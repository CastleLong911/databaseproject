from django.http import HttpResponse
from django.shortcuts import render
from movies.models import Movie

def index(request):
    movies = Movie.objects.order_by('?').all()
    result = {'result' : movies}
    return render(request, 'index.html', result)
