# Generated by Django 5.1.2 on 2024-11-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poderoso_apps', '0006_remove_exercicio_tempo_estimado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='imagens',
            field=models.ImageField(blank=True, null=True, upload_to='None'),
        ),
    ]