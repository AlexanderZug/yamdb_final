# Generated by Django 2.2.16 on 2022-08-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220811_0829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined']},
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default=0, max_length=40),
        ),
    ]
