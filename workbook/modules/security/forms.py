from django import forms
from django.contrib.auth.models import User
from .models import Color, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

class FormProfileImage(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super(FormProfileImage, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = "form-field"
        self.fields['image'].required = False

class FormColor(forms.ModelForm):
    primary_color = forms.CharField(max_length=10, widget=forms.HiddenInput())
    secondary_color = forms.CharField(max_length=10, widget=forms.HiddenInput())
    primary_trans_color = forms.CharField(max_length=10, widget=forms.HiddenInput())
    base_color = forms.CharField(max_length=10, widget=forms.HiddenInput())
    base_trans_color = forms.CharField(max_length=10, widget=forms.HiddenInput())
    text_color = forms.CharField(max_length=10, widget=forms.HiddenInput())
    
    class Meta:
        model = Color
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormColor, self).__init__(*args, **kwargs)
        self.fields['user'].label = ''
        self.fields['user'].label_suffix = ''
        self.fields['user'].widget.attrs['class'] = "form-field"
        self.fields['user'].widget.attrs['hidden'] = True

class FormProfile(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-field"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-field"}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"form-field"}))
    
    class Meta():
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(FormProfile, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-field"

class FormPassword(PasswordChangeForm):
    auto_password = forms.BooleanField(required=False, label='Auto generate password',widget=forms.CheckboxInput(attrs={"class":"form-field"}))

    class Meta():
        model = User
        fields = ["old_password", "new_password1", "new_password2"]

    def __init__(self, *args, **kwargs):
        super(FormPassword, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = "form-field"
        self.fields['new_password1'].widget.attrs['class'] = "form-field"
        self.fields['new_password2'].widget.attrs['class'] = "form-field"

class FormRegister(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-field"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-field"}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"form-field"}))
    auto_password = forms.BooleanField(required=False, label='Auto generate password',widget=forms.CheckboxInput(attrs={"class":"form-field"}))
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(FormRegister, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-field"
        self.fields['password1'].widget.attrs['class'] = "form-field"
        self.fields['password2'].widget.attrs['class'] = "form-field"

class FormRegisterAuto(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-field"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-field"}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"form-field"}))
    auto_password = forms.BooleanField(label='Auto generate password',widget=forms.CheckboxInput(attrs={"class":"form-field"}))
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(FormRegisterAuto, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-field"
        
class FormLogin(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-field"
        self.fields['password'].widget.attrs['class'] = "form-field"