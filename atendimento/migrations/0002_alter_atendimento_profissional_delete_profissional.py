# Generated by Django 5.0.3 on 2024-03-13 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0001_initial'),
        ('profissional', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profissional.profissional'),
        ),
        migrations.DeleteModel(
            name='Profissional',
        ),
    ]