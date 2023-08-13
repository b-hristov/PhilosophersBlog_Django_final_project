import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RegisterUserForm, LoginForm, EditProfileForm
from .models import Profile, BlogUser
from ..main.models import Post

UserModel = get_user_model()


class CreateUserView(CreateView):
    template_name = 'profile/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class LoginView(LoginView):
    template_name = 'profile/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url


class LogOutView(LogoutView):
    next_page = reverse_lazy('index')


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile/profile.html'

    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        posts = Post.objects.filter(user=request.user).order_by('-created_on')
        return render(request, self.template_name, {'profile': profile, 'posts': posts})


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        if 'image' in self.request.FILES:
            profile.image = self.request.FILES['image']
        profile.save()
        return super().form_valid(form)


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = BlogUser
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        profile = self.object.profile

        image_path = profile.image.path
        if image_path and os.path.exists(image_path):
            os.remove(image_path)

        profile.delete()
        self.object.delete()
        return redirect(self.success_url)


class MyPostsView(LoginRequiredMixin, ListView):
    template_name = 'profile/my-posts.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user=user).order_by('-created_on')

