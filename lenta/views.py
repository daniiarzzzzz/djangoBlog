from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from lenta.forms import PostForm
from lenta.models import Post


class PostView(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'lenta.html'


class PostCreateView(generic.CreateView):
    template_name = 'add-post.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            return render(request, self.template_name, context={'form': form})
        return render(request, self.template_name, context={'form': form})


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


class PostDetailView(generic.DetailView):
    template_name = 'post-detail.html'
    model = Post


def detail_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
        return render(request, 'post-detail.html', context={'post': post})
    except Post.DoesNotExist:
        return HttpResponse('Does Not Exist!', status=404)


def edit_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return HttpResponse('Does Not Exist!', status=404)
    if request.method == 'GET':
        return render(request, 'edit-post.html', context={'post': post})
    if request.method in 'POST':
        data = request.POST
        if 'image' in data:
            post.image = data['image']
        if 'description' in data:
            post.description = data['description']
        if 'title' in data:
            post.title = data['title']

        post.save()
        return render(request, 'edit-post.html', context={'post': post})


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
