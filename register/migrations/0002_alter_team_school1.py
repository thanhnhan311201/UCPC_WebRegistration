# Generated by Django 3.2 on 2022-04-26 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='school1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school1', to='register.school'),
        ),
    ]
