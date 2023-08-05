from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from PhilosophersBlog_Django_final_project.Blog.accounts.models import Profile
from PhilosophersBlog_Django_final_project.Blog.accounts.widgets import ClearRedundantImageFieldsWidget
from PhilosophersBlog_Django_final_project.Blog.main.validators import validate_names

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'password1', 'password2',
                  'first_name', 'last_name',
                  'date_of_birth']

    first_name = forms.CharField(
        max_length=25,
        validators=(
            validate_names,
        )
    )

    last_name = forms.CharField(
        max_length=25,
        validators=(
            validate_names,
        )
    )

    email = forms.EmailField()

    date_of_birth = forms.DateField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if Profile.objects.filter(email=email).exists():
            raise ValidationError('This email address is already registered.')

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            # image=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            user=user,
        )

        if commit:
            user.save()
            profile.save()
        return user


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        field = ['username', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name',
        })
        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your birthday',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email address',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })

    image = forms.ImageField(widget=ClearRedundantImageFieldsWidget)
