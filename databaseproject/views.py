from django.http import HttpResponse
from django.shortcuts import render
from movies.models import Movie

def index(request):
    movies = Movie.objects.order_by('?').all()
    print(movies)
    randMovie = movies[13]
    print(randMovie.thumbnail, randMovie.title)
    result = {'result' : movies, 'thumbnail' : randMovie.thumbnail, 'title' : randMovie.title, 'ratio' : randMovie.ratio, 'id' : randMovie.id}
    return render(request, 'index.html', result)

def search(request):
    keyword = request.GET.get('keyword',None)
    print(keyword)
    movies = Movie.objects.filter(title__contains=keyword)
    result = {'result' : movies, 'keyword' : keyword}
    return render(request, 'search.html', result)