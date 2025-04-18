# Generated by Django 5.2 on 2025-04-14 15:49

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('storyId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Story ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('content', models.TextField(verbose_name='Story')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('isPublic', models.BooleanField(default=True, verbose_name='Is it Public')),
            ],
            options={
                'verbose_name': 'Stories',
                'verbose_name_plural': 'Stories',
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(verbose_name='Rating')),
                ('storyId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.stories')),
            ],
            options={
                'verbose_name': 'Ratings',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
