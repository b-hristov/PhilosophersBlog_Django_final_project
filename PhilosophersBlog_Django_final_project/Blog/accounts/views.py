from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm, LoginForm
from .models import Profile

UserModel = get_user_model()


class CreateUserView(CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url


class LogOutView(LogoutView):
    next_page = reverse_lazy('index')

