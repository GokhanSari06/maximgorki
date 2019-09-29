# Generated by Django 2.2.5 on 2019-09-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HizmetlerimizIcerik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Blog İçerik', max_length=100)),
                ('description', models.CharField(default='Description', max_length=100)),
                ('keywords', models.CharField(default='Keywords', max_length=100)),
                ('author', models.CharField(default='Author', max_length=100)),
                ('link', models.SlugField(unique=True)),
                ('ustbaslik', models.CharField(max_length=100)),
                ('altbaslik', models.CharField(max_length=100)),
                ('buyukyazi', models.TextField()),
                ('kucukyazi', models.TextField()),
                ('resim', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
