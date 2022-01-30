from django.db import models

from server.models.character import Character


class Item(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Inventory(models.Model):
    items = models.ManyToManyField(Item, through="EquipSlot")
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inventory of {self.character.savestate.profile.user.username}"


class EquipSlot(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="equipslots")
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
