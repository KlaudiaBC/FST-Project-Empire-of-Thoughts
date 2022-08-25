"""
Define the URLs for the 'blog' application
"""
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/post/<int:pk>', views.PostView.as_view(), name='post_view'),
    path('blog/add_post/', views.AddPost.as_view(), name="add_post"),
    path('blog/edit/<int:pk>', views.UpdatePost.as_view(), name="update_post"),
    path('blog/delete/<int:pk>', views.DeletePost.as_view(),
         name="delete_post"),
    path('blog/like/<int:pk>', views.like_click, name="like_post"),
    path('blog/view/<int:pk>/comment',
         views.AddComment.as_view(), name="add_comment"),
    path('blog/category/<str:cats>', views.category_list, name="category"),
    path('blog/category-list/', views.category_list_view,
         name="category_list"),
    path('blog/post/<int:pk>/comment', views.AddComment.as_view(),
         name="add_comment"),
    path('blog/mypage/', views.MyPosts.as_view(), name='my_page'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'), name="members_urls"),
    ]
