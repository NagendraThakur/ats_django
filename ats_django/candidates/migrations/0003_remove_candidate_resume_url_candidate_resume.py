# Generated by Django 5.1.3 on 2024-12-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_alter_candidate_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='resume_url',
        ),
        migrations.AddField(
            model_name='candidate',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
