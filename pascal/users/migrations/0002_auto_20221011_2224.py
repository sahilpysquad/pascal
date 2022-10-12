# Generated by Django 3.2.16 on 2022-10-11 16:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='email_token',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Email Token'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False, verbose_name='Is Email Verified'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_phone_verified',
            field=models.BooleanField(default=False, verbose_name='Is Phone Verified'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='OTP'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[6-9]\\d{9}$')], verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='sem',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Semester'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('RQ', 'Requested'), ('AP', 'Approved'), ('RJ', 'Rejected')], default='RQ', max_length=2, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_choice',
            field=models.CharField(choices=[('FH', 'Faculty Head'), ('FM', 'Faculty Member'), ('ST', 'Student'), ('OT', 'Other')], default='ST', max_length=2, verbose_name='User Choice'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.department', verbose_name='Department'),
        ),
    ]