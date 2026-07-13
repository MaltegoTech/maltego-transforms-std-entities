# Copyright (c) Maltego Technologies GmbH.
from enum import Enum

__all__ = [
    "EntityCategories",
]


class EntityCategories(str, Enum):
    CRYPTOCURRENCY = "Cryptocurrency"
    DEVICES = "Devices"
    EVENTS = "Events"
    GROUPS = "Groups"
    INFRASTRUCTURE = "Infrastructure"
    LOCATION = "Locations"
    MALWARE = "Malware"
    PERSONAL = "Personal"
    SOCIAL_NETWORK = "Social Network"
    STIX2 = "STIX2"
    STIX2_DOMAIN_OBJECTS = "STIX 2 domain objects"
    STIX2_OBSERVABLES = "STIX 2 observables"
    STIX2_RELATIONSHIP_OBJECTS = "STIX 2 relationship objects"
    TECHNOLOGY = "Technology"
