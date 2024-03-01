from django.db import models
from django.db.models import Sum, F

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)
    date = models.DateField(auto_now_add=True)
    yield_quantity = models.PositiveIntegerField(default=1)
    ingredients = models.ManyToManyField('Ingredient', through='ProductIngredient')

    def __str__(self):
        return self.name

    # En caso de agregar q x p
    def get_total_cost(self):
        return self.productingredient_set.aggregate(
            total_cost=Sum(F('cost') * F('quantity'), output_field=models.DecimalField())
        )['total_cost'] or 0

    # En caso de agregar costo completo x ingrediente y unidades utilizadas
    def get_total_ingredient_cost(self):
        return self.productingredient_set.aggregate(
            total_cost=Sum(F('cost'), output_field=models.DecimalField())
        )['total_cost'] or 0
    
    def get_cost_per_unit(self):
        # total_cost = self.get_total_cost()
        total_cost = self.get_total_ingredient_cost()
        # Asegúrate de no dividir por cero
        if self.yield_quantity > 0:
            cost_per_unit = total_cost / self.yield_quantity
            return round(cost_per_unit, 4)
        return 0

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=[
        ('kg', 'Kilogramo'),
        ('g', 'Gramo'),
        ('unit', 'Unidad'),
        ('l', 'Litro'),
        ('ml', 'Mililitro'),
    ])

    def get_total_ingredient_cost(self):
        return self.productingredient_set.aggregate(
            total_cost=Sum(F('cost'), output_field=models.DecimalField())
        )['total_cost'] or 0
    
    def get_ingredient_cost_per_unit(self):
        # total_cost = self.get_total_cost()
        total_cost = self.get_total_ingredient_cost()
        # Asegúrate de no dividir por cero
        if self.quantity > 0:
            cost_per_unit = total_cost / self.quantity
            return round(cost_per_unit, 4)
        return 0

    def __str__(self):
        return f"{self.product.name} - {self.ingredient.name}: {self.quantity} {self.unit} at ${self.cost}"
