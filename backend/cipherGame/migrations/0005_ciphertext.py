# Generated by Django 4.1.7 on 2023-06-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cipherGame', '0004_gameidmodel_scoremodel_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciphertext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
