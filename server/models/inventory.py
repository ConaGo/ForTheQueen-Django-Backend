from django.db import models

from server.models.savestate import Savestate


class Item(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Inventory(models.Model):
    savestate = models.ForeignKey(Savestate, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)


class EquipSlot(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class EquipSlot(models.TextChoices):
        INVENTORY = "IN"
        HEAD = "HE"
        CHEST = "CH"
        LEGS = "LE"
        FEET = "FE"
        RING_LEFT = "RL"
        RING_RIGHT = "RR"

    equip_slot = models.CharField(
        max_length=2, choices=EquipSlot.choices, default=EquipSlot.INVENTORY
    )
