# Generated by Django 3.2.6 on 2021-08-13 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_project', '0003_rename_album_tracks_albums'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='name',
            field=models.CharField(default='name', max_length=250),
            preserve_default=False,
        ),
    ]