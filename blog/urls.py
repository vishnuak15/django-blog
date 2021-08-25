from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home' ),
    path('post/<int:pk>/',PostDetialView.as_view(),name='post-detial'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('about/',views.about,name='blog-about' ),
    path('post/new/',PostCreateView.as_view(),name='post-create' ),
    
]
