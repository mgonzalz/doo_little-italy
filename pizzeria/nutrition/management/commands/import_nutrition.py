from django.core.management.base import BaseCommand
from nutrition.models import Ingredient
from nutrition.utils import fetch_nutrition

class Command(BaseCommand):
    help = "Import Nutrition Data for Pizza Ingredients fromm Edamam API"

    def handle(self, *args, **kwargs):
        ingredients = {
            "Base": [
                "pizza dough",
                "whole wheat pizza dough",
                "gluten-free pizza dough"
            ],
            "Sauce": [
                "tomato sauce",
                "pesto sauce",
                "white garlic sauce"
            ],
            "Topping": [
                "mozzarella cheese",
                "cheddar cheese",
                "parmesan cheese",
                "pepperoni",
                "mushrooms",
                "onions",
                "green peppers",
                "black olives",
                "pineapple",
                "basil",
                "dried oregano",
                "chicken",
                "ham",
                "bacon",
                "italian sausage"
            ]
        }

        base_quantity = "1 cup"
        for category, items in ingredients.items():
            for name in items:
                query = f"{base_quantity} {name}"
                data = fetch_nutrition(query)
                if data:
                    calories = data.get("calories", 0)
                    total_nutrients = data.get("totalNutrients", {})
                    fats = total_nutrients.get("FAT", {}).get("quantity", 0)
                    proteins = total_nutrients.get("PROCNT", {}).get("quantity", 0)
                    carbohydrates = total_nutrients.get("CHOCDF", {}).get("quantity", 0)
                    price_per_unit = 3.0 if category == "Base" else (2.0 if category == "Sauce" else 1)

                    Ingredient.objects.update_or_create(
                        name=name,
                        defaults={
                            "category": category,
                            "calories_per_unit": calories,
                            "fats_per_unit": fats,
                            "proteins_per_unit": proteins,
                            "carbohydrates_per_unit": carbohydrates,
                            "price_per_unit": price_per_unit,
                        },
                    )
                    self.stdout.write(f"Added/Updated ingredient: {name} ({category})")
                else:
                    self.stdout.write(f"Failed to fetch data for: {name}")
