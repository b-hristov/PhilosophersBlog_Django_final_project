from django.urls import path, include
from .views import IndexView, PostDetailsView, CreatePostView, EditPostView, DeletePostView, CreateCommentView, \
    EditCommentView, DeleteCommentView, LikeView, SearchView, CategoryView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailsView.as_view(), name='post_details'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/create-comment/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/edit/', EditCommentView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
    path('post/<int:pk>/like/', LikeView.as_view(), name='like_post'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<slug:category_slug>/', CategoryView.as_view(), name='category_view'),
]
