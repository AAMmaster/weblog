from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from . models import User
from django.contrib.auth import authenticate




class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'username', "email", "avatar"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField(help_text='')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'username', "email", "avatar", "is_active", "is_admin"]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'avatar')

class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'نام کاربری'
    }))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder':'رمز عبور'
    }))

    def clean(self):
        cleaned_data = super().clean()
        u = cleaned_data.get('username')
        p = cleaned_data.get('password')
        if u and p:
            user = authenticate(username=u, password=p)
            if not user:
                raise forms.ValidationError('نام کاربری یا رمز عبور اشتباه است.')
            cleaned_data['user'] = user
        return cleaned_data
