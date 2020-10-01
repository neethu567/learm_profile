# Generated by Django 3.1.1 on 2020-09-30 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(upload_to='')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('mobile_number', models.IntegerField(default=0)),
                ('address', models.TextField(blank=True, max_length=500)),
                ('country', models.TextField(blank=True, max_length=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]