# Generated by Django 2.0.10 on 2019-05-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstituicaoLista',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('instituicao', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(blank=True, max_length=255, null=True)),
                ('cep', models.CharField(blank=True, max_length=255, null=True)),
                ('cidade', models.CharField(blank=True, max_length=255, null=True)),
                ('descricao', models.TextField(blank=True, max_length=1000, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('entidade_que_administra_o_abrigo', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('idade', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_de_criancas', models.CharField(blank=True, max_length=255, null=True)),
                ('pais', models.CharField(blank=True, max_length=255, null=True)),
                ('possui_programa_de_apadrinhamento_afetivo', models.CharField(blank=True, max_length=255, null=True)),
                ('responsavel', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.CharField(blank=True, max_length=255, null=True)),
                ('telefone', models.CharField(blank=True, max_length=255, null=True)),
                ('end_format', models.CharField(blank=True, max_length=255, null=True)),
                ('lat_long', models.CharField(blank=True, max_length=255, null=True)),
                ('logo_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('autorizado', models.BooleanField(default=False)),
                ('editado', models.BooleanField(default=False)),
            ],
        ),
    ]
