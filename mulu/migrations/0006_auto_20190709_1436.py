# Generated by Django 2.2.2 on 2019-07-09 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mulu', '0005_furniture_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='files',
        ),
        migrations.CreateModel(
            name='furniture_detail_photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='files/%Y%m%d')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mulu.furniture')),
            ],
        ),
    ]
