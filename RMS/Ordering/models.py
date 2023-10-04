from django.db import models


# Model to handle the Menu data as required. like name, description and price
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

# Model to deal with all Table data and status. it can show if table is taken or vacant or reserved
class Tables(models.Model):
    OCCUPIED = 'occupied' # here is to mention the choices that a waiter has to select when monitoring the table
    BOOKED = 'booked'
    VACANT = 'Vacant'

    TABLE_STATUS_CHOICES = [
        (OCCUPIED, 'occupied'),
        (BOOKED, 'booked'),
        (VACANT, 'vacant'),
    ]

    table_number = models.IntegerField(unique=True)
    table_status = models.CharField(max_length=30, choices=TABLE_STATUS_CHOICES, default=VACANT)

    def __str__(self):
        return f"Table {self.table_number} - {self.table_status}"

# Model class to store all order history and related data
class Orders(models.Model):
    DONE = 'DONE'
    ONGOING = 'ONGOING'
    NONE = 'NONE'

    ORDER_STATUS =[
        (DONE, 'DONE'),
        (ONGOING, 'ONGOING'),
        (NONE, 'NONE')
    ]

    order_id = models.IntegerField(default=1)
    name_of_menu_ordered = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customer_preferences = models.CharField(max_length=500)
    customer_name = models.CharField(max_length=100, default='your name')
    waiter = models.CharField(max_length=100, default="waiter's name")
    table_of_order = models.ForeignKey(Tables, on_delete=models.CASCADE, default='1')
    status = models.CharField(max_length=30, choices=ORDER_STATUS, default=NONE)

    def __str__(self):
        return str(self.order_id)






        


