# Generated by Django 5.1.1 on 2024-10-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_bio_customuser_biography_posting_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]