# Generated by Django 5.1.1 on 2024-11-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_category_post_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(default='Annet', related_name='posts', to='blog.category'),
        ),
    ]
