from django import forms
from .models import ListTask

class FormList(forms.ModelForm):
    
    class Meta:
        model = ListTask
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormList, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-field"
        self.fields['description'].widget.attrs['class'] = "form-field"
        self.fields['user'].label = ''
        self.fields['user'].label_suffix = ''
        self.fields['user'].widget.attrs['class'] = "form-field"
        self.fields['user'].widget.attrs['hidden'] = True
