# Generated by Django 2.1.2 on 2018-12-15 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_auto_20181212_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264, unique=True)),
                ('intro', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=20000)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'db_table': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Blogtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
            ],
            options={
                'db_table': 'Blogtype',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webpages.Blogtype'),
        ),
    ]
