# Generated by Django 3.2 on 2022-11-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0007_delete_aimodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=30, null=True)),
                ('file_upload', models.FileField(blank=True, upload_to='D:\\KT\\7th_miniproject\\Aivle_7th_miniproject\\upload_model')),
                ('uploader', models.CharField(max_length=100, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
