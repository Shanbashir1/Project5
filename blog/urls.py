from django.urls import path
from .import views
from .views import PostList



urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('<str:slug>/', views.post_blog, name='post_blog'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('editBlog/<slug:slug>/', views.editBlog, name='edit_blog'),
    path('deleteBlog/<slug:slug>/', views.deleteBlog, name='delete_blog'),
    path('addBlog', views.addBlog, name='add_blog'), 
]
