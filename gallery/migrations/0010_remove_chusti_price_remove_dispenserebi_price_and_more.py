# Generated by Django 5.0.6 on 2024-07-15 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_rename_headeren_chusti_headereng_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chusti',
            name='price',
        ),
        migrations.RemoveField(
            model_name='dispenserebi',
            name='price',
        ),
        migrations.RemoveField(
            model_name='elitealternative',
            name='price',
        ),
        migrations.RemoveField(
            model_name='myarisaponi',
            name='price',
        ),
        migrations.RemoveField(
            model_name='petbotli',
            name='price',
        ),
        migrations.RemoveField(
            model_name='tsubi',
            name='price',
        ),
    ]
