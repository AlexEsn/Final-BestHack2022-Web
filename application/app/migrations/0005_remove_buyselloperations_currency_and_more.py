# Generated by Django 4.0.4 on 2022-04-23 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_buyselloperations_user_buyselloperations_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyselloperations',
            name='currency',
        ),
        migrations.AddField(
            model_name='buyselloperations',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.currencies'),
        ),
    ]
