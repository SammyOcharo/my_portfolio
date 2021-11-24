# Generated by Django 3.2.7 on 2021-11-24 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioWebsite', '0006_feedback_contact_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='SubTitle',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Remark',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
