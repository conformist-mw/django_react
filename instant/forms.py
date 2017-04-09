from io import BytesIO
from django import forms
from django.template.defaultfilters import filesizeformat
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as UserProfile

MIN_SIZE = 51200
MAX_SIZE = 2097152


class RestrictedImageField(forms.ImageField):
    default_error_messages = {
        'invalid_image': (
            'Некорректный формат файла, поддерживаемые форматы: JPG, BMP, PNG, TIFF'),
    }

    def __init__(self, *args, **kwargs):
        self.min_upload_size = MIN_SIZE
        self.max_upload_size = MAX_SIZE
        super(RestrictedImageField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(RestrictedImageField, self).clean(*args, **kwargs)
        if self.min_upload_size > data.size:
            raise forms.ValidationError('Размер файла ({}) слишком мал для распознавания изображения. Минимум {}'.format(
                filesizeformat(data.size), filesizeformat(self.min_upload_size)))
        elif self.max_upload_size < data.size:
            raise forms.ValidationError('Размер файла ({}) превышает максимальный размер. Максимум {}'.format(
                filesizeformat(data.size), filesizeformat(self.max_upload_size)))
        return data

    def to_python(self, data):
        f = super(RestrictedImageField, self).to_python(data)
        if f is None:
            return None
        from PIL import Image
        if hasattr(data, 'temporary_file_path'):
            file = data.temporary_file_path()
        else:
            if hasattr(data, 'read'):
                file = BytesIO(data.read())
            else:
                file = BytesIO(data['content'])
        try:
            image = Image.open(file)
            if image.format not in ('JPEG', 'BMP', 'PNG', 'TIFF'):
                raise forms.ValidationError(
                    'Некорректный формат файла, поддерживаемые форматы: JPG, BMP, PNG, TIFF')
            image.verify()
            f.image = image
            f.content_type = Image.MIME.get(image.format)
        except Exception:
            raise forms.ValidationError('Некорректный формат файла.')
        if hasattr(f, 'seek') and callable(f.seek):
            f.seek(0)
        return f


class UserCreateForm(UserCreationForm):
    username = forms.CharField(help_text='Allowed symbols: only letters, numbers, and @/./+/-/_ characters')
    email = forms.EmailField(required=False, help_text='user@example.com')
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('username', 'password1',
                  'password2', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class FeedBack(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='E-mail', max_length=254)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    image = RestrictedImageField()
