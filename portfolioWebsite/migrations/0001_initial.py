# Generated by Django 3.2.7 on 2021-09-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headline', models.CharField(max_length=150)),
                ('Subheadline', models.CharField(blank=True, max_length=200, null=True)),
                ('Body', models.TextField(blank=True, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Active', models.BooleanField(default=False)),
                ('Featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tags', models.CharField(max_length=200)),
            ],
        ),
    ]