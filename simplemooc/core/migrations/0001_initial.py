# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_emp', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='Id Empresa')),
                ('cnpj', models.CharField(max_length=20, unique=True, verbose_name='CNPJ')),
                ('razao', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('fantasia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Fantasia')),
                ('endereco', models.CharField(max_length=55, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=55, verbose_name='Cidade')),
                ('uf', models.CharField(choices=[('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
            ],
            options={
                'ordering': ['razao'],
                'verbose_name_plural': 'Empresas',
                'verbose_name': 'Empresa',
            },
        ),
    ]