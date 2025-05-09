# Generated by Django 4.2.20 on 2025-04-07 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True)),
                ('mail', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('direccion', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('telefono', models.CharField(blank=True, default='', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('dni', models.IntegerField(default=0)),
                ('telefono', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='InstitucionPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.institucion')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.persona')),
            ],
        ),
        migrations.AddField(
            model_name='institucion',
            name='id_persona',
            field=models.ManyToManyField(related_name='trabajadores', to='seguridadVial.persona'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='id_persona_encargado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encargado', to='seguridadVial.persona'),
        ),
        migrations.CreateModel(
            name='Elementos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('estado', models.BooleanField(blank=True, default=False, null=True)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.categoria')),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.institucion')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridadVial.persona')),
            ],
        ),
    ]
