from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from lenta.models import Post


def add_post(request):
    if request.method == 'POST':
        data = request.POST
        post = Post.objects.create(
            image=data['image'], title=data['title'], description=data['description']
        )
        return HttpResponse('Post created')
    if request.method == 'GET':
        return render(request, 'add-post.html')
    else:
        return HttpResponse('Method not allowed')


@csrf_exempt
def show_lenta(request):
    if request.method == 'GET':
        return render(request, 'lenta.html', context={'posts': Post.objects.all()})


@csrf_exempt
def add_like(request):
    return HttpResponse(
        f"method - {request.method} <br/> <br/> header - {request.headers} <br/> <br/> body - {request.body}"
    )


@csrf_exempt
def add_comment(request):
    if request.method == 'GET':
        return render(request, 'add-comment.html')
    elif request.method == 'POST':
        if request.headers[
            'User-Agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0':
            return HttpResponse('Пользователи windows не могу загерестрироваться')
        return HttpResponse('Form submitted')
