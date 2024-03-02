from django.urls import path 
from .views import home, receiptcosts, product_detail, delete_product_ingredient, update_product_ingredient, get_product_ingredient_data, get_ingredients, add_product_ingredient, ingredients, get_ingredient_units, download_product_data_excel, download_ingredients_data_excel, download_products_with_ingredients

urlpatterns = [
    path('', home, name="home"),
    path('receipt_home', home, name="receipt-home"),
    path('receipt_costs', receiptcosts, name="receipt-costs"),
    path('recipe_book/<int:product_id>', product_detail, name="product_detail"),
    path('delete_product_ingredient/', delete_product_ingredient, name='delete_product_ingredient'),
    path('get_product_ingredient_data/<int:ingredient_id>/', get_product_ingredient_data, name='get_product_ingredient_data'),
    path('update_product_ingredient/', update_product_ingredient, name='update_product_ingredient'),
    path('add_product_ingredient/', add_product_ingredient, name='add_product_ingredient'),
    path('ruta_para_obtener_ingredientes/', get_ingredients, name='ruta_para_obtener_ingredientes'),
    path('ruta_para_obtener_ingredientes_units/', get_ingredient_units, name='ruta_para_obtener_ingredientes_units'),
    path('ingredients', ingredients, name="ingredients"),
    path('download_product_data_excel/', download_product_data_excel, name='download_product_data_excel'),
    path('download_ingredients_data_excel/', download_ingredients_data_excel, name='download_ingredients_data_excel'),
    path('download_products_with_ingredients/', download_products_with_ingredients, name='download_products_with_ingredients'),
]
