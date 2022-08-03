# Generated by Django 4.2.16 on 2024-10-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0123_upstreampulp_q_select"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="deferred",
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="immediate",
            field=models.BooleanField(default=False, null=True),
        ),
    ]