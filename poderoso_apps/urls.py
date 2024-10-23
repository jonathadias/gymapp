#URL DA PODEROSO_APPS#

from django.urls import path
from . import views

app_name = 'poderoso_apps'

urlpatterns = [
    #Home Page#
    path('', views.index, name='index'),
    #Pagina com Tópicos
    path('topics/', views.topics, name='topics'),
    #Pagina com Tópico detalhado
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Criação de novo tópico
    path('new_topic/', views.new_topic, name='new_topic'),
    #Criação do texto do tópico
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Edição dos tópicos inseridos
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


]
