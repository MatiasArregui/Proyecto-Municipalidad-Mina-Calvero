# Generated by Django 4.2.13 on 2025-06-27 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catastrophe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_disaster', models.CharField(default=None, max_length=255)),
                ('descripcion', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_default', models.BooleanField(default=False)),
                ('image_disaster', models.CharField(max_length=255)),
                ('mapa_interactivo', models.CharField(default=None, max_length=855)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=240)),
                ('direccion', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('telefono', models.CharField(blank=True, default='', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitucionCargoPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=120)),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Refujio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catastrofe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.catastrophe')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Protocole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_seleccion', models.CharField(blank=True, choices=[('Antes', 'Antes'), ('Durante', 'Durante'), ('Despues', 'Despues')], default=None, max_length=50, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('catastrophe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protocoles', to='seguridadVial.catastrophe')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=120)),
                ('dni', models.IntegerField(default=0)),
                ('telefono', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('id_institucion', models.ManyToManyField(through='seguridadVial.InstitucionCargoPersona', to='seguridadVial.institucion')),
            ],
        ),
        migrations.AddField(
            model_name='institucioncargopersona',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.persona'),
        ),
        migrations.CreateModel(
            name='Elementos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('tipo', models.CharField(blank=True, max_length=120, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('cantidad', models.IntegerField(blank=True, default=1, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=240, null=True)),
                ('estado', models.BooleanField(blank=True, default=True, null=True)),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.institucion')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seguridadVial.persona')),
            ],
        ),
    ]
