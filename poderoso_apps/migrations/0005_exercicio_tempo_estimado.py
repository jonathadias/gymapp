# Generated by Django 5.1.2 on 2024-10-31 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poderoso_apps', '0004_planotreino_exercicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='tempo_estimado',
            field=models.PositiveIntegerField(default=30, help_text='Tempo em minutos'),
            preserve_default=False,
        ),
    ]
