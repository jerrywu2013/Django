from django.contrib import admin
from restaurants.models import Restaurant, Food

# Register your models here.
class RestautantAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'address')
	search_fields = ('name',)

class FoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'restaurant', 'price')
	list_filter = ('is_spicy',)
	#fields = ('price', 'restaurant')
	ordering = ('price',)
admin.site.register(Restaurant, RestautantAdmin)
admin.site.register(Food, FoodAdmin)
