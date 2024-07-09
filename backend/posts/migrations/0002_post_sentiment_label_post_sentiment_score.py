# Generated by Django 5.0.6 on 2024-07-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sentiment_label',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sentiment_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]