# Generated by Django 2.2.3 on 2019-09-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0004_questattempt_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='cooldown_minutes',
            field=models.IntegerField(default=5),
        ),
    ]
