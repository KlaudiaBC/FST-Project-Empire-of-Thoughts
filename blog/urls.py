"""
Define the URLs for the 'blog' application
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>', views.PostView.as_view(), name='post_view'),
    path('add_post/', views.AddPost.as_view(), name="add_post"),
    path('edit/<int:pk>', views.UpdatePost.as_view(), name="update_post"),
    path('delete/<int:pk>', views.DeletePost.as_view(), name="delete_post"),
    path('like/<int:pk>', views.LikeClick, name="like_post"),
    path('view/<int:pk>/comment',
         views.AddComment.as_view(), name="add_comment"),
    path('category/<str:cats>', views.CategoryList, name="category"),
    path('category-list/', views.CategoryListView, name="category_list"),
    ]
