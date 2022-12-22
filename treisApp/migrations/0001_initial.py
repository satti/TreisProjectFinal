# Generated by Django 4.0.6 on 2022-11-21 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(null=True)),
                ('academicyear', models.CharField(choices=[('21', '2021-2022'), ('22', '2022-2023'), ('23', '2023-2024')], default='2021-2022', max_length=100, null=True)),
                ('year', models.CharField(choices=[('I Year', 'I Year'), ('II Year', 'II Year')], max_length=50, null=True)),
                ('group', models.CharField(choices=[('MPC', 'MPC'), ('BPC', 'BPC'), ('MEC', 'MEC')], max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100, null=True)),
                ('group', models.CharField(max_length=100, null=True)),
                ('testtype', models.CharField(max_length=100, null=True)),
                ('ac', models.CharField(max_length=20, null=True)),
                ('s1', models.IntegerField()),
                ('s2', models.IntegerField()),
                ('s3', models.IntegerField()),
                ('s4', models.IntegerField()),
                ('s5', models.IntegerField()),
                ('s6', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treisApp.student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
