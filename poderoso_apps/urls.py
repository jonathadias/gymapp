# Importa o módulo path que facilita a definição de URLs.
from django.urls import path  
# Importa as views que contêm a lógica de cada página.
from . import views  

# Define o namespace da aplicação para que as URLs possam ser referenciadas de maneira única.
app_name = 'poderoso_apps'  

# Lista de padrões de URL que a aplicação pode responder.
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),  # Quando o usuário acessa a raiz do site, chama a função index na views.

    # Página com Tópicos
    path('topics/', views.topics, name='topics'),  # Quando o usuário acessa /topics/, chama a função topics.

    # Página com Tópico detalhado
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # Captura um ID de tópico e chama a função topic com esse ID.

    # Criação de novo tópico
    path('new_topic/', views.new_topic, name='new_topic'),  # Acessa /new_topic/ para criar um novo tópico, chamando new_topic.

    # Criação do texto do tópico
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  # Permite criar uma nova entrada para um tópico específico.

    # Edição dos tópicos inseridos
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Permite editar uma entrada existente, capturando seu ID.

    # Exibição da lista de planos de treino
    path('planos_treinos/', views.planos_treinos, name='planos_treinos'),  # Acessa /planos_treino/ para exibir todos os planos de treino.

    # Exibição dos detalhes de um plano de treino
    path('detalhes_plano/', views.detalhes_planos, name='detalhes_plano'),  # Acessa /detalhes_plano/ para mostrar os detalhes de um plano específico.

]
