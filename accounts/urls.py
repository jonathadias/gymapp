from django.urls import path, include
from . import views

app_name = 'accounts'


urlpatterns = [

    #Urls padrão para autenticação
    path('', include('django.contrib.auth.urls')),
    #Página de registro
    path('register/', views.register, name='register'),

]