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

    name = models.CharField
    (
        max_length = 100,
    )

    description = models.TextField
    (
        max_length = 10000,
        blank=True,
    )

    category = models.CharField
    (
        max_length = 100,
        choices = CATEGORY_CHOICES,
    )

    def __str__(self):
        return self.name