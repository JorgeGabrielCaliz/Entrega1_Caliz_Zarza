# Generated by Django 4.1.1 on 2022-11-02 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_afiliado_autorizaciones_cartillas_seguro_al_viajero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_plan', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('numero_de_afiliado', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='autorizaciones',
            name='numero_de_afiliado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seguro_al_viajero',
            name='numero_de_afiliado',
            field=models.IntegerField(),
        ),
    ]
