from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as UserProfile


class UserCreateForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField(required=True, help_text='user@example.com')
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
