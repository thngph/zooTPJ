from django.urls import path
from . import views
from .models import Event
# from .views import post_detail, news_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('post/<int:event_id>', views.post_main, name='post'),
    path('post/comment', views.post_comment, name="comment"),
    path('post/delete', views.delete_comment, name="delete"),
    # path('', news_list.as_view(), name='news_list'),
    # path('/post/<int:pk>', post_detail.as_view(), name='post_detail'),
]
