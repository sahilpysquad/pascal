# Generated by Django 3.2.16 on 2022-10-11 17:54

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
            name='ClubCell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('club_or_cell', models.CharField(choices=[('CB', 'Club'), ('CL', 'Cell')], default='CB', max_length=2, verbose_name='Club or Cell')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('faculty_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_head', to=settings.AUTH_USER_MODEL, verbose_name='Faculty Head')),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='Members')),
            ],
        ),
    ]
