# Generated by Django 5.0.4 on 2024-04-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_itenscompra'),
    ]

    operations = [
        migrations.AddField(
            model_name='itenscompra',
            name='preco_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]