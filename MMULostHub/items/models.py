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
        ('clc', 'CLC'),
        ('mph', 'MPH / Annex Hall'),
        ('misri-plaza', 'Misri Plaza'),
        ('rimbun-ilmu', 'Rimbun Ilmu'),
        ('dtc', 'DTC'),
        ('chancelery', 'MMU Chancelery'),
        ('stad', 'STAD Building'),
        ('ips', 'IPS Building'),
        ('library', 'Library'),
        ('bakery', 'Bakery'),
        ('haji-tapah', 'Haji Tapah'),
        ('starbees', 'Starbees'),
        ('dapo-sahang', 'Dapo Sahang'),
        ('hb1', 'Hostel Block 1'),
        ('hb2', 'Hostel Block 2'),
        ('hb3', 'Hostel Block 3'),
        ('hb4', 'Hostel Block 4'),
        ('entrance-A', 'MMU Entrance A'),
        ('entrance-B', 'MMU Entrance B'),
        ('bustop-A', 'Bustop Entrance A'),
        ('bustop-B', 'Bustop Entrance B'),
        ('cyberpark', 'MMU Cyberpark'),
        ('stadium', 'Stadium MMU'),
        ('isc', 'Indoor Sports Centre'),
        ('footbal', 'Football Field'),
        ('rugby', 'Rugby Field'),
        ('swimming', 'Swimming Pool'),
        ('tennis', 'Tennis Court'),
        ('basketball', 'Basketball Court'),
        ('volleyball', 'Volleyball Court'),
        ('archery', 'Archery'),
        ('edc', "EDC Building"),
        ('fmd', 'FMD Building'),
        ('masjid', 'Masjid'),
        ('nea', 'NEA'),
        ('eaa', 'EAA'),
        ('eab', 'EAB'),
        ('guest house', 'MMUGuest House'),
    ]