from django.db import models


class Road(models.Model):
    PAYMENT_MODE = [('ON', 'ONLINE PAYMENT'), ("EMI", "MONTHLY INSTALLMENT")]
    ROAD_LENGTH = [("2KM", '2000m'), ("3KM", '3000m'), ("4KM", '4000m')]
    contractor_name = models.CharField(max_length=20)
    KM_price = models.IntegerField()
    road_no = models.IntegerField()
    maintaince_price = models.IntegerField()
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE)
    road_length = models.CharField(max_length=10, choices=ROAD_LENGTH)

