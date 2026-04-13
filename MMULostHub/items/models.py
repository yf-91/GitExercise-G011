from django.db import models

# yf-storage (Items Categories)

class ItemCategory (models.Model):
    
    CATEGIRY_CHOICES = [
        ('electronics', 'Electronic Devices'),
        ('stationary', 'Stationaries'),
        ('wallet', 'Wallets'),
        ('card', 'Cards'),
        ('bottle', 'Water Bottles'),
        ('bag', 'Bags'),
        ('key', 'Keys'),
        ('umbrella', 'Umbrellas'),
        ('keychain', 'Keychains'),
        ('clothes', 'Clothes'),
        ('shoes', 'Shoes'),
        ('accessory', 'Accessories'),
        ('other', 'Other Items'),
    ]