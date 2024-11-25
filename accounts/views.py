from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileEditForm, UserEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    #Registrar um novo usuario#
    if request.method != 'POST':
        #Formulário de registro em branco.
        form = CustomUserCreationForm()

    else:
        #Processar formulário completado.
        form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_user = form.save()
            #Logar  e direcionar o usuário para a homepage
            Profile.objects.create(user=new_user, avatar=form.cleaned_data['avatar'])
            login(request, new_user)
            return redirect('poderoso_apps:perfil')

    #Mostrar formuulário em branco ou inválido
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login(request):

    return render(request, 'registration/login.html')
# Create your views here.

@login_required
def perfil_editar(request):
    
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil atualizado')
            return redirect('poderoso_apps:perfil')
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'registration/perfil_editar.html', context)