# Importa o módulo forms do Django, que fornece classes para criar formulários.
from django import forms  
# Importa os modelos Topic e Entry que serão usados nos formulários.
from .models import Topic, Entry  

class TopicForm(forms.ModelForm):
    class Meta:
        # Define as configurações do formulário relacionado ao modelo Topic.
        model = Topic  # Especifica que este formulário se baseia no modelo Topic.
        fields = ['text']  # Lista os campos do modelo que devem ser incluídos no formulário.
        labels = {'text': ''}  # Define um rótulo vazio para o campo 'text', removendo o título do campo.

class EntryForm(forms.ModelForm):
    class Meta:
        # Define as configurações do formulário relacionado ao modelo Entry.
        model = Entry  # Especifica que este formulário se baseia no modelo Entry.
        fields = ['text']  # Lista os campos do modelo que devem ser incluídos no formulário.
        labels = {'text': ''}  # Define um rótulo vazio para o campo 'text', removendo o título do campo.
        # Personaliza a apresentação do campo 'text' no formulário.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # Usa um widget Textarea com 80 colunas.

class CalculoBasal(forms.Form):
    peso = forms.FloatField(max_value=999, min_value=5, error_messages={"required": "Por favor, entre um número válido!"})
    idade = forms.IntegerField(max_value=105)
    SEXO_CHOICES = [
        ('H', 'Homem'),
        ('M', 'Mulher'),
    ]
    sexo = forms.ChoiceField(
        choices = SEXO_CHOICES,
        widget = forms.RadioSelect(attrs={'class': 'btn-sexo'})
    )