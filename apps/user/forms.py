from django import forms

from apps.user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=255)
    password = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput)

    def clean_email(self):
        email =self.cleaned_data['email']
        check = User.objects.filter(email=email)
        if check:
            raise forms.ValidationError("User with this email already exists")
        return email

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password_confirm == password:
            return password_confirm
        raise forms.ValidationError("Passwords do not match")


    class Meta:
        model = User
        fields = ['username',
                  'image',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'password',
                  'password_confirm',
                  'about']
