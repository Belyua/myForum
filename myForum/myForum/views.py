from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import PostForm, RegisterForm, LoginForm
from .models import Post, Topic


def forum_home(request):
    return render(request, 'forum/home.html')


def name(request):
    if request.method == 'GET':
        topic_name = request.path.split('/')[1]
        return topic_name


def logins(request):
    form = LoginForm(request=request, data = request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
    return render(request, "forum/login.html", {"form": form})


def register(response, ):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "account created succefuly")
            return redirect("/")
        messages.error(response, "error")
        return render(response, "forum/register.html", {"form": form})
    else:
        form = RegisterForm()
        messages.warning(response, "error")
    return render(response, "forum/register.html", {"form": form})


def create_topic_post(request):
    topic_link = request.path.split('/')[1]
    print(request.path.split('/'))
    topic = Topic.objects.filter(topic_link=topic_link)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.topic = topic
            post.topic_link = topic_link
            post.save()
            return redirect('/')
            # return redirect('se', topic_slug=topic.slug)
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'topic': topic, 'form': form})


def posts(request, link):
    link = request.path.split('/')[1]
    topics = Topic.objects.filter(topic_link=link)
    print(topics)
    return render(request, 'forum/posts.html', {'topics': topics})


