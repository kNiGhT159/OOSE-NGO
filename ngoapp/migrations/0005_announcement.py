# Generated by Django 3.1.7 on 2021-05-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0004_remove_sinfo_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_email', models.EmailField(max_length=254, null=True)),
                ('heading', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=300)),
                ('expires_on', models.DateField()),
            ],
        ),
    ]
