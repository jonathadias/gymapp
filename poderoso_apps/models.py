from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """
    Modelo que representa um tópico sobre o qual o usuário está aprendendo.

    Attributes:
        text (CharField): O título ou nome do tópico (máximo 200 caracteres)
        date_added (DateTimeField): Data e hora de criação do tópico (preenchido automaticamente)
        owner (ForeignKey): Referência ao usuário que criou o tópico
    
    Relationships:
        - Pertence a um User (owner)
        - Pode ter múltiplas Entry relacionadas
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna uma representação em string do tópico.

        Returns:
            str: O texto do tópico
        """
        return self.text

class Entry(models.Model):
    """
    Modelo que representa uma entrada específica de aprendizado relacionada a um tópico.

    Attributes:
        topic (ForeignKey): Referência ao tópico ao qual esta entrada pertence
        text (TextField): O conteúdo da entrada
        date_added (DateTimeField): Data e hora de criação da entrada (preenchido automaticamente)
    
    Relationships:
        - Pertence a um Topic (topic)

    Meta:
        verbose_name_plural define o nome plural correto para o modelo no admin do Django
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """
        Retorna uma representação em string da entrada.

        Returns:
            str: Os primeiros 50 caracteres do texto da entrada, seguidos por reticências
        """
        return f"({self.text[:50]}...)"

