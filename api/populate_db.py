# populate_db.py
import json
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from your_app_name.models import Product

# JSON data to be inserted
json_data = [
    {
        "name": "Crude Oil",
        "category": "Energy",
        "quantity": 5000000,
        "unit": "barrels",
        "country_of_origin": "Saudi Arabia",
        "exported_to": ["United States", "China", "India"],
        "unit_price": 75.50,
        "total_value": 377500000,
        "description": "Unrefined petroleum oil used for fuel and energy production."
    },
    {
        "name": "Wheat",
        "category": "Agriculture",
        "quantity": 200000,
        "unit": "metric tons",
        "country_of_origin": "United States",
        "exported_to": ["Egypt", "Indonesia", "Philippines"],
        "unit_price": 250.00,
        "total_value": 50000000,
        "description": "High-quality durum wheat used in food production and animal feed."
    },
    {
        "name": "Automobile Parts",
        "category": "Manufacturing",
        "quantity": 100000,
        "unit": "units",
        "country_of_origin": "Germany",
        "exported_to": ["Brazil", "Mexico", "South Korea"],
        "unit_price": 1500.00,
        "total_value": 150000000,
        "description": "Essential automobile components for various car models, including engines and transmissions."
    },
    # Add the remaining JSON objects here...
]

# Insert data into the database
for entry in json_data:
    product, created = Product.objects.get_or_create(
        name=entry['name'],
        defaults={
            "category": entry["category"],
            "quantity": entry["quantity"],
            "unit": entry["unit"],
            "country_of_origin": entry["country_of_origin"],
            "exported_to": entry["exported_to"],
            "unit_price": entry["unit_price"],
            "total_value": entry["total_value"],
            "description": entry["description"]
        }
    )
    if created:
        print(f"Inserted {product.name} into the database.")
    else:
        print(f"{product.name} already exists in the database.")
