# Generated by Django 4.0.5 on 2022-10-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_post_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
