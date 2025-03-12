# Generated by Django 2.0.13 on 2023-07-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('associated_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Acceptmodel',
            },
        ),
        migrations.CreateModel(
            name='donormodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phoneno', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'donormodel',
            },
        ),
        migrations.CreateModel(
            name='donorModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selleremail', models.CharField(max_length=100)),
                ('cropname', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100000)),
                ('location', models.CharField(max_length=100000)),
                ('file', models.FileField(upload_to='post_images/')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'donorstable',
            },
        ),
        migrations.CreateModel(
            name='OurAchivements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='post_images/')),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'OurAchivements',
            },
        ),
    ]
