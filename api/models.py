from django.db import models
from pytils.translit import slugify
from django.utils.safestring import mark_safe


class Banner(models.Model):
    text = models.CharField('Текст', max_length=255, blank=False, null=True)

    image = models.ImageField('Фото', upload_to='service/', blank=True, null=True)

    def __str__(self):
        return f'Баннер id {self.id}'

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

class Service(models.Model):
    name = models.CharField('Название услуги', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Фото', upload_to='service/', blank=True, null=True)
    show_at_index = models.BooleanField('Отображать на главной?', default=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.name_slug = slug

        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return f'Услуга {self.name}'

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class AutoCategory(models.Model):
    name = models.CharField('Категория в автопарке', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Фото', upload_to='autopark/', blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.name_slug = slug
        super(AutoCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'Категория в автопарке {self.name}'

    class Meta:
        verbose_name = "Категория в автопарке"
        verbose_name_plural = "Категории в автопарке"


class AutoSubCategory(models.Model):
    category = models.ForeignKey(AutoCategory, blank=False, null=True, on_delete=models.SET_NULL,
                                    verbose_name='Категория',related_name='subcategory')
    name = models.CharField('Подкатегория в автопарке', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.name_slug = slug

        super(AutoSubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'Подкатегория в автопарке {self.name}'

    class Meta:
        verbose_name = "Подкатегория в автопарке"
        verbose_name_plural = "Подкатегория в автопарке"

class CarOptions(models.Model):
    name = models.CharField('Опция', max_length=255, blank=False, null=True)
    image = models.ImageField('Фото', upload_to='car/options/', blank=True, null=True)

    def __str__(self):
        return f'Опция {self.name}'

    class Meta:
        verbose_name = "Опция"
        verbose_name_plural = "Опции"

class Car(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    subcategory = models.ManyToManyField(AutoSubCategory, blank=True, verbose_name='Подкатегории',related_name='cars')
    service = models.ManyToManyField(Service, blank=True, verbose_name='Услуги')
    option = models.ManyToManyField(CarOptions, blank=True, verbose_name='Опции')
    price_hour = models.IntegerField('Стоимость за час',blank=True,null=True)
    price_km = models.IntegerField('Стоимость за km',blank=True,null=True)
    min_hour = models.IntegerField('Минимально часов',blank=True,null=True)
    seats = models.IntegerField('Мест' ,blank=True,null=True)
    description = models.TextField('Описание', blank=True,null=True)
    show_at_index = models.BooleanField('Отображать на главной?', default=False)
    is_active = models.BooleanField('Отображать?', default=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.name_slug = slug
        super(Car, self).save(*args, **kwargs)

    def get_cat_name(self):
        return self.subcategory.all().first().category.name

    def get_cat_slug(self):
        return self.subcategory.all().first().category.name_slug

    def __str__(self):
        return f'Транспорт {self.name}'

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"

class CarImage(models.Model):
    car = models.ForeignKey(Car, blank=False, null=True, on_delete=models.CASCADE,
                                verbose_name='Изображение для',related_name='images')
    image = models.ImageField('Изображение', upload_to='technique/items/', blank=False, null=True)


    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    image_tag.short_description = 'Изображение'