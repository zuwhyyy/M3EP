import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyInventorySystem.settings')
django.setup()

from MyInventoryApp.models import Supplier, WaterBottle

suppliers_data = [
    {"name": "Meister, Inc.", "city": "Dresden", "country": "Germany", "created_at": "2019-01-20 08:20:00"},
    {"name": "Sailfish, Inc.", "city": "Racoon City", "country": "Canada", "created_at": "2019-03-14 08:21:00"},
    {"name": "Bucky, Inc.", "city": "California", "country": "USA", "created_at": "2018-12-01 08:22:00"},
    {"name": "Custom Supplier", "city": "Custom City", "country": "Custom Country", "created_at": "2022-06-15 10:00:00"},
]

supplier_map = {}
for data in suppliers_data:
    supplier, _ = Supplier.objects.get_or_create(**data)
    supplier_map[data["name"]] = supplier

water_bottles_data = [
    {"sku": "1A1", "brand": "Hydro Flask", "Cost": 3500.00, "size": "18 Oz", "mouth_size": "Wide Mouth", "color": "Black", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "2B1", "brand": "Hydro Flask", "Cost": 3500.00, "size": "18 Oz", "mouth_size": "Wide Mouth", "color": "Blue", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "3C1", "brand": "Hydro Flask", "Cost": 3500.00, "size": "18 Oz", "mouth_size": "Wide Mouth", "color": "White", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "4D1", "brand": "Kleen Kanteen", "Cost": 3000.00, "size": "18 Oz", "mouth_size": "Standard Mouth", "color": "Black", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 100},
    {"sku": "5E1", "brand": "Kleen Kanteen", "Cost": 3000.00, "size": "18 Oz", "mouth_size": "Standard Mouth", "color": "Blue", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 100},
    {"sku": "6F1", "brand": "Nalgene", "Cost": 3000.00, "size": "48 Oz", "mouth_size": "Wide Mouth", "color": "Blue", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 100},
    {"sku": "7G1", "brand": "Hydro Flask", "Cost": 3500.00, "size": "18 Oz", "mouth_size": "Standard Mouth", "color": "White", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 100},
    {"sku": "8H1", "brand": "Nalgene", "Cost": 2000.00, "size": "32 Oz", "mouth_size": "Wide Mouth", "color": "Transparent", "supplied_by": supplier_map["Sailfish, Inc."], "current_quantity": 100},
    {"sku": "9I1", "brand": "Thermos", "Cost": 2500.00, "size": "1 Liter", "mouth_size": "Wide Mouth", "color": "White", "supplied_by": supplier_map["Sailfish, Inc."], "current_quantity": 100},
    {"sku": "10J1", "brand": "Owala", "Cost": 1500.00, "size": "24 Oz", "mouth_size": "Standard Mouth", "color": "Transparent", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "11K1", "brand": "Owala", "Cost": 2500.00, "size": "24 Oz", "mouth_size": "Standard Mouth", "color": "Pink", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "12L1", "brand": "Owala", "Cost": 2500.00, "size": "24 Oz", "mouth_size": "Standard Mouth", "color": "White", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "13M1", "brand": "Owala", "Cost": 3000.00, "size": "32 Oz", "mouth_size": "Standard Mouth", "color": "White", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "14N1", "brand": "Owala", "Cost": 3000.00, "size": "32 Oz", "mouth_size": "Standard Mouth", "color": "Blue", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "15O1", "brand": "Owala", "Cost": 3000.00, "size": "32 Oz", "mouth_size": "Standard Mouth", "color": "Pink", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "16P1", "brand": "Aqua Flask", "Cost": 2500.00, "size": "24 Oz", "mouth_size": "Small Mouth", "color": "Transparent", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 100},
    {"sku": "17Q1", "brand": "Aqua Flask", "Cost": 1500.00, "size": "32 Oz", "mouth_size": "Standard Mouth", "color": "Black", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 150},
    {"sku": "18R1", "brand": "Aqua Flask", "Cost": 3000.00, "size": "24 Oz", "mouth_size": "Wide Mouth", "color": "Blue", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 100},
    {"sku": "19S1", "brand": "Aqua Flask", "Cost": 3500.00, "size": "48 Oz", "mouth_size": "Wide Mouth", "color": "White", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 200},
    {"sku": "20T1", "brand": "Aqua Flask", "Cost": 1500.00, "size": "24 Oz", "mouth_size": "Standard Mouth", "color": "Gray", "supplied_by": supplier_map["Meister, Inc."], "current_quantity": 100},
    {"sku": "21U1", "brand": "Aqua Flask", "Cost": 2500.00, "size": "64 Oz", "mouth_size": "Small Mouth", "color": "Pink", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 250},
    {"sku": "22V1", "brand": "Thermoflask", "Cost": 2000.00, "size": "32 Oz", "mouth_size": "Wide Mouth", "color": "Yellow", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 200},
    {"sku": "23X1", "brand": "Thermoflask", "Cost": 2500.00, "size": "32 Oz", "mouth_size": "Wide Mouth", "color": "Pink", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 200},
    {"sku": "24Y1", "brand": "Thermoflask", "Cost": 3000.00, "size": "24 Oz", "mouth_size": "Small Mouth", "color": "Yellow", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 200},
    {"sku": "25Z1", "brand": "Thermoflask", "Cost": 3000.00, "size": "32 Oz", "mouth_size": "Wide Mouth", "color": "Green", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 200},
    {"sku": "26A2", "brand": "Thermoflask", "Cost": 3500.00, "size": "32 Oz", "mouth_size": "Standard Mouth", "color": "Yellow", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 200},
    {"sku": "27B2", "brand": "Thermoflask", "Cost": 1500.00, "size": "48 Oz", "mouth_size": "Wide Mouth", "color": "Yellow", "supplied_by": supplier_map["Bucky, Inc."], "current_quantity": 200},
]

for data in water_bottles_data:
    WaterBottle.objects.get_or_create(**data)

print("Successfully added")
