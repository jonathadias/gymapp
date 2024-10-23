from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Home Page"""
    return render(request, 'poderoso_apps/index.html')
# Create your views here.

@login_required
def topics(request):
    """Página dos tópicos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'poderoso_apps/topics.html', context)

@login_required
def topic(request, topic_id):
    """Página do tópico por Id"""
    topic = Topic.objects.get(id=topic_id)
    #Assegurar que o tópico pertence ao usuário logado
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'poderoso_apps/topic.html', context)

@login_required
def new_topic(request):
    """Página inserir novo tópico"""
    if request.method != 'POST':
        #Nenhum dado enviado; criar um formulário em branco.
        form = TopicForm()
    else:
        #Há dados enviados, processar dados.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            return redirect('poderoso_apps:topics')
    
    #Demonstrar formulário em branco ou inválido
    context = {'form': form}
    return render(request, 'poderoso_apps/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Página inserir nova entrada"""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        #Nenhum dado enviado; criar u formulário em branco.
        form = EntryForm()
    else:
        #Há dados enviados, processar dados.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('poderoso_apps:topic', topic_id=topic_id)

    #Demonstrar formulário em branco ou inválido
    context = {'topic': topic, 'form': form}
    return render(request, 'poderoso_apps/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Formulário previamente preenchido
        form = EntryForm(instance=entry)
    else:
        #Há dados enviados, processar dados.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('poderoso_apps:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'poderoso_apps/edit_entry.html', context)