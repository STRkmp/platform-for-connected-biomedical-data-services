# Generated by Django 5.0.2 on 2024-04-03 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('health_check_url', models.URLField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('full_path', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosisRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='diagnosis_request', to='api.processingservice')),
                ('result_file', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='result_file_diagnosis_request', to='api.uploadedfile')),
                ('uploaded_file', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='uploaded_file_diagnosis_request', to='api.uploadedfile')),
            ],
        ),
    ]
