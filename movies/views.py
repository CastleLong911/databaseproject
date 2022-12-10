from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone

from movies.models import Movie, Review
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.db.models import Sum

def ajax_get_review_popup(request):
    if request.method == 'GET':
        return HttpResponse('index.html')
    else:
        movieid = request.POST['movieid'];
        movie = Movie.objects.get(id=movieid)
        title = movie.title
        ratio = movie.ratio
        intro = movie.intro
        info = movie.info
        released_date = movie.released_date
        if str(movie.gifs) is not '':
            thumbnail = str(movie.gifs)
        else:
            thumbnail = str(movie.thumbnail)
        solution = {'title' : title, 'ratio' : ratio, 'intro' : intro, 'thumbnail' : thumbnail, 'info' : info, 'released_date' : released_date}
        return JsonResponse(solution)


def ajax_get_review_detail(request):
    if request.method == 'GET':
        return HttpResponse('index.html')
    else:
        reviews = serialize('json', Review.objects.filter(movieId=request.POST['movieid']).order_by('-created_at')[:4])

        result = {'result' : reviews}
        return JsonResponse(result)


def ajax_write_review(request):
    if request.method == 'GET':
        return HttpResponse('index.html')
    else:
        Review.objects.create(
            userId=User.objects.get(id=request.POST["userid"]),
            movieId=Movie.objects.get(id=request.POST["movieid"]),
            ratio=request.POST["ratio"],
            reviewText=request.POST["reviewtext"],
            created_at=timezone.now()
        )
        ratios = Review.objects.filter(movieId=request.POST["movieid"])
        ratio_sum = ratios.aggregate(Sum('ratio'))
        movie = Movie.objects.get(id=request.POST["movieid"])
        movie.ratio = ratio_sum['ratio__sum'] / len(ratios)
        movie.save()
        result = {"result":"good"}
        print(result)
        return JsonResponse(result)
