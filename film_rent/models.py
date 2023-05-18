from django.db import models
from datetime import date

class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва фільму')
    release_year = models.PositiveIntegerField(verbose_name='Рік зйомки')
    genre = models.CharField(max_length=255, verbose_name='Жанр')
    duration = models.PositiveIntegerField(verbose_name='Тривалість')
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Рейтинг')
    film_actor = models.ForeignKey('Actor', on_delete=models.CASCADE, null=True, blank=True, related_name='film_actor', verbose_name='Актор')

    class Meta:
        verbose_name_plural = 'Фільми'

    def __str__(self):
        return f'film-{self.id}'

class Client(models.Model):
    last_name = models.CharField(max_length=255, verbose_name='Прізвище клієнта')
    first_name = models.CharField(max_length=255, verbose_name='Ім\'я клієнта')
    address = models.CharField(max_length=255, verbose_name='Адреса')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Електронна пошта')
    rentals_count = models.PositiveIntegerField(default=0, verbose_name='Кількість прокатів')
    clients_films = models.ManyToManyField('Film', null=True, blank=True, verbose_name='Фільми')

    class Meta:
        verbose_name_plural = 'Клієнти'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Rental(models.Model):
    film_name = models.CharField(max_length=255, verbose_name='Назва фільму')
    start_date = models.DateField(default=date.today, verbose_name='Дата початку прокату')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна прокату')
    end_date = models.DateField(default=date.today, verbose_name='Дата закінчення прокату')
    returns = models.IntegerField(default=0, verbose_name='Кількість повернень')
    rental_studio = models.ForeignKey('Studio', on_delete=models.CASCADE, null=True, blank=True, related_name='rental_studio', verbose_name='Студія')

    class Meta:
        verbose_name_plural = 'Прокати'

    def __str__(self):
        return f'{self.price}, {self.film_name}'

class Actor(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Прізвище актора')
    first_name = models.CharField(max_length=50, verbose_name="Ім'я актора")
    birth_date = models.DateField(verbose_name='Дата народження')
    country = models.CharField(max_length=50, verbose_name='Країна')
    num_of_movies = models.IntegerField(verbose_name='Кількість зйомок')
    age = models.IntegerField(verbose_name='Вік')
    actor_studio = models.ForeignKey('Studio', on_delete=models.CASCADE, null=True, blank=True, related_name='actor_studio', verbose_name='Студія')

    class Meta:
        verbose_name_plural = 'Актори'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Studio(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва')
    founded_year = models.PositiveIntegerField(verbose_name='Рік заснування')
    country = models.CharField(max_length=50, verbose_name='Країна')
    number_of_films = models.PositiveIntegerField(verbose_name='Кількість знятих фільмів')
    revenue = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Прибуток')
    studio_film = models.ForeignKey('Film', on_delete=models.CASCADE, null=True, blank=True, related_name='studio_film', verbose_name='Фільм')

    class Meta:
        verbose_name_plural = 'Студії'

    def __str__(self):
        return f'{self.name}'

class Director(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Прізвище режисера')
    first_name = models.CharField(max_length=50, verbose_name='Ім’я режисера')
    birth_date = models.DateField(verbose_name='Дата народження')
    film_company = models.CharField(max_length=100, verbose_name='Кінокомпанія')
    experience = models.PositiveIntegerField(verbose_name='Стаж')
    genre = models.CharField(max_length=255, verbose_name='Жанр', default=None)
    directors_actors = models.ManyToManyField('Actor', null=True, blank=True, verbose_name='Актор')

    class Meta:
        verbose_name_plural = 'Режисери'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Order(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна замовлення')
    volume = models.IntegerField(verbose_name='Об’єм замовлення')
    return_date = models.DateField(verbose_name='Дата повернення')
    order_date = models.DateField(verbose_name='Дата замовлення')
    order_client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True, blank=True, related_name='order_client', verbose_name='Клієнт')

    class Meta:
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'{self.volume}, {self.order_date}'

class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('CASH', 'Готівка'),
        ('CARD', 'Кредитна картка'),
        ('BANK_TRANSFER', 'Банківський переказ'),
    ]

    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, verbose_name='Тип платежу')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сума')
    payment_terms = models.CharField(max_length=50, verbose_name='Умови оплати')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Борг')
    payment_date = models.DateTimeField(verbose_name='Дата оплати')
    payment_order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True, related_name='payment_order', verbose_name='Замовлення')

    class Meta:
        verbose_name_plural = 'Платежі'

    def __str__(self):
        return f"{self.payment_type} - {self.amount} ({self.payment_date})"