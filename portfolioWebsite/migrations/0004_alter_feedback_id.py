# Generated by Django 3.2.7 on 2021-09-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioWebsite', '0003_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
