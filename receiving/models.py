from django.db import models
from django.contrib.auth.models import User


class Inventory(models.Model):
    sender = models.CharField(max_length=255)
    document = models.FileField(upload_to="media/")
    signature = models.CharField(max_length=128)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiving_staff")
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Inventories"

    def __str__(self):
        return self.sender


CATEGORIES = (
    (1, "Outfits"),
    (2, "Electronics"),
    (3, "Toys"),
    (4, "Tools"),
)

UNIT = (
    (1, "KILO"),
    (2, "PIECE"),
    (3, "LITRES"),
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.IntegerField(choices=CATEGORIES)
    amount = models.FloatField()
    unit = models.IntegerField(choices=UNIT)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="related_inventory")
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.name
