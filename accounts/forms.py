from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ("username", "email",) + UserCreationForm.Meta.fields[2:]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está en uso.")
        return email
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')