from django import forms
from .models import CustomUser

# from django.contrib.auth.hashers import make_password


class SignInForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    email = forms.CharField(
        max_length=32,
        widget=forms.EmailInput(attrs={"placeholder": "enter your email"}),
    )
    password = forms.CharField(
        max_length=32, widget=forms.PasswordInput(attrs={"placeholder": "password"})
    )

    def clean(self):

        email = self.cleaned_data.get("email")
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError({"email": ["unexsiting account"]})

        password = self.cleaned_data.get("password")
        if not CustomUser.objects.filter(password=password).exists():
            raise forms.ValidationError({"password": ["wrong password"]})

    def get_user(self):
        return CustomUser.objects.get(email=self.cleaned_data.get("email"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "phone_number", "password"]

    email = forms.CharField(
        max_length=32,
        widget=forms.EmailInput(attrs={"placeholder": "enter your email"}),
    )
    password = forms.CharField(
        max_length=32, widget=forms.PasswordInput(attrs={"placeholder": "password"})
    )

    phone_number = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={"placeholder": "enter your phone number"}),
    )

    confirm_password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(attrs={"placeholder": "confirm your password"}),
    )
    #

    def clean(self):

        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError({"email": ["used email"]})

        phone_number = self.cleaned_data.get("phone_number")
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError({"email": ["used phone number"]})

        # same password
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                {
                    "password": ["passwords must be indentical"],
                    "confirm_password": ["passwords must be indentical"],
                }
            )

    def save(self, commit=True):
        # Create a new CustomUser instance
        user = super().save(commit=False)
        user.password = user.password
        # You can perform additional actions here if needed
        if commit:
            user.save()

        return user
