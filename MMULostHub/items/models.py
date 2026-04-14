from django.db import models

# yf-storage (Items Categories)

class ItemCategory (models.Model):
    
    # ('storage name inside sqlite', 'display name on website')
    CATEGORY_CHOICES = [
        (   'electronics'  ,    'Electronic Devices'),
        (   'stationary'   ,    'Stationaries'      ),
        (   'wallet'       ,    'Wallets'           ),
        (   'card'         ,    'Cards'             ),
        (   'bottle'       ,    'Water Bottles'     ),
        (   'bag'          ,    'Bags'              ),
        (   'key'          ,    'Keys'              ),
        (   'umbrella'     ,    'Umbrellas'         ),
        (   'keychain'     ,    'Keychains'         ),
        (   'clothes'      ,    'Clothes'           ),
        (   'shoes'        ,    'Shoes'             ),
        (   'accessory'    ,    'Accessories'       ),
        (   'other'        ,    'Other Items'       ),
    ]

    # Add name for the storage item inside the category
    # Contoh : Iphone, Nike Shoe ...
    itemName = models.CharField(
        max_length = 100,                 # Name can have 100 characters
    )

    # Add description for the storage item **maybe can used inside create post
    description = models.TextField(
        max_length = 10000,
        blank = True,                     # Description can be empty
    )

    itemCategory = models.CharField(
        max_length = 100,
        choices = CATEGORY_CHOICES,
    )

    # Display name of the item on the admin page
    # Contoh : √ Laptop ✗ Item Obeject 1
    def __str__(self):
        return self.itemName

class MMULocation (models.Model):

    LOCATION_CHOICES = [
        ('fci', 'FCI Building'),
        ('fom', 'FOM Building'),
        ('faie', 'FAIE Building'),
        ('fcm', 'FCM Building'),
        ('libary', 'Library / LP'),
        bakery
        hjtp
        ('dtc', 'Dewan Tun Chancellor (DTC)'),
        ips
        chanselory
        ('clc', 'CLC'),
        ('', 'Other Locations'),

    ]