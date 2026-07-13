# Copyright (c) Maltego Technologies GmbH.
from maltego.model.entity import MEF, MaltegoEntity, MaltegoEntityConfig

from maltego.categories import EntityCategories

__all__ = [
    "Thing",
    "Item",
]


class Thing(MaltegoEntity):
    TYPE_NAME = "maltego.Thing"
    Config = MaltegoEntityConfig(
        display_name="Thing",
        display_name_plural="Things",
        category=EntityCategories.PERSONAL.value,
        description="Abstract root type of all things that we encounter in the cyber crime domain.",
        icon_resource="Assemble",
        allowed_root=False,
        display_property="thing_value",
        value_property="thing_value",
    )

    thing_value: str = MEF(hidden=True)


class Item(Thing):
    TYPE_NAME = "maltego.Item"
    Config = MaltegoEntityConfig(
        display_name="Item",
        display_name_plural="Items",
        description="A generic representation of a thing that is not a place, an event or an agent.",
        category=EntityCategories.PERSONAL.value,
        icon_resource="Assemble",
        allowed_root=False,
    )