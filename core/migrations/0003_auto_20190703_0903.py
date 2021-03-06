# Generated by Django 2.2.2 on 2019-07-03 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190703_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='host',
            name='localisation',
        ),
        migrations.RemoveField(
            model_name='hosted',
            name='localisation',
        ),
        migrations.AddField(
            model_name='user',
            name='localisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Localisation'),
        ),
    ]
