# Generated by Django 5.1.2 on 2024-10-25 00:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poderoso_apps', '0003_topic_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoTreino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('series', models.IntegerField()),
                ('repeticoes', models.IntegerField()),
                ('intervalo', models.CharField(max_length=50)),
                ('concluido', models.BooleanField(default=False)),
                ('plano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercicios', to='poderoso_apps.planotreino')),
            ],
        ),
    ]