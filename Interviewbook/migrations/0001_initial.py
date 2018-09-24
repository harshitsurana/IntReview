# Generated by Django 2.1.1 on 2018-09-24 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('job_profile', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('rounds', models.IntegerField(blank=True, null=True)),
                ('questions', models.CharField(max_length=5000)),
                ('compensation', models.IntegerField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]