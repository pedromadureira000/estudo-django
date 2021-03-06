# Generated by Django 3.2.4 on 2021-06-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
                ('vimeo_id', models.CharField(max_length=30)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
