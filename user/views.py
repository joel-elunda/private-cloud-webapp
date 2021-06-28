from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from user.forms import UserLogin, ContactForm

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        pass

    
def email_check(user):
    return user.email.endswith('@example.com')

@login_required  
@user_passes_test(email_check, login_url='/login/')
def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
    if form.is_valid():
        pass  # does nothing, just trigger the validation
    else:
        form = UserLogin()
    return render(request, 'login.html', {'form': form})




def home(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = UserLogin()
    return render(request, 'index.html', {'form': form})

class LoginCreateView(CreateView):
    pass

class RegisterCreateView(CreateView):
    pass

class UpdateCreateView(CreateView):
    # model = Author
    fields = ['name']
    template_name_suffix = '_update_form' 