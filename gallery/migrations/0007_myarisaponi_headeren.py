# Generated by Django 5.0.6 on 2024-05-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_elitealternative_delete_elitealternativee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myarisaponi',
            name='headerEn',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
