
from django.urls import path
from .views import CreateUserView, LoginView, LogOutView, ProfileView, MyPostsView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('posts/', MyPostsView.as_view(), name='my_posts'),
]
