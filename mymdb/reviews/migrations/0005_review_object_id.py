# Generated by Django 4.2.5 on 2023-09-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='object_id',
            field=models.IntegerField(default=0),
        ),
    ]
