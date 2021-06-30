from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test, login_required 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from user.forms import UserLogin, ContactForm
from django.contrib.auth import logout

def logout_view(request):
    logout(request)

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
 
@user_passes_test(email_check, login_url='/accounts/login/')
@login_required(login_url='/accounts/login/')
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user) 
    else:
        form = UserLogin()
    return render(request, 'login.html', {'form': form})
 
def home(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

class UpdateCreateView(CreateView):
    # model = Author
    fields = ['name']
    template_name_suffix = '_update_form' 