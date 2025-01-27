# Generated by Django 4.2.5 on 2023-10-23 13:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0005_alter_inputquiz_question_alter_pageofcourse_context_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='code_snippet',
            options={'verbose_name': 'kod ', 'verbose_name_plural': 'kodlar'},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='locked',
        ),
        migrations.AddField(
            model_name='lesson',
            name='lock',
            field=models.ManyToManyField(blank=True, related_name='lesson_lock', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='code_snippet',
            name='answer',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
