# Generated by Django 4.2.5 on 2023-10-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_choice_options_alter_code_snippet_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputquiz',
            name='answer',
            field=models.CharField(max_length=50),
        ),
    ]
