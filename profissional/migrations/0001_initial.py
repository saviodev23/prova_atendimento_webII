# Generated by Django 5.0.3 on 2024-03-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('especialidade', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
    ]
