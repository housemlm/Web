# Generated by Django 2.2.2 on 2019-07-01 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter a furniture brand: ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter a furniture kind: ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='furniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mulu.Brand')),
                ('kind', models.ManyToManyField(help_text='select a kind for this furniture: ', to='mulu.kind')),
            ],
        ),
    ]
