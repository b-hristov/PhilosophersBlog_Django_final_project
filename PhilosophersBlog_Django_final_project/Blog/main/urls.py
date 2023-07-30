from django.urls import path, include
from .views import IndexView, PostDetailsView, CreatePostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailsView.as_view(), name='post_details'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
]
