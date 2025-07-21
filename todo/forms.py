from django import forms
from todo.models import Contact
from django.contrib.auth.models import User


class LoginForms(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Fuad"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}
        ),
        max_length=250,
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}
        ),
        max_length=250,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm your password"}
        ),
        max_length=250,
        label="Confirm your password",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password2")

        # Şifrələr uyğun olmalıdır
        if password != confirm_password:
            raise forms.ValidationError("Şifrələr uyğun deyil.")
        return cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "name"}),
            "email": forms.TextInput(attrs={"placeholder": "email"}),
            "phone": forms.TextInput(attrs={"placeholder": "phone"}),
            "message": forms.TextInput(
                attrs={"placeholder": "message", "class": "message-box"}
            ),
        }
