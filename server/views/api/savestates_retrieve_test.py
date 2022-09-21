from ddf import F
from ddf import G
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from server.models import Character
from server.models import EquipSlot
from server.models import Inventory
from server.models import Item
from server.models import Profile
from server.models import Savestate
from server.views.api.savestates import SavestateViewset


class SavestateViewsetRetrieveTest(TestCase):
    def setUp(self):
        self.view = SavestateViewset.as_view({"get": "list"})
        self.factory = APIRequestFactory()
        self.admin = G(User, is_superuser=True)
        self.staff = G(User, is_staff=True)

        self.user = G(User)
        self.savestate = G(Savestate, profile=self.user.profile)
        character_1 = G(Character, savestate=self.savestate)
        character_2 = G(Character, savestate=self.savestate)

        G(Inventory, character=character_1, items=3)
        G(Inventory, character=character_2, items=2)

        self.other_user = G(User)
        self.other_savestate = G(Savestate, profile=self.other_user.profile)
        character_other_1 = G(Character, savestate=self.other_savestate)
        G(Inventory, character=character_other_1, items=1)

    def test_setup(self):
        savestates = list(Savestate.objects.all())
        self.assertEqual(len(savestates), 2)
        characters = list(Character.objects.all())
        self.assertEqual(len(characters), 3)
        equip = list(EquipSlot.objects.all())
        self.assertEqual(len(equip), 6)
        inventories = list(Inventory.objects.all())
        self.assertEqual(len(inventories), 3)
        items = list(Item.objects.all())
        self.assertEqual(len(items), 6)

    def test_with_normal_user(self):
        # Arrange
        request = self.factory.get("/api/savestates", format="json")
        force_authenticate(request, user=self.user)
        # Act
        response = self.view(request)
        # Assert
        assert response.status_code is 200
        assert response.data is not None
        assert len(response.data) is 1
        savestate = response.data[0]
        assert "characters" in savestate.keys()
        assert len(savestate["characters"]) is 2

        characters = savestate["characters"]
        assert "inventory" in characters[0].keys()

        inventory = characters[0]["inventory"]
        assert "items" in inventory.keys()
        assert len(inventory["items"]) is 3

        item = inventory["items"][0]
        assert "item" in item.keys()
        assert "equip_slot" in item.keys()

    def test_with_other_user(self):
        request = self.factory.get("/api/savestates", format="json")
        force_authenticate(request, user=self.other_user)
        # Act
        response = self.view(request)
        assert len(response.data[0]["characters"]) is 1

    def test_with_admin(self):
        request = self.factory.get("/api/savestates", format="json")
        force_authenticate(request, user=self.admin)
        # Act
        response = self.view(request)
        assert len(response.data) is 2

    def test_with_staff(self):
        request = self.factory.get("/api/savestates", format="json")
        force_authenticate(request, user=self.staff)
        # Act
        response = self.view(request)
        assert len(response.data) is 2

    def test_save(self):
        request = self.factory.post("/api/savestates", format="json")
