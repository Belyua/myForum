from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import PostForm, RegisterForm, LoginForm, CommentForm
from .models import Topic, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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


def create_topic_post(request, category):

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
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'topic': topic, 'form': form})


def add_comment(request, post_id):
    post = get_object_or_404(Topic, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'form': form, 'post': post})


def posts(request, category):
    topics = Topic.objects.filter(topic_link=category)
    return render(request, 'forum/posts.html', {'topics': topics, 'category': category})



def post_detail(request, category, post_id):
    post = get_object_or_404(Topic, pk=post_id)
    form = CommentForm()
    comment = Comment.objects.filter(post=post)
    #comment = Comment.objects.filter(post=post)
    # Get the first comment (or None if no comment exists)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', category=category, post_id=post_id)

    return render(request, 'post_detail.html', {'post': post, 'form': form, 'comment': comment})


#def post_detail(request, category, post_id):
    #post = Topic.objects.get(pk=post_id)
    #form = CommentForm()
    #comments = Comment.objects.get(post_id=post_id)
    #return render(request, 'post_detail.html', {'post': post, 'form': form})


@login_required
def delete_post(request, category, post_id):
    post = get_object_or_404(Topic, pk=post_id)
    if post.username != request.user.username:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post.delete()
        return redirect('posts', category=category)
    return render(request, 'forum/delete_post.html', {'post': post})





