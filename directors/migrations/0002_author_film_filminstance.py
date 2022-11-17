# Generated by Django 4.1.3 on 2022-11-17 17:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('directors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('summary', models.TextField(help_text='observations', max_length=100)),
                ('isbn', models.CharField(help_text='ISBN is 13 characters', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directors.author')),
                ('genre', models.ManyToManyField(to='directors.genre')),
            ],
        ),
        migrations.CreateModel(
            name='FilmInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='unique ID for this movie', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='film availability', max_length=1)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directors.film')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]