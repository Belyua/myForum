
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('jet/', include('jet.urls')),
    path('jet/dashboard', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', views.forum_home, name='forum_home'),
    path('admin/', admin.site.urls),
    path('se/', views.posts, name='services'),
    path('se/create_topic_post/', views.create_topic_post, name='create_topic_post'),
    # path('se/<str:topic_slug>/', views.se, name='se'),
    # path('se/<str:topic_slug>/create_post/', views.create_topic_post, name='create_topic_post'),

]
