# Generated by Django 3.0.7 on 2020-06-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]
