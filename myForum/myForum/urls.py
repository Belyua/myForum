from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email

from . import views


urlpatterns = [
    path('jet/', include('jet.urls')),
    path('jet/dashboard', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', views.forum_home, name='forum_home'),

    path('admin/', admin.site.urls),
    path('login/', views.logins, name='login'),

    path('<str:category>/', views.posts, name='posts'),
    path('se/', views.posts, name='services'),
    path('bi/', views.posts, name='work'),

    path('accounts/', include('allauth.urls')),
    #path('accounts/rest-auth/', include('rest_auth.urls')),
    #path('accounts/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'),

    path('<str:category>/create_topic_post/', views.create_topic_post, name='<category>_create_topic_post'),
    path('<str:category>/post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('<str:category>/post/<int:post_id>/delete_post', views.delete_post, name='post_delete')


]
