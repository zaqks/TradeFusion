"""# populate_db.py
import json
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_main_app.settings")
django.setup()

from stocks_app.models import Stock

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
json_data =  [
    "https://www.google.com/imgres?q=oil%20barrels&imgurl=https%3A%2F%2Fwww.europecaribbeanline.com%2Fassets%2Ffiles%2Fessential-guide-to-barrel-shipping-for-oil-riggers.webp&imgrefurl=https%3A%2F%2Fwww.europecaribbeanline.com%2Flogistics%2Fessential-guide-to-barrel-shipping-for-oil-riggers%2F&docid=CsmcQq6GT1N2XM&tbnid=5flBoHrzHjfBnM&vet=12ahUKEwi4q8WHoLqJAxUpfKQEHXHWJQ0QM3oECEwQAA..i&w=1254&h=836&hcb=2&ved=2ahUKEwi4q8WHoLqJAxUpfKQEHXHWJQ0QM3oECEwQAA","https://www.google.com/imgres?q=Wheat&imgurl=http%3A%2F%2Fstandishmilling.com%2Fcdn%2Fshop%2Ffiles%2Fl-intro-1664307140_grande.jpg%3Fv%3D1722858758&imgrefurl=https%3A%2F%2Fstandishmilling.com%2Fproducts%2Fwheat-grain-50-lb-bag&docid=rRkySZN-jO2BwM&tbnid=F52LnLA5JEcJfM&vet=12ahUKEwiQg_SpoLqJAxUlUaQEHeXjMX8QM3oECBkQAA..i&w=600&h=338&hcb=2&ved=2ahUKEwiQg_SpoLqJAxUlUaQEHeXjMX8QM3oECBkQAA","https://www.google.com/imgres?q=wheat%20&imgurl=http%3A%2F%2Fstandishmilling.com%2Fcdn%2Fshop%2Ffiles%2Fl-intro-1664307140_grande.jpg%3Fv%3D1722858758&imgrefurl=https%3A%2F%2Fstandishmilling.com%2Fproducts%2Fwheat-grain-50-lb-bag&docid=rRkySZN-jO2BwM&tbnid=F52LnLA5JEcJfM&vet=12ahUKEwia9anwoLqJAxXRRaQEHYdULzwQM3oECBsQAA..i&w=600&h=338&hcb=2&ved=2ahUKEwia9anwoLqJAxXRRaQEHYdULzwQM3oECBsQAA","https://www.google.com/imgres?q=Automobile%20Parts&imgurl=https%3A%2F%2Fokcredit-blog-images-prod.storage.googleapis.com%2F2021%2F06%2Fautomobile-parts1--1-.jpg&imgrefurl=https%3A%2F%2Fokcredit.in%2Fblog%2Fhow-to-start-automobile-parts-manufacturing-business%2F&docid=CelNlDuB1fKrDM&tbnid=NsxqKGQf5RPc6M&vet=12ahUKEwiFxOrPoLqJAxU0RqQEHfO3BXIQM3oECHsQAA..i&w=500&h=334&hcb=2&ved=2ahUKEwiFxOrPoLqJAxU0RqQEHfO3BXIQM3oECHsQAA","https://www.google.com/imgres?q=Pharmaceutical%20Products%20stock&imgurl=https%3A%2F%2Fas1.ftcdn.net%2Fv2%2Fjpg%2F04%2F79%2F17%2F82%2F1000_F_479178289_pgiQfGRCk8PQ3YYpH2NZxxHhOO5Wwd4F.jpg&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fimages%2Fpharmaceutical-products-for-sale-at-a-pharmacy-store%2F479178289&docid=agcgRDhpFfFm2M&tbnid=kCvSW0GOZqNkXM&vet=12ahUKEwiu3om3obqJAxXVcaQEHVxmJoMQM3oECHIQAA..i&w=1000&h=667&hcb=2&itg=1&ved=2ahUKEwiu3om3obqJAxXVcaQEHVxmJoMQM3oECHIQAA","https://www.google.com/imgres?q=Copper%20Ore%20tube&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1255689471%2Fphoto%2Fmany-copper-bobbins-warehouse-copper-pipes.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DIPLKEbZqD3KiKdFq4S8QpRNu3i-sVR7M7WVDHptnhP4%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fcopper-ore&docid=eUaTo3UHAK6eTM&tbnid=6zXprLgFdGLP_M&vet=12ahUKEwiNkNfPobqJAxV5Q6QEHQJZBxgQM3oECHEQAA..i&w=612&h=336&hcb=2&itg=1&ved=2ahUKEwiNkNfPobqJAxV5Q6QEHQJZBxgQM3oECHEQAA","https://www.google.com/imgres?q=natural%20gas%20wagon&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F954463206%2Fphoto%2Frailway-tanker-cars.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DMwqhLk3vuRt22vSJ9tcuRu1LDGwmxwDxwfKQPeeT7RM%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fnatural-gas-train&docid=26hycWCTS9yDlM&tbnid=GCweeSHmWhh8qM&vet=12ahUKEwjc27D_obqJAxX5APsDHe0XMkgQM3oECBoQAA..i&w=612&h=438&hcb=2&ved=2ahUKEwjc27D_obqJAxX5APsDHe0XMkgQM3oECBoQAA","https://www.google.com/imgres?q=Soybeans&imgurl=http%3A%2F%2Fwww.adascan.ca%2Fwp-content%2Fuploads%2Fsoybeans-health-benefits.jpg&imgrefurl=https%3A%2F%2Fwww.adascan.ca%2Fblog%2Fnutrition-facts-health-benefits-soybeans%2F&docid=JyP7BZB1kyfedM&tbnid=scol-mlMktZuqM&vet=12ahUKEwip0s7DorqJAxV4TqQEHSTODuUQM3oFCIABEAA..i&w=822&h=420&hcb=2&ved=2ahUKEwip0s7DorqJAxV4TqQEHSTODuUQM3oFCIABEAA","https://www.google.com/imgres?q=Textile%20Fabrics&imgurl=https%3A%2F%2Fstudy.com%2Fcimages%2Fmultimages%2F16%2Ftextiles413789856903977913.jpg&imgrefurl=https%3A%2F%2Fstudy.com%2Facademy%2Flesson%2Fwhat-are-textiles.html&docid=6sS4FWPU-3LLdM&tbnid=qqdqxSnIQ6GrCM&vet=12ahUKEwjlzNHgorqJAxX9RKQEHaamFDUQM3oECHsQAA..i&w=450&h=290&hcb=2&ved=2ahUKEwjlzNHgorqJAxX9RKQEHaamFDUQM3oECHsQAA","https://www.google.com/imgres?q=Coffee%20Beans&imgurl=https%3A%2F%2Fassets.bonappetit.com%2Fphotos%2F57c5d0e36a6acdf3485dfb2b%2Fmaster%2Fpass%2F3717295073_f5ae257d71_o.jpg&imgrefurl=https%3A%2F%2Fwww.bonappetit.com%2Fdrinks%2Fnon-alcoholic%2Farticle%2Fstoring-coffee&docid=moV9tKfLZdIkKM&tbnid=WnVOrvqzY2uMAM&vet=12ahUKEwic4eb_orqJAxXzdqQEHaMwAygQM3oECH8QAA..i&w=3357&h=2238&hcb=2&ved=2ahUKEwic4eb_orqJAxXzdqQEHaMwAygQM3oECH8QAA","https://www.google.com/imgres?q=Steel&imgurl=https%3A%2F%2Fmillenniumalloys.ca%2Fwp-content%2Fuploads%2F2019%2F10%2FFacts-about-steel-Millennium-Specialty-Alloys-metal-online-1024x684.jpeg&imgrefurl=https%3A%2F%2Fmillenniumalloys.ca%2Fsteel-facts%2F&docid=VOK-nfno07vBLM&tbnid=Jt39HlXd4LVvqM&vet=12ahUKEwimgpuXo7qJAxXLVKQEHZo3GcMQM3oECFQQAA..i&w=1024&h=684&hcb=2&ved=2ahUKEwimgpuXo7qJAxXLVKQEHZo3GcMQM3oECFQQAA"
]

# Insert data into the database
for entry in json_data:
    product, created = Stock.objects.get_or_create(
        name=entry['name'],
        defaults={
            "category": entry["category"],
            "quantity": entry["quantity"],
            "unit": entry["unit"],
            "country_of_origin": entry["countryOfOrigin"],
            "exported_to": entry["exportedTo"],
            "unit_price": entry["unitPrice"],
            "total_value": entry["totalValue"],
            "description": entry["description"]
        }
    )
    if created:
        print(f"Inserted {product.name} into the database.")
    else:
        print(f"{product.name} already exists in the database.")



"""


import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_main_app.settings")
django.setup()

from stocks_app.models import Stock


# Assuming you have a Stock entry for each image and they are in order
for _ in range(10):
    stock_item = Stock.objects.get(id=_ + 1)  # Adjust depending on your indexing
    stock_item.img = f"/static/assets/images/stock/{_+1}.jpg"
    stock_item.save()


