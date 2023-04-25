from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, Topic, Section
def forum_home(request):
    return render(request, 'forum/home.html')

def posts(request):
     return render(request, 'forum/posts.html')

def se(request):

    return render(request, 'forum/se.html')


def name(request):
    if request.method == 'GET':
        topic_name = request.path.split('/')[-2]
        return topic_name


def create_topic_post(request):
    topic_link = request.path.split('/')[1]
    print(request.path.split('/'))
    topic = Topic.objects.get_or_create(topic_link=topic_link)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.topic = topic
            post.save()
            return redirect('/')
            # return redirect('se', topic_slug=topic.slug)
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'topic': topic, 'form': form})




# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('home')
#     else:
#         form = PostForm()
#     return render(request, 'create_post.html', {'form': form})

