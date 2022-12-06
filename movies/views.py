from django.http import HttpResponse
from django.http import JsonResponse
from movies.models import Movie, Review
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.db.models import Sum

def ajax_get_review_popup(request):
    if request.method == 'GET':
        return HttpResponse('index.html')
    else:
        print('movieid = '+request.POST['movieid'])
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
        print(thumbnail)
        solution = {'title' : title, 'ratio' : ratio, 'intro' : intro, 'thumbnail' : thumbnail, 'info' : info, 'released_date' : released_date}
        return JsonResponse(solution)


def ajax_get_review_detail(request):
    if request.method == 'GET':
        return HttpResponse('index.html')
    else:
        print(request.POST)
        reviews = serialize('json', Review.objects.filter(movieId=request.POST['movieid']).order_by('-created_at')[:5])
        print(reviews)

        result = {'result' : reviews}
        return JsonResponse(result)


def ajax_write_review(request):
    if request.method == 'GET':
        return HttpResponse('index.html')
    else:
        print(f'{request.POST["userid"]}, {request.POST["movieid"]}, {request.POST["ratio"]}, {request.POST["reviewtext"]}')
        Review.objects.create(
            userId=User.objects.get(id=request.POST["userid"]),
            movieId=Movie.objects.get(id=request.POST["movieid"]),
            ratio=request.POST["ratio"],
            reviewText=request.POST["reviewtext"]
        )
        ratios = Review.objects.filter(movieId=request.POST["movieid"])
        ratio_sum = ratios.aggregate(Sum('ratio'))
        movie = Movie.objects.get(id=request.POST["movieid"])
        movie.ratio = ratio_sum['ratio__sum'] / len(ratios)
        movie.save()
        print(ratio_sum['ratio__sum'] / len(ratios))
        return JsonResponse({'result' : 'good'})