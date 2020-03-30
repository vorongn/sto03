from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# from tinymce.models import HTMLField

# from django.urls import reverse
# from django.conf import settings


# Create your models here.


class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=70)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)
    homepage = models.BooleanField('Разместить на главной')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Car(models.Model):
    AKPP = (
        ('механика', 'механика'),
        ('автомат', 'автомат'),
        ('easytronic', 'easytronic'),

    )
    vin = models.CharField('VIN код', max_length=20)
    brend_car = models.CharField('марка', max_length=20)
    model_car = models.CharField('модель', max_length=20)
    year = models.IntegerField('год выпуска')
    motor = models.CharField('двигатель', max_length=10)
    transmission = models.CharField('КПП', max_length=10,
                                    choices=AKPP,
                                    default='механика')
    number = models.CharField('госномер', max_length=10)
    photo = models.ImageField('фото', upload_to='cars/', default='cars/nophotocars.jpg')
    description = models.TextField('описание', max_length=500, blank=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['number']


class Client(models.Model):
    STATUS_TYPES = (
        ('новый', 'без скидок'),
        ('скидка', 'скидка'),
    )
    first_name = models.CharField('имя', max_length=50)
    last_name = models.CharField('фамилия', max_length=50)
    phone_number = models.CharField('телефон', max_length=15)
    photo = models.ImageField('фото', upload_to='clients/', default='clients/def.jpg')
    status = models.CharField('статус', max_length=20,
                              choices=STATUS_TYPES,
                              default='без скидок')
    description = models.TextField('описание', blank=True)
    date_create = models.DateTimeField('дата регистрации', auto_now_add=True)
    cars = models.ManyToManyField(Car, related_name='cars', blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Work(models.Model):
    work = models.CharField('вид работы', max_length=50)
    description = models.TextField('описание работы', blank=True)

    def __str__(self):
        return self.work

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'


class Repair(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_mileage = models.IntegerField('пробег', blank=True)
    date = models.DateTimeField('дата', default=timezone.now)
    repworks = models.ManyToManyField(Work, related_name='works')
    description = models.TextField('Описание работ и проблем')
    repair_cost = models.IntegerField('Стоимость ремонта BYN', default=0)
    photo01 = models.ImageField('фото01', upload_to='repairs/', default='repairs/nophoto.png')
    photo02 = models.ImageField('фото02', upload_to='repairs/', default='repairs/nophoto.png')
    photo03 = models.ImageField('фото03', upload_to='repairs/', default='repairs/nophoto.png')

    class Meta:
        verbose_name = 'Заказ-наряд'
        verbose_name_plural = 'Ремонты'
