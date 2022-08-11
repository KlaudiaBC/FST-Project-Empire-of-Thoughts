from . import views
from django.urls import path
from .views import PostList, PostView, AddPost, UpdatePost


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('view/<int:pk>', views.PostView.as_view(), name='post_view'),
    path('add_post/', views.AddPost.as_view(), name="add_post"),
    path('edit/<int:pk>', views.UpdatePost.as_view(), name="update"),
]
