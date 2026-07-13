# Copyright (c) Maltego Technologies GmbH.
from maltego.categories import EntityCategories
from maltego.entities.malware import Hash
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity import Overlay
from maltego.model.entity import OverlayPositions
from maltego.model.entity import OverlayTypes
from maltego.model.entity.property import MEF
from maltego.model.types import MATCHING_RULE_LOOSE

__all__ = [
    "ETag",
    "SSLCertificateHash",
    "SSLCertificateSerial",
]


class ETag(Hash):
    TYPE_NAME = "maltego.ETag"
    Config = MaltegoEntityConfig(
        display_name="ETag",
        description="HTTP ETag is an identifier for a specific version of a resource",
        display_name_plural="HTTP ETags",
        icon_resource="Technology/Tag",
        category=EntityCategories.TECHNOLOGY.value,
        overlays=[
            Overlay(OverlayTypes.TEXT, OverlayPositions.NORTH, "type"),
        ],
    )
    hash: str = MEF(
        name="properties.hash",
        display_name="Hash",
        sample_value="ce590e6f24aa1e8013891cd682acda84-ssl",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    type: str = MEF(
        name="type",
        display_name="Hash Type",
        readonly=True,
        sample_value="ETag",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class SSLCertificateHash(Hash):
    TYPE_NAME = "maltego.SSLCertificateHash"
    Config = MaltegoEntityConfig(
        display_name="SSL Certificate Hash",
        description="SSL Certificate Hash",
        display_name_plural="SSL Certificate Hashes",
        icon_resource="People/Hashtag",
        category=EntityCategories.TECHNOLOGY.value,
        overlays=[
            Overlay(OverlayTypes.TEXT, OverlayPositions.NORTH, "type"),
        ],
    )
    hash: str = MEF(
        name="properties.hash",
        display_name="Hash",
        sample_value="7a03fcad63521161e3ca44fade0487bd7a94014d",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    hash_type: str = MEF(
        name="hash_type",
        display_name="Hash Type",
        readonly=True,
        sample_value="SHA1",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class SSLCertificateSerial(Hash):
    TYPE_NAME = "maltego.SSLCertificateSerial"
    Config = MaltegoEntityConfig(
        display_name="SSL Certificate Serial",
        description="SSL Certificate Serial Number",
        display_name_plural="SSL Certificate Serials",
        icon_resource="People/Hashtag",
        category=EntityCategories.TECHNOLOGY.value,
        overlays=[
            Overlay(OverlayTypes.TEXT, OverlayPositions.NORTH, "type"),
        ],
    )
    hash: str = MEF(
        name="properties.hash",
        display_name="Hash",
        sample_value="369843066328785094512869461491419516338993",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    hash_type: str = MEF(
        name="hash_type",
        display_name="Hash Type",
        readonly=True,
        sample_value="Certificate Serial",
        matching_rule=MATCHING_RULE_LOOSE,
    )
