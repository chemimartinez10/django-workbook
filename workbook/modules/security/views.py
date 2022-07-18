from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from modules.main.forms import FormList
from modules.main.models import Item, ListTask

from modules.security.models import Color, Profile

from .methods import generate_pwd
from .forms import FormColor, FormProfile, FormProfileImage,FormPassword, FormLogin, FormRegister, FormRegisterAuto
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/security/login')

def login(request):
    if request.user.is_authenticated:
        listas = ListTask.objects.filter(user=request.user).order_by('-id')
        last_task = Item.objects.filter(list_task__user=request.user).last()
        form_list = FormList(initial={"user": request.user})
        return render(request, 'main/index.html', {'form_list': form_list, 'listas': listas, 'last_task': last_task})
    if request.method == 'POST':
        form = FormLogin(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                auth_login(request,user)
                listas = ListTask.objects.filter(user=request.user).order_by('-id')
                last_task = Item.objects.filter(list_task__user=request.user).last()
                form_list = FormList(initial={"user": request.user})
                return render(request, 'main/index.html', {'form_list': form_list, 'listas':listas, 'last_task':last_task})
                
        else:
            print(form.errors)
    else:
        form = FormLogin()
    return render(request, 'security/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        listas = ListTask.objects.filter(user=request.user).order_by('-id')
        last_task = Item.objects.filter(list_task__user=request.user).last()
        form_list = FormList(initial={"user": request.user})
        return render(request, 'main/index.html', {'form_list': form_list, 'listas': listas, 'last_task': last_task})
    if request.method == 'POST':
        auto_pwd = request.POST.get('auto_password')
        updated_req = request.POST
        if auto_pwd == 'on':
            updated_req = request.POST.copy()
            updated_req.update({'password1': 'Avemaria12'})
            updated_req.update({'password2': 'Avemaria12'})
        form = FormRegister(updated_req)
        if form.is_valid():
            username = form.cleaned_data['username']
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            if auto_pwd == 'on':
                password = generate_pwd()
            else:
                password = form.cleaned_data['password1']
            pwd = make_password(password)

            new_user = User(username=username, first_name=fname, last_name=lname, email=email, password=pwd)
            new_user.save()
            new_profile = Profile(image='imagen', user=new_user)
            new_profile.save()
            new_color = Color(user=new_user)
            new_color.save()

            if auto_pwd == 'on':
                return render(request, 'security/password.html', {'password': password})
            return HttpResponseRedirect('login')
    else:
        form = FormRegister()

    return render(request, 'security/register.html', {'form': form})

@login_required
def profile(request):
    form_profile = FormProfile(instance=request.user)
    form_image = FormProfileImage()
    form_pass = FormPassword(request.user)
    message=""
    if request.method == 'POST':
        updated_req = request.POST
        if updated_req.get('username'):
            form_profile = FormProfile(updated_req, instance=request.user)
            old_profile=Profile.objects.filter(user=request.user)
            if not old_profile.exists():
                new_profile=Profile(user=request.user)
                new_profile.save()
            form_image = FormProfileImage(request.POST, request.FILES, instance=request.user.profile)
            if form_profile.is_valid() and form_image.is_valid():
                form_image.save()
                form_profile.save()
                redirect('security/profile.html')
            else:
                print(form_profile.errors)
        else:   
            auto_pwd = updated_req.get('auto_password')
            if auto_pwd == 'on':
                new_request = updated_req.copy()
                password = generate_pwd()
                new_request.update({'new_password1': password})
                new_request.update({'new_password2': password})
                form_pass = FormPassword(request.user, new_request)
            else:
                form_pass = FormPassword(request.user, updated_req)
            if form_pass.is_valid():
                password = form_pass.cleaned_data['new_password1']
                pwd = make_password(password)
                updated_user = User.objects.get(pk=request.user.pk)
                updated_user.password = pwd
                updated_user.save()

                if auto_pwd == 'on':
                    return render(request, 'security/password.html', {'password': password})
            else:
                print(form_pass.errors)
    form = {"form_profile":form_profile, "form_image":form_image, "form_pass":form_pass, "message":message}
    return render(request, 'security/profile.html', form)

@login_required
def settings(request):
    if request.method == 'POST':
        form_color=FormColor(request.POST, instance=request.user.color)
        if form_color.is_valid():
            form_color.save()
    my_color=Color.objects.filter(user=request.user)
    if not my_color.exists():
        new_color=Color(user=request.user)
        color_user=new_color.save()
    else:
        color_user=my_color[0]
    form_color_1 = FormColor(
        initial={'user': request.user, 'primary_color': '#6aa5ff', 'primary_trans_color': '#6aa5ff77', 'secondary_color': '#4883dd', 'base_color': '#fff', 'base_trans_color': '#fff7', 'text_color': '#000'})
    form_color_2 = FormColor(
        initial={'user': request.user, 'primary_color': '#ffa56a', 'primary_trans_color': '#ffa56a77', 'secondary_color': '#dd8348', 'base_color': '#eee', 'base_trans_color': '#eee7', 'text_color': '#111'})
    form_color_3 = FormColor(
        initial={'user': request.user, 'primary_color': '#6affa5', 'primary_trans_color': '#6affa577', 'secondary_color': '#48dd83', 'base_color': '#ddd', 'base_trans_color': '#ddd7', 'text_color': '#222'})
    form_color_4 = FormColor(
        initial={'user': request.user, 'primary_color': '#ffa5ff', 'primary_trans_color': '#ffa5ff77', 'secondary_color': '#dd83dd', 'base_color': '#fff', 'base_trans_color': '#fff7', 'text_color': '#000'})
    
    return render(request, 'security/settings.html', {'color_user':color_user,'forms_color':[form_color_1, form_color_2, form_color_3, form_color_4]})