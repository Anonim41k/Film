from django.contrib import admin
from .models import *


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title' ,'release_year', 'genre', 'duration', 'rating', 'film_actor')
    list_filter = ('title' ,'release_year', 'genre', 'duration', 'rating', 'film_actor__last_name')
    search_fields = ('title' ,'release_year', 'genre', 'duration', 'rating', 'film_actor__last_name')
    ordering = ('title' ,'release_year', 'genre', 'duration', 'rating', 'film_actor__last_name')
    fields = ('title' ,'release_year', 'genre', 'duration', 'rating', 'film_actor')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'address', 'phone_number', 'email', 'rentals_count')
    list_filter = ('last_name', 'first_name', 'address', 'phone_number', 'email', 'rentals_count', 'clients_films__title')
    search_fields = ('last_name', 'first_name', 'address', 'phone_number', 'email', 'rentals_count', 'clients_films__title')
    ordering = ('last_name', 'first_name', 'address', 'phone_number', 'email', 'rentals_count', 'clients_films__title')
    fields = ('last_name', 'first_name', 'address', 'phone_number', 'email', 'rentals_count', 'clients_films' )


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('film_name', 'start_date', 'price', 'end_date', 'returns', 'rental_studio')
    list_filter = ('film_name', 'start_date', 'price', 'end_date', 'returns', 'rental_studio__name')
    search_fields = ('film_name', 'start_date', 'price', 'end_date', 'returns', 'rental_studio__name')
    ordering = ('film_name', 'start_date', 'price', 'end_date', 'returns','rental_studio__name')
    fields = ('film_name', 'start_date', 'price', 'end_date', 'returns', 'rental_studio')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date', 'country', 'num_of_movies', 'age', 'actor_studio')
    list_filter = ('last_name', 'first_name', 'birth_date', 'country', 'num_of_movies', 'age', 'actor_studio__name')
    search_fields = ('last_name', 'first_name', 'birth_date', 'country', 'num_of_movies', 'age', 'actor_studio__name')
    ordering = ('last_name', 'first_name', 'birth_date', 'country', 'num_of_movies', 'age', 'actor_studio__name')
    fields = ('last_name', 'first_name', 'birth_date', 'country', 'num_of_movies', 'age', 'actor_studio')


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_year', 'country', 'number_of_films', 'revenue', 'studio_film')
    list_filter = ('name', 'founded_year', 'country', 'number_of_films', 'revenue', 'studio_film__title')
    search_fields = ('name', 'founded_year', 'country', 'number_of_films', 'revenue', 'studio_film__title')
    ordering = ('name', 'founded_year', 'country', 'number_of_films', 'revenue', 'studio_film__title')
    fields = ('name', 'founded_year', 'country', 'number_of_films', 'revenue', 'studio_film')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date', 'film_company', 'experience', 'genre')
    list_filter = ('last_name', 'first_name', 'birth_date', 'film_company', 'experience', 'genre', 'directors_actors__last_name')
    search_fields = ('last_name', 'first_name', 'birth_date', 'film_company', 'experience', 'genre', 'directors_actors__last_name')
    ordering = ('last_name', 'first_name', 'birth_date', 'film_company', 'experience', 'genre', 'directors_actors__last_name')
    fields =  ('last_name', 'first_name', 'birth_date', 'film_company', 'experience', 'genre', 'directors_actors')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('price', 'volume', 'return_date', 'order_date', 'order_client')
    list_filter = ('price', 'volume', 'return_date', 'order_date', 'order_client__last_name')
    search_fields = ('price', 'volume', 'return_date', 'order_date', 'order_client__last_name')
    ordering = ('price', 'volume', 'return_date', 'order_date', 'order_client__last_name')
    fields =  ('price', 'volume', 'return_date', 'order_date', 'order_client')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'amount', 'payment_terms', 'debt', 'payment_date', 'payment_order')
    list_filter = ('payment_type', 'amount', 'payment_terms', 'debt', 'payment_date', 'payment_order__price')
    search_fields = ('payment_type', 'amount', 'payment_terms', 'debt', 'payment_date', 'payment_order__price')
    ordering = ('payment_type', 'amount', 'payment_terms', 'debt', 'payment_date', 'payment_order__price')
    fields = ('payment_type', 'amount', 'payment_terms', 'debt', 'payment_date', 'payment_order')


