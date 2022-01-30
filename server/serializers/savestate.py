from rest_framework import serializers

from server.models import Character
from server.models import Inventory
from server.models import Item
from server.models import Savestate
from server.models.inventory import EquipSlot


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["name"]


class EquipSlotSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = EquipSlot
        fields = ["item", "equip_slot"]


class InventorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    items = EquipSlotSerializer(source="equipslots", many=True)

    class Meta:
        model = Inventory
        fields = ["id", "items"]


class CharacterSerializer(serializers.Serializer):
    inventory = InventorySerializer()

    class Meta:
        model = Character
        fields = ["hp_max", "hp_current", "class_type", "inventory"]


class SavestateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    characters = CharacterSerializer(many=True, max_length=3, min_length=1)

    class Meta:
        model = Savestate
        fields = ["current_level", "characters"]

    def create(self, validated_data):
        characters_data = validated_data.pop("characters")
        savestate = Savestate.objects.create(**validated_data)
        for character_data in characters_data:
            character = Character.objects.create(savestate=savestate, **character_data)

        return savestate
