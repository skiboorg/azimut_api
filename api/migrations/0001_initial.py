# Generated by Django 3.1.5 on 2021-01-13 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Категория в автопарке')),
                ('name_slug', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='autopark/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='AutoSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Подкатегория в автопарке')),
                ('name_slug', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.autocategory', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, null=True, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='service/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_slug', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
                ('price_hour', models.IntegerField(blank=True, null=True, verbose_name='Стоимость за час')),
                ('price_km', models.IntegerField(blank=True, null=True, verbose_name='Стоимость за km')),
                ('min_hour', models.IntegerField(blank=True, null=True, verbose_name='Минимально часов')),
                ('seats', models.IntegerField(blank=True, null=True, verbose_name='Мест')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='CarOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Категория в автопарке')),
                ('image', models.ImageField(blank=True, null=True, upload_to='car/options/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название услуги')),
                ('name_slug', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='service/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='technique/items/', verbose_name='Изображение')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.car', verbose_name='Изображение для')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='option',
            field=models.ManyToManyField(blank=True, to='api.CarOptions', verbose_name='Опции'),
        ),
        migrations.AddField(
            model_name='car',
            name='service',
            field=models.ManyToManyField(blank=True, to='api.Service', verbose_name='Услуги'),
        ),
        migrations.AddField(
            model_name='car',
            name='subcategory',
            field=models.ManyToManyField(blank=True, to='api.AutoSubCategory', verbose_name='Подкатегории'),
        ),
    ]
