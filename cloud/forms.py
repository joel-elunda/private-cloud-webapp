from django import forms 
from cloud.models import Upload

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['file']

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class ModelFormWithFileField(forms.Form):
    print('')
    pass

class FileFieldForm(forms.Form):
    pass 