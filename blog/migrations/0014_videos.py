# Generated by Django 3.2 on 2021-04-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Video', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]