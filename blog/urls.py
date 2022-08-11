from . import views
from django.urls import path
from .views import PostList, PostView, AddPost


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('view/<int:pk>', views.PostView.as_view(), name='post_view'),
    path('add_post/', views.AddPost.as_view(), name="add_post")
]
