# Generated by Django 3.1.6 on 2021-02-01 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zolnierze', '0002_ekwipunek_kontrakty_przepustki_wnioski_wyjazdy_sluzbowe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wnioski',
            name='rodzaj_wniosku',
            field=models.CharField(choices=[('Urlopowy', 'Urlopowy'), ('Mieszkaniowy', 'Mieszkaniowy'), ('Boli mnie brzusio', 'Boli mnie brzusio')], max_length=45),
        ),
        migrations.AlterField(
            model_name='wnioski',
            name='status',
            field=models.CharField(choices=[('Przyjęty', 'Przyjęty'), ('Odrzucony', 'Odrzucony')], max_length=45),
        ),
    ]
