# Generated by Django 4.2.16 on 2024-09-20 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.TimeField(blank=True, null=True)),
                ('q2', models.IntegerField(blank=True, null=True)),
                ('q3', models.TimeField(blank=True, null=True)),
                ('q4', models.TimeField(blank=True, null=True)),
                ('q5a', models.IntegerField(null=True)),
                ('q5b', models.IntegerField(null=True)),
                ('q5c', models.IntegerField(null=True)),
                ('q5d', models.IntegerField(null=True)),
                ('q5e', models.IntegerField(null=True)),
                ('q5f', models.IntegerField(null=True)),
                ('q5g', models.IntegerField(null=True)),
                ('q5h', models.IntegerField(null=True)),
                ('q5i', models.IntegerField(null=True)),
                ('q5j', models.IntegerField(blank=True, null=True)),
                ('q6', models.IntegerField(null=True)),
                ('q7', models.IntegerField(null=True)),
                ('q8', models.IntegerField(null=True)),
                ('q9', models.IntegerField(null=True)),
                ('q10', models.IntegerField(null=True)),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.questionario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
