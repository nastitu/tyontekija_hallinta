# Generated by Django 5.1 on 2024-09-03 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelma', '0007_alter_maakunta_nimi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='työpiste',
            name='kunta',
        ),
        migrations.RemoveField(
            model_name='työntekijä',
            name='työkunta',
        ),
        migrations.RemoveField(
            model_name='työntekijä',
            name='työmaakunta',
        ),
        migrations.RemoveField(
            model_name='työntekijä',
            name='työpiste',
        ),
        migrations.DeleteModel(
            name='Kunta',
        ),
        migrations.DeleteModel(
            name='Maakunta',
        ),
        migrations.DeleteModel(
            name='Työpiste',
        ),
    ]
