# Generated by Django 2.0.10 on 2019-05-04 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doacoes', '0001_initial'),
        ('instituicoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doacaouser',
            name='doador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doacaooutros',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instituicoes.InstituicaoLista'),
        ),
        migrations.AddField(
            model_name='demandadoacao',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instituicoes.InstituicaoLista'),
        ),
    ]
