# Generated by Django 4.1.6 on 2023-08-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_blog_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
