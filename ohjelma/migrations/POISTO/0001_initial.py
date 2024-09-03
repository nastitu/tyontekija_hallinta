# Generated by Django 5.1 on 2024-08-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Työntekijä',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etunimi', models.CharField(max_length=50)),
                ('sukunimi', models.CharField(max_length=50)),
                ('puhelin', models.CharField(max_length=50)),
                ('osoite', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('aloitus_pvm', models.DateField()),
                ('lopetus_pvm', models.DateField()),
                ('työsuhteen_tyyppi', models.CharField(choices=[('vakituinen', 'Vakituinen'), ('määräaikainen', 'Määräaikainen')], default='Vakituinen', max_length=50)),
            ],
        ),
    ]
