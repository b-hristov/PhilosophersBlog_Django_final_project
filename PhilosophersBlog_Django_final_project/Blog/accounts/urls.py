from django.urls import path
from .views import CreateUserView, LoginView, LogOutView, ProfileView, MyPostsView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('delete_profile/', DeleteProfileView.as_view(), name='delete_profile'),
    path('posts/', MyPostsView.as_view(), name='my_posts'),
]
