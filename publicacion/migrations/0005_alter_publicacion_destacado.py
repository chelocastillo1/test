# Generated by Django 4.0 on 2021-12-16 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0004_alter_publicacion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='destacado',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
