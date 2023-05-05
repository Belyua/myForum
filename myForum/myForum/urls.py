from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('jet/', include('jet.urls')),
    path('jet/dashboard', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', views.forum_home, name='forum_home'),
    path('admin/', admin.site.urls),
    path('login/', views.logins, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('se/', views.posts, name='services'),
    path('bi/', views.posts, name='work'),
    # path('create_topic_post/', views.create_topic_post, name='create_topic_post'),
    # добавить новый маршрут для создания топика
    path('se/create_topic_post/', views.create_topic_post, name='se_create_topic_post'),
    path('bi/create_topic_post/', views.create_topic_post, name='bi_create_topic_post'),

]
