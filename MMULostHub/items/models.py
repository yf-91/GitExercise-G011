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

    itemCategory = models.CharField(
        max_length = 100,
        choices = CATEGORY_CHOICES,
    )

    # Display name of the item on the admin page
    # Contoh : √ Laptop ✗ Item Obeject 1
    def __str__(self):
        return self.itemName


class MMULocation (models.Model):
    
    location_code = models.CharField(                   # system or url(weblink) will see
        max_length = 50,
        unique = True,
    )

    location_name = models.CharField(                   # user see
        max_length = 100,
    )

    latitude = models.FloatField(                       # coordinates (lat , long)
        null = True,
        blank = True,
    )

    longitude = models.FloatField(
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.location_name
    