# Importa o módulo admin do Django, que fornece funcionalidades para criar interfaces administrativas.
from django.contrib import admin  
# Importa os modelos que serão registrados no painel administrativo.
from .models import Topic, Entry, PlanoTreino, Exercicio
from accounts.models import Profile

# Registra o modelo Topic no painel administrativo do Django.
admin.site.register(Topic)  
# Registra o modelo Entry no painel administrativo do Django.
admin.site.register(Entry)  
# Registra o modelo PlanoTreino no painel administrativo do Django.
admin.site.register(PlanoTreino)  
# Registra o modelo Exercicio no painel administrativo do Django.
admin.site.register(Exercicio)  
# Comentário indicando que aqui é o local para registrar modelos adicionais, se necessário.
admin.site.register(Profile)
