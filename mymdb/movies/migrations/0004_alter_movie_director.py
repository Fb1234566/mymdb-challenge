# Generated by Django 4.2.5 on 2023-09-13 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0001_initial'),
        ('movies', '0003_movie_director_alter_character_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cast.person'),
        ),
    ]
