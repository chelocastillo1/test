# Generated by Django 4.0 on 2021-12-16 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0005_alter_publicacion_destacado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
    ]
