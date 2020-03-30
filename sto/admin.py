from django.contrib import admin
from . import models


@admin.register(models.Article)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'pub_date',)
    search_fields = ('article_title',)
    ordering = ('pub_date',)


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number',
                    'status', 'description', 'date_create')
    list_filter = ('first_name', 'last_name', 'date_create', 'status')
    search_fields = ('first_name', 'last_name')
    date_hierarchy = 'date_create'
    ordering = ('first_name', 'last_name', 'date_create', 'status')


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('number', 'brend_car', 'model_car', 'year', 'motor',
                    'transmission')
    search_fields = ('brend_car', 'model_car')


@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('work',)
    search_fields = ('work', 'description')
    ordering = ('work',)


@admin.register(models.Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('car', 'date', 'car_mileage', 'repair_cost')
    search_fields = ('car', 'date')
    ordering = ('date', 'car', 'repair_cost')
