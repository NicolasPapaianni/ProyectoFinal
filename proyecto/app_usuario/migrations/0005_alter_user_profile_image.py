# Generated by Django 4.0.6 on 2022-08-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_usuario', '0004_user_profile_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='perfil_image/'),
        ),
    ]
