# Generated by Django 2.1.5 on 2019-02-24 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190224_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='initial_profiles/459.jpg', upload_to='profile_pics'),
        ),
    ]
