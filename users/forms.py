from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    """
    A custom authentication form that you can customize if needed.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom fields or modify existing ones here if desired.
        # Example: Add a custom label to username field.
        self.fields['username'].label = "Username or Email" # Change label