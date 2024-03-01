from django.contrib import admin
from .models import Product, Ingredient, ProductIngredient

class ProductIngredientInline(admin.TabularInline):
    model = ProductIngredient
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductIngredientInline, ]
    list_display = ('name', 'description', 'date')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date')

class ProductIngredientAdmin(admin.ModelAdmin):
    list_display = ('product', 'ingredient', 'cost', 'quantity', 'unit')
    list_filter = ('product', 'ingredient')
    search_fields = ('product__name', 'ingredient__name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(ProductIngredient, ProductIngredientAdmin)
