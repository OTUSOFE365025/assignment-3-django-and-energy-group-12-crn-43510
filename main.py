############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few users in the database
Product.objects.get_or_create(upc="12345", name="Cereal", price=4.47)
Product.objects.get_or_create(upc="67890", name="Bread", price=2.48)
Product.objects.get_or_create(upc="90210", name="Eggs", price=3.93)
Product.objects.get_or_create(upc="29577", name="Tea", price=2.90)
Product.objects.get_or_create(upc="41410", name="Grapes", price=6.70)
Product.objects.get_or_create(upc="89283", name="Donuts", price=2.00)

for u in Product.objects.all():
    print(f'Name: {u.name} \tUPC: {u.upc}  \tPrice: {u.price}')
