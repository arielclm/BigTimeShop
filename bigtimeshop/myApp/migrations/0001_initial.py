# Generated by Django 4.2.7 on 2023-12-07 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=128)),
                ('Cquantity', models.IntegerField()),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=128)),
                ('pdate', models.DateTimeField()),
                ('pstock', models.IntegerField()),
                ('pprice', models.IntegerField()),
                ('isDelete', models.BooleanField()),
                ('pcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myApp.category')),
            ],
        ),
    ]
