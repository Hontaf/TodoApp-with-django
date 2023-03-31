# Generated by Django 4.1.7 on 2023-03-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=255)),
                ('priority', models.CharField(choices=[('Haute', 'Haute'), ('Moyenne', 'Moyenne'), ('Basse', 'Basse'), ('Quelconque', 'Quelconque')], max_length=50)),
                ('enability', models.BooleanField(default=True)),
                ('date_debut', models.DateField()),
                ('date_expiration', models.DateField()),
                ('to_prolong', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]