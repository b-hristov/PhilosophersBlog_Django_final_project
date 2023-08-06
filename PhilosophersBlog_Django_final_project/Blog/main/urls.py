from django.urls import path, include
from .views import IndexView, PostDetailsView, CreatePostView, EditPostView, DeletePostView, CreateCommentView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailsView.as_view(), name='post_details'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/create-comment/', CreateCommentView.as_view(), name='create_comment'),
]
