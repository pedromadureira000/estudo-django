# Generated by Django 3.2.4 on 2021-06-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='descricao',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(default=1, max_length=30),
        ),
    ]
