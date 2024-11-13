from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    #Registrar um novo usuario#
    if request.method != 'POST':
        #Formulário de registro em branco.
        form = UserCreationForm()
    else:
        #Processar formulário completado.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Logar  e direcionar o usuário para a homepage
            login(request, new_user)
            return redirect('poderoso_apps:index')

    #Mostrar formuulário em branco ou inválido
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login(request):

    return render(request, 'registration/login.html')
# Create your views here.
