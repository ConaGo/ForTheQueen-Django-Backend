from django import db
from django.contrib import admin

from server.models import Character
from server.models import Inventory
from server.models import Item
from server.models import Profile
from server.models import Savestate
from server.models import UserSession
from server.models.inventory import EquipSlot


class EquippedItemInline(admin.TabularInline):
    model = EquipSlot
    extra = 3


class InventoryAdmin(admin.ModelAdmin):
    inlines = (EquippedItemInline,)


admin.site.register(Character)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Item)
admin.site.register(Profile)
admin.site.register(Savestate)
admin.site.register(UserSession)
