# Generated by Django 5.1.2 on 2024-11-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poderoso_apps', '0007_exercicio_imagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='imagens',
            field=models.ImageField(blank=True, null=True, upload_to='exercicios'),
        ),
    ]
