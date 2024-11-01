# populate_db.py
from stocks_app.models import Stock
import json
import os
import django

# Set up Django environment
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_main_app.settings")
#django.setup()


# JSON data to be inserted
json_data = [
    {
        "id": "1",
        "name": "Crude Oil",
        "category": "Energy",
        "quantity": 5000000,
        "unit": "barrels",
        "countryOfOrigin": "Saudi Arabia",
        "exportedTo": ["United States", "China", "India"],
        "unitPrice": 75.50,
        "totalValue": 377500000,
        "description": "Unrefined petroleum oil used for fuel and energy production."
    },
    {
        "id": "2",
        "name": "Wheat",
        "category": "Agriculture",
        "quantity": 200000,
        "unit": "metric tons",
        "countryOfOrigin": "United States",
        "exportedTo": ["Egypt", "Indonesia", "Philippines"],
        "unitPrice": 250.00,
        "totalValue": 50000000,
        "description": "High-quality durum wheat used in food production and animal feed."
    },
    {
        "id": "3",
        "name": "Automobile Parts",
        "category": "Manufacturing",
        "quantity": 100000,
        "unit": "units",
        "countryOfOrigin": "Germany",
        "exportedTo": ["Brazil", "Mexico", "South Korea"],
        "unitPrice": 1500.00,
        "totalValue": 150000000,
        "description": "Essential automobile components for various car models, including engines and transmissions."
    },
    {
        "id": "4",
        "name": "Pharmaceutical Products",
        "category": "Healthcare",
        "quantity": 50000,
        "unit": "kilograms",
        "countryOfOrigin": "Switzerland",
        "exportedTo": ["Canada", "Australia", "South Africa"],
        "unitPrice": 350.00,
        "totalValue": 17500000,
        "description": "Medicines and vaccines exported to meet global healthcare needs."
    },
    {
        "id": "5",
        "name": "Copper Ore",
        "category": "Mining",
        "quantity": 1000000,
        "unit": "metric tons",
        "countryOfOrigin": "Chile",
        "exportedTo": ["Japan", "China", "Germany"],
        "unitPrice": 120.00,
        "totalValue": 120000000,
        "description": "High-grade copper ore for industrial use, particularly in electronics and construction."
    },
    {
        "id": "6",
        "name": "Natural Gas",
        "category": "Energy",
        "quantity": 3000000,
        "unit": "cubic meters",
        "countryOfOrigin": "Russia",
        "exportedTo": ["Europe", "China"],
        "unitPrice": 2.50,
        "totalValue": 7500000,
        "description": "Liquefied natural gas used for heating, electricity generation, and industrial processes."
    },
    {
        "id": "7",
        "name": "Soybeans",
        "category": "Agriculture",
        "quantity": 500000,
        "unit": "metric tons",
        "countryOfOrigin": "Brazil",
        "exportedTo": ["China", "Spain", "Netherlands"],
        "unitPrice": 400.00,
        "totalValue": 200000000,
        "description": "Protein-rich soybeans used in food products, animal feed, and biodiesel production."
    },
    {
        "id": "8",
        "name": "Textile Fabrics",
        "category": "Textiles",
        "quantity": 1000000,
        "unit": "meters",
        "countryOfOrigin": "India",
        "exportedTo": ["United States", "United Kingdom", "Japan"],
        "unitPrice": 10.00,
        "totalValue": 10000000,
        "description": "Cotton and synthetic fabrics used in clothing and industrial materials."
    },
    {
        "id": "9",
        "name": "Coffee Beans",
        "category": "Food & Beverage",
        "quantity": 150000,
        "unit": "metric tons",
        "countryOfOrigin": "Colombia",
        "exportedTo": ["United States", "Germany", "Japan"],
        "unitPrice": 3.50,
        "totalValue": 525000,
        "description": "Arabica and Robusta coffee beans for commercial coffee production."
    },
    {
        "id": "10",
        "name": "Steel",
        "category": "Manufacturing",
        "quantity": 500000,
        "unit": "metric tons",
        "countryOfOrigin": "China",
        "exportedTo": ["United States", "Australia", "India"],
        "unitPrice": 600.00,
        "totalValue": 300000000,
        "description": "High-grade steel for construction, automotive, and industrial use."
    }
]

# Insert data into the database
for entry in json_data:
    product, created = Stock.objects.get_or_create(
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
