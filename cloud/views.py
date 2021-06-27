from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect, request
from .forms import UploadFileForm


def home():
    return render(request, 'index.html')

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


# Téléversement de fichiers liés à un modèle¶
# Si vous enregistrez un fichier dans un Model contenant un champ FileField, 
# l’emploi d’un formulaire ModelForm simplifie le processus. 
# L’objet fichier sera enregistré à l’emplacement indiqué par le paramètre 
# upload_to du champ FileField correspondant lors de l’appel à form.save():

from cloud.forms import ModelFormWithFileField

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})




# Si vous construisez manuellement un objet, vous pouvez attribuer l’objet fichier provenant 
# de request.FILES au champ de fichier du modèle :
 
from cloud.models import ModelWithFileField

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


from django.views.generic.edit import FormView
from cloud.forms import FileFieldForm

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
'''
Fonctionnalités
===============

    1. Catégoriser les fichiers
    2. Créer des dossiers sécurisés selons les catégories ou le niveau de confidentialité 
    ...
    5. Lire les fichiers
    6. Supprimer les fichiers
    7. Protéger les fichiers où dossiers par mot de passer
    8. Cripter les fichiers
    9. Bloquer l'accès des fichiers confidentiels ou sensibles
    9. Ajouter aux favoris
    10. Afficher l'espace de stockage disponible ou restant

    11. Gérer le droit d'accès
    12. Gérer les utilisateurs

'''

class UploadCreateView(CreateView):
    pass

class FileDeleteView(DeleteView):
    # model = Author
    success_url = reverse_lazy('files-list') 

