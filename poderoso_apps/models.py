# Importa os módulos necessários do Django.
from django.db import models  
from django.contrib.auth.models import User  # Importa o modelo User para associar usuários aos tópicos e planos.
from django.db.models import CASCADE  # Importa o comportamento de exclusão em cascata.

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
    # Define o campo 'text' como um CharField com um limite de 200 caracteres.
    text = models.CharField(max_length=200)
    # Define o campo 'date_added' como um DateTimeField que armazena a data e a hora em que o tópico foi criado.
    date_added = models.DateTimeField(auto_now_add=True)  # Preenchido automaticamente na criação.
    # Define o campo 'owner' como uma chave estrangeira que referencia o modelo User.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna uma representação em string do tópico.

        Returns:
            str: O texto do tópico
        """
        return self.text  # Retorna o texto do tópico quando chamado.

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
    # Define o campo 'topic' como uma chave estrangeira que referencia o modelo Topic.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # A entrada está vinculada a um tópico.
    # Define o campo 'text' como um TextField para armazenar o conteúdo da entrada.
    text = models.TextField()  
    # Define o campo 'date_added' como um DateTimeField para armazenar a data e a hora de criação.
    date_added = models.DateTimeField(auto_now_add=True)  # Preenchido automaticamente.

    class Meta:
        verbose_name_plural = 'entries'  # Define como 'entries' para o plural no admin.

    def __str__(self):
        """
        Retorna uma representação em string da entrada.

        Returns:
            str: Os primeiros 50 caracteres do texto da entrada, seguidos por reticências
        """
        return f"({self.text[:50]}...)"  # Retorna os primeiros 50 caracteres da entrada seguidos por '...'.

class PlanoTreino(models.Model):
    """Modelo que representa um plano de treino (ex: TREINO AXB, 3X, 4X)"""

    # Define o campo 'nome' como um CharField com limite de 100 caracteres.
    nome = models.CharField(max_length=100)
    # Define o campo 'descricao' como um TextField que pode ser nulo ou em branco.
    descricao = models.TextField(null=True, blank=True)  
    # Define o campo 'owner' como uma chave estrangeira que referencia o modelo User.
    owner = models.ForeignKey(User, on_delete=CASCADE)  # Usuário que criou o plano.

    def __str__(self):
        return self.nome  # Retorna o nome do plano de treino.

class Exercicio(models.Model):
    """Modelo que representa um exercício específico em um plano"""

    # Define o campo 'plano' como uma chave estrangeira que referencia o modelo PlanoTreino.
    plano = models.ForeignKey(PlanoTreino, related_name='exercicios', on_delete=CASCADE)  
    # Define o campo 'nome' como um CharField com limite de 200 caracteres.
    nome = models.CharField(max_length=200)
    # Define o campo 'series' como um IntegerField para armazenar o número de séries do exercício.
    series = models.IntegerField()  
    # Define o campo 'repeticoes' como um IntegerField para armazenar o número de repetições do exercício.
    repeticoes = models.IntegerField()  
    # Define o campo 'intervalo' como um CharField com limite de 50 caracteres para armazenar o intervalo.
    intervalo = models.CharField(max_length=50)  
    # Define o campo 'concluido' como um BooleanField que indica se o exercício foi concluído ou não.
    concluido = models.BooleanField(default=False)  # Padrão é False.

    def __str__(self):
        return self.nome  # Retorna o nome do exercício.
