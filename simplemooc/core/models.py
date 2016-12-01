from django.db import models

# Create your models here.
class Empresa(models.Model):
    uf_padrao = (
        ('AL', "Alagoas"), ('AP', "Amapá"), ('AM', "Amazonas"), ('BA', "Bahia"), ('CE', "Ceará"),
        ('DF', "Distrito Federal"), ('ES', "Espírito Santo"), ('GO', "Goiás"), ('MA', "Maranhão"),
        ('MT', "Mato Grosso"), ('MS', "Mato Grosso do Sul"), ('MG', "Minas Gerais"), ('PA', "Pará"),
        ('PB', "Paraíba"), ('PR', "Paraná"), ('PE', "Pernambuco"), ('PI', "Piauí"), ('RJ', "Rio de Janeiro"),
        ('RN', "Rio Grande do Norte"), ('RS', "Rio Grande do Sul"), ('RO', "Rondônia"), ('RR', "Roraima"),
        ('SC', "Santa Catarina"), ('SP', "São Paulo"), ('SE', "Sergipe"), ('TO', "Tocantins")
    )
    id_emp = models.AutoField('Id Empresa', primary_key=True, auto_created=True, blank=False, null=False, unique=True,
                              name='id_emp')
    cnpj = models.CharField('CNPJ', max_length=20, unique=True, blank=False, null=False, name='cnpj')
    razao = models.CharField('Razão Social', max_length=100, blank=False, null=False, name='razao')
    fantasia = models.CharField('Nome Fantasia', max_length=100, blank=True, null=True, name='fantasia')
    endereco = models.CharField('Endereço', max_length=55, blank=False, null=False, name='endereco')
    cidade = models.CharField('Cidade', max_length=55, blank=False, null=False, name='cidade')
    uf = models.CharField('Estado', max_length=2, choices=uf_padrao, blank=False, null=False, name='uf')
    cep = models.IntegerField('CEP', blank=False, null=False, name='cep')
    ativo = models.BooleanField('Ativo?', blank=False, null=False, default=True, name='ativo')
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, name='data_cadastro')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['razao']