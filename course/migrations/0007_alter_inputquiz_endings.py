# Generated by Django 4.2.5 on 2023-10-23 14:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_code_snippet_options_remove_lesson_locked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputquiz',
            name='endings',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
