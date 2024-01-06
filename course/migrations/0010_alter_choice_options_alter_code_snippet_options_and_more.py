# Generated by Django 4.2.5 on 2023-10-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_inputquiz_new_line_alter_choice_choice_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'VARIANT ', 'verbose_name_plural': 'VARIANTLAR'},
        ),
        migrations.AlterModelOptions(
            name='code_snippet',
            options={'verbose_name': 'KOD ', 'verbose_name_plural': 'KODLAR'},
        ),
        migrations.AlterModelOptions(
            name='inputquiz',
            options={'verbose_name': 'OCHIQ TEST ', 'verbose_name_plural': 'OCHIQ TESTLAR'},
        ),
        migrations.AlterModelOptions(
            name='pageofcourse',
            options={'verbose_name': 'SAHIFA ', 'verbose_name_plural': 'SAHIFALAR'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'TEST ', 'verbose_name_plural': 'TESTLAR'},
        ),
        migrations.AlterModelOptions(
            name='tips',
            options={'verbose_name': 'ESLATMA ', 'verbose_name_plural': 'ESLATMALAR'},
        ),
        migrations.AlterField(
            model_name='inputquiz',
            name='answer',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]