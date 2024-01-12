from django.db import models


class Frame(models.Model):
    color = models.CharField(max_length=64)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Seat(models.Model):
    color = models.CharField(max_length=64)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Tire(models.Model):
    type = models.CharField(max_length=64)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type


class Basket(models.Model):
    quantity = models.IntegerField()


class Bike(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    has_basket = models.BooleanField()

    def __str__(self):
        return self.name


class Order(models.Model):
    READY = 'R'
    PENDING = 'P'
    STATUS = [
        (READY, 'ready'),
        (PENDING, 'pending'),
    ]
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    status = models.CharField(max_length=2, choices=STATUS)

