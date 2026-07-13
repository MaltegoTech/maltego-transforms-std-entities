import importlib.util

from maltego.entities import (
    BankAccount,
    Gun,
    MacAddress,
    Transport,
)
from maltego.entities.casefile import Weapon


def test_casefile_entities_are_available_from_standard_catalog():
    assert BankAccount.TYPE_NAME == "maltego.BankAccount"
    assert Gun.TYPE_NAME == "maltego.Gun"
    assert MacAddress.TYPE_NAME == "maltego.MacAddress"
    assert Transport.Config.category == "Transportation"
    assert Weapon.Config.category == "Weapons"


def test_legacy_casefile_side_package_is_not_shipped():
    assert importlib.util.find_spec("casefile_entities") is None
