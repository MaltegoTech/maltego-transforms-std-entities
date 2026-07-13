import inspect
from pathlib import Path

import maltego.entities as entities
import maltego.entities.casefile as casefile_entities
import maltego.icons as icons
from maltego.server import MaltegoIcon


ROOT = Path(__file__).resolve().parents[1]


def entity_classes(module):
    for name, value in inspect.getmembers(module, inspect.isclass):
        if hasattr(value, "TYPE_NAME"):
            yield name, value


def icon_classes(module):
    for _, value in inspect.getmembers(module, inspect.isclass):
        if issubclass(value, MaltegoIcon) and value is not MaltegoIcon:
            yield value


def test_casefile_entities_are_re_exported_without_duplicate_mac_address():
    assert entities.BankAccount is casefile_entities.BankAccount
    assert entities.IdentificationNumber is casefile_entities.IdentificationNumber
    assert casefile_entities.Businessman.TYPE_NAME == "maltego.Businessman"
    assert not hasattr(entities, "Business")
    assert not hasattr(casefile_entities, "Business")
    assert not hasattr(casefile_entities, "MacAddress")
    assert entities.MacAddress.TYPE_NAME == "maltego.MacAddress"


def test_catalog_type_names_are_unique():
    seen = {}
    duplicates = []

    for export_name, entity_class in entity_classes(entities):
        previous = seen.setdefault(entity_class.TYPE_NAME, export_name)
        if previous != export_name:
            duplicates.append((entity_class.TYPE_NAME, previous, export_name))

    assert duplicates == []


def test_casefile_type_names_do_not_overlap_standard_catalog():
    standard_type_names = {
        entity_class.TYPE_NAME
        for _, entity_class in entity_classes(entities)
        if entity_class.__module__ != casefile_entities.__name__
    }
    casefile_type_names = {
        entity_class.TYPE_NAME
        for _, entity_class in entity_classes(casefile_entities)
        if entity_class.__module__ == casefile_entities.__name__
    }

    assert "maltego.Person" in standard_type_names
    assert "maltego.Person" not in casefile_type_names
    assert casefile_type_names & standard_type_names == set()


def test_casefile_entities_define_explicit_config():
    missing_config = [
        export_name
        for export_name, entity_class in entity_classes(casefile_entities)
        if entity_class.__module__ == casefile_entities.__name__
        and "Config" not in entity_class.__dict__
    ]

    assert missing_config == []


def test_composite_entities_are_not_shipped_in_public_catalog():
    composite_type_names = {
        "maltego.OnlineService",
        "maltego.basic_profile",
        "maltego.channel_profile",
        "maltego.community_profile",
        "maltego.group_profile",
        "maltego.message",
        "maltego.public_message",
        "maltego.user_profile",
        "maltego.Video",
        "maltego.LongVideo",
        "maltego.ShortVideo",
        "maltego.Comment",
        "maltego.ontology.Event",
        "maltego.ontology.Message",
        "maltego.ontology.Profile",
    }

    exported_type_names = {
        entity_class.TYPE_NAME
        for _, entity_class in entity_classes(entities)
    }

    assert composite_type_names.isdisjoint(exported_type_names)


def test_icon_assets_exist_for_exported_icon_classes():
    missing = [
        icon_class.filename
        for icon_class in icon_classes(icons)
        if not Path(icon_class.filename).is_file()
    ]

    assert len(list(icon_classes(icons))) == 76
    assert missing == []
