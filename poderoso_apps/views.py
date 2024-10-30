# Importa funções e classes necessárias do Django
from django.shortcuts import get_object_or_404, render, redirect  # Funções para renderizar páginas e redirecionar
from .models import Topic, Entry, PlanoTreino, Exercicio  # Importa os modelos que representam os dados no banco de dados
from .forms import TopicForm, EntryForm  # Importa os formulários que lidam com os dados de entrada
from django.contrib.auth.decorators import login_required  # Importa o decorador que restringe acesso a usuários logados
from django.http import Http404  # Importa a classe para gerar erros 404


def index(request):
    """Renderiza a página inicial do aplicativo."""
    # A função 'render()' combina um template HTML com um dicionário de dados e retorna uma resposta ao navegador.
    # Aqui, 'poderoso_apps/index.html' é o caminho para o template e 'request' é a solicitação HTTP.
    return render(request, 'poderoso_apps/index.html')


@login_required  # Garante que apenas usuários logados possam acessar esta função
def topics(request):
    """Exibe a lista de tópicos do usuário logado."""
    # 'Topic.objects.filter()' recupera todos os tópicos do banco de dados que pertencem ao usuário logado.
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # Ordena os tópicos pela data de adição.
    
    # 'context' é um dicionário que contém os dados que serão passados para o template.
    context = {'topics': topics}  # Aqui, associamos a lista de tópicos à chave 'topics'.
    
    # 'render()' retorna uma resposta ao navegador, renderizando o template 'poderoso_apps/topics.html' com o contexto fornecido.
    return render(request, 'poderoso_apps/topics.html', context)


@login_required  # Protege a função para garantir que o usuário esteja logado
def topic(request, topic_id):
    """Exibe os detalhes de um tópico específico pelo seu ID."""
    # 'get_object_or_404()' tenta obter o tópico correspondente ao ID. Se não encontrar, retorna um erro 404.
    topic = get_object_or_404(Topic, id=topic_id)
    
    # Aqui, verificamos se o tópico pertence ao usuário que está logado. Se não pertencer, levantamos um erro 404.
    if topic.owner != request.user:
        raise Http404  # Lança um erro 404 para indicar que o recurso não foi encontrado.
    
    # Obtém todas as entradas associadas a este tópico, ordenando-as da mais recente para a mais antiga.
    entries = topic.entry_set.order_by('-date_added')
    
    # Cria um dicionário de contexto com o tópico e suas entradas, que será utilizado pelo template.
    context = {'topic': topic, 'entries': entries}  
    
    # Renderiza a página do tópico, retornando o template 'poderoso_apps/topic.html' com o contexto.
    return render(request, 'poderoso_apps/topic.html', context)


@login_required  # Garante que o usuário esteja logado para acessar essa função
def new_topic(request):
    """Exibe um formulário para criar um novo tópico."""
    if request.method != 'POST':  # Verifica se a requisição não é do tipo POST
        # Se não houver dados enviados, cria um formulário vazio para o novo tópico.
        form = TopicForm()  
    else:
        # Se a requisição for do tipo POST, significa que o usuário está tentando enviar dados para criar um novo tópico.
        form = TopicForm(data=request.POST)  # Preenche o formulário com os dados que foram enviados.
        
        # 'is_valid()' verifica se os dados do formulário estão corretos (como se todos os campos obrigatórios foram preenchidos).
        if form.is_valid():  
            new_topic = form.save(commit=False)  # Salva o tópico, mas não o envia ao banco de dados ainda.
            new_topic.owner = request.user  # Associa o novo tópico ao usuário logado, definindo o proprietário.
            new_topic.save()  # Agora salva o novo tópico no banco de dados.
            
            # Redireciona o usuário para a lista de tópicos após criar o novo tópico.
            return redirect('poderoso_apps:topics')  
    
    # Se o formulário não for válido ou se não houver dados, mostra o formulário novamente.
    context = {'form': form}  # Prepara o contexto para renderizar o formulário.
    
    # Renderiza a página para criar um novo tópico, enviando o contexto.
    return render(request, 'poderoso_apps/new_topic.html', context)


@login_required  # Garante que apenas usuários logados possam acessar esta função
def new_entry(request, topic_id):
    """Exibe um formulário para criar uma nova entrada em um tópico específico."""
    # Obtém o tópico específico usando o ID fornecido na URL.
    topic = get_object_or_404(Topic, id=topic_id)  
    
    if request.method != 'POST':  # Verifica se a requisição não é do tipo POST
        # Se não houver dados enviados, cria um formulário vazio para a nova entrada.
        form = EntryForm()  
    else:
        # Se a requisição for do tipo POST, significa que o usuário enviou dados para criar uma nova entrada.
        form = EntryForm(data=request.POST)  # Preenche o formulário com os dados que foram enviados.
        
        # Verifica se os dados do formulário são válidos.
        if form.is_valid():  
            new_entry = form.save(commit=False)  # Salva a entrada, mas não a envia ao banco de dados ainda.
            new_entry.topic = topic  # Associa a nova entrada ao tópico específico.
            new_entry.save()  # Agora salva a nova entrada no banco de dados.
            
            # Redireciona para a página do tópico após criar a nova entrada.
            return redirect('poderoso_apps:topic', topic_id=topic_id)  
    
    # Se o formulário não for válido ou se não houver dados, mostra o formulário novamente.
    context = {'topic': topic, 'form': form}  # Prepara o contexto com o tópico e o formulário.
    
    # Renderiza a página para criar nova entrada, enviando o contexto.
    return render(request, 'poderoso_apps/new_entry.html', context)


@login_required  # Protege a função para garantir que o usuário esteja logado
def edit_entry(request, entry_id):
    """Exibe um formulário para editar uma entrada existente."""
    # Obtém a entrada a ser editada pelo ID fornecido.
    entry = get_object_or_404(Entry, id=entry_id)  
    topic = entry.topic  # Obtém o tópico ao qual a entrada pertence.

    # Verifica se o tópico pertence ao usuário logado.
    if topic.owner != request.user:
        raise Http404  # Levanta um erro 404 se o usuário não é o proprietário do tópico.

    if request.method != 'POST':  # Verifica se a requisição não é do tipo POST
        # Se não houver dados enviados, cria um formulário preenchido com os dados da entrada existente.
        form = EntryForm(instance=entry)  
    else:
        # Se a requisição for do tipo POST, significa que o usuário está enviando dados para atualizar a entrada.
        form = EntryForm(instance=entry, data=request.POST)  # Preenche o formulário com dados existentes e os dados enviados.
        
        # Verifica se os dados do formulário são válidos.
        if form.is_valid():  
            form.save()  # Salva as alterações na entrada no banco de dados.
            
            # Redireciona para a página do tópico após a edição.
            return redirect('poderoso_apps:topic', topic_id=topic.id)  
    
    # Prepara o contexto para renderização, incluindo a entrada, o tópico e o formulário.
    context = {'entry': entry, 'topic': topic, 'form': form}  
    
    # Renderiza a página de edição, enviando o contexto.
    return render(request, 'poderoso_apps/edit_entry.html', context)


def planos_treinos(request):
    """Exibe a lista de planos de treino disponíveis."""
    # Obtém todos os planos de treino do banco de dados.
    planos = PlanoTreino.objects.all()  
    plano_id = request.GET.get('plano_id')
    # Renderiza a lista de planos, enviando os dados para o template.
    return render(request, 'poderoso_apps/planos_treinos.html', {'planos': planos, 'plano_id': plano_id})  


def detalhes_planos(request):
    """Exibe detalhes de um plano de treino específico e permite marcar exercícios como concluídos."""
    # Obtém o ID do plano a partir da requisição GET, que é geralmente passado na URL.
    plano_id = request.GET.get('plano_id')  
    
    if plano_id:  # Se o ID do plano foi fornecido
        # Tenta obter o plano específico. Se não encontrar, retorna um erro 404.
        plano = get_object_or_404(PlanoTreino, id=plano_id)  
        
        # Obtém todos os exercícios associados ao plano.
        exercicios = plano.exercicios.all()  
    else:
        plano = None  # Se não houver ID, não existe plano.
        exercicios = None  # Não há exercícios se não houver plano.

    # Obtém todos os planos de treino disponíveis no banco de dados.
    planos = PlanoTreino.objects.all() 
    
    if exercicios:
        total_exercicios = exercicios.count()
        exercicios_concluidos = exercicios.filter(concluido=True).count()
        progresso = (exercicios_concluidos / total_exercicios) * 100 if total_exercicios > 0 else 0
    else:
        progresso = 0


    # Verifica se a requisição é do tipo POST, indicando que o usuário está tentando atualizar o status de um exercício.
    if request.method == 'POST':
        exercicio_id = request.POST.get('exercicio_id')  # Obtém o ID do exercício que o usuário está tentando marcar como concluído.
        
        # Obtém o exercício específico. Se não encontrar, retorna um erro 404.
        exercicio = get_object_or_404(Exercicio, id=exercicio_id, plano=plano)  
        
        # Inverte o status de 'concluído' do exercício. Se estava como concluído, agora será marcado como não concluído, e vice-versa.
        exercicio.concluido = not exercicio.concluido  
        
        # Salva as alterações no banco de dados.
        exercicio.save()  # Atualiza o exercício no banco de dados para refletir o novo status.
        # Redireciona para evitar que o usuário atualize o status novamente se ele recarregar a página.
    
    # Renderiza a página com detalhes do plano, enviando o plano, seus exercícios e todos os planos disponíveis para o template.
    return render(request, 'poderoso_apps/detalhes_plano.html', {
        'plano': plano,
        'exercicios': exercicios,
        'planos': planos,
        'progresso': progresso
    })

