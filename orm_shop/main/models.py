from django.db import models
from django.utils.translation import gettext as _


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.CharField(verbose_name='Модель', max_length=200)
    year = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    color = models.CharField(verbose_name='Цвет', max_length=50)
    mileage = models.PositiveIntegerField(verbose_name='Пробег, км')
    volume = models.DecimalField(verbose_name='Объем двигателя, л', max_digits=5, decimal_places=2)
    body_type = models.CharField(verbose_name='Тип кузова', max_length=20, choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField(verbose_name='Привод', max_length=10, choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField(verbose_name='Коробка передач', max_length=10, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(verbose_name='Тип топлива', max_length=10, choices=FUEL_TYPE_CHOICES)
    price = models.PositiveIntegerField(verbose_name='Цена, руб')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.model


class Sale(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    created_at = models.DateTimeField(verbose_name='Дата и время продажи', auto_now_add=True)

    class Meta:
        verbose_name = 'Продажа автомобиля'
        verbose_name_plural = 'Продажи автомобилей'

    def __str__(self):
        return f'Продажа {self.car.model} {self.car.year} {self.client.name}'
