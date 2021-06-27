from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
 

class LoginCreateView(CreateView):
    pass

class RegisterCreateView(CreateView):
    pass

class UpdateCreateView(CreateView):
    # model = Author
    fields = ['name']
    template_name_suffix = '_update_form' 