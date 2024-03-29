# Generated by Django 2.2.2 on 2019-07-09 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mulu', '0003_auto_20190704_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='furniture',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='furniture',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='furniture/%Y%m%d'),
        ),
        migrations.AlterIndexTogether(
            name='furniture',
            index_together={('id', 'slug')},
        ),
    ]
