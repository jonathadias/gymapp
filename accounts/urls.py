from django.urls import path, include
from . import views

app_name = 'accounts'


urlpatterns = [

    #Urls padrão para autenticação
    path('', include('django.contrib.auth.urls')),
    #Página de registro
    path('register/', views.register, name='register'),

    path('login/', views.login, name='login'),

    path('perfil_editar/', views.perfil_editar, name='perfil_editar'),
]