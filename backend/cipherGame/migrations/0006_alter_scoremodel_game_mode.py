# Generated by Django 4.1.7 on 2023-06-05 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cipherGame', '0005_ciphertext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoremodel',
            name='game_mode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cipherGame.gamemode'),
        ),
    ]