# Generated by Django 4.1.3 on 2022-11-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=20, verbose_name='Никнейм')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Юзер',
                'verbose_name_plural': 'Юзеры',
            },
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
