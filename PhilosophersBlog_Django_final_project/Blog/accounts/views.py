from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm


class CreateUserView(CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Check if the email address is unique
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'This email address is already registered.')
            return self.form_invalid(form)

        user = form.save(commit=False)

        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(self.request, user)

        return super().form_valid(form)


class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')

