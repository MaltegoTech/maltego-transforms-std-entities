# Copyright (c) Maltego Technologies GmbH.
from maltego.categories import EntityCategories
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity.property import MEF
from maltego.model.types import MATCHING_RULE_LOOSE
from maltego.model.types import MATCHING_RULE_STRICT

__all__ = [
    "Industry",
    "OnlineGroup",
    "Organization",
    "Company",
    "EducationInstitution",
    "Gang",
    "PoliticalMovement",
    "ReligiousGroup",
]


class Industry(MaltegoEntity):
    TYPE_NAME = "maltego.Industry"
    Config = MaltegoEntityConfig(
        value_property="name",
        display_name="Industry",
        description="A group of companies producing or providing similar goods and services.",
        display_property="name",
        category=EntityCategories.GROUPS.value,
        display_name_plural="Industries",
        icon_resource="General/PowerPlant",
        _visible=True,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="Name of the industry.",
        sample_value="Computer Programming Activities",
        matching_rule=MATCHING_RULE_STRICT,
    )
    nace2: str = MEF(
        name="nace2",
        display_name="NACE Rev. 2",
        description="Industry identifier following the NACE Revision 2 classification system.",
        sample_value="62.01",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    isic: str = MEF(
        name="isic",
        display_name="ISIC",
        description="Industry identifier following the International Standard Industrial Classification of All "
        "Economic Activities classification system.",
        sample_value="6201",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    naics: str = MEF(
        name="naics",
        display_name="NAICS",
        description="Industry identifier following the North American Industry Classification System.",
        sample_value="541511",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class OnlineGroup(MaltegoEntity):
    TYPE_NAME = "maltego.OnlineGroup"
    Config = MaltegoEntityConfig(
        value_property="title",
        display_name="Online Group",
        description="A socializing service on the Internet such as Facebook, an IRC channel or a mailing list",
        display_property="title",
        category=EntityCategories.GROUPS.value,
        display_name_plural="Online Groups",
        icon_resource="OnlineGroup",
    )
    title: str = MEF(
        name="title",
        display_name="Name",
        description="Name of the online group",
        sample_value="Facebook",
        matching_rule=MATCHING_RULE_STRICT,
    )
    url: str = MEF(
        name="url",
        display_name="URL",
        description="Web reference",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Organization(MaltegoEntity):
    TYPE_NAME = "maltego.Organization"
    Config = MaltegoEntityConfig(
        value_property="title",
        display_name="Organization",
        description="A social group which distributes tasks for a collective goal",
        display_property="title",
        category=EntityCategories.GROUPS.value,
        display_name_plural="Organizations",
        icon_resource="Organization",
        _visible=True,
    )
    title: str = MEF(
        name="title",
        display_name="Name",
        description="Name of the organization",
        sample_value="United Nations",
        matching_rule=MATCHING_RULE_STRICT,
    )


class Company(Organization):
    TYPE_NAME = "maltego.Company"
    Config = MaltegoEntityConfig(
        display_name="Company",
        description="A business organization",
        display_name_plural="Companies",
        icon_resource="Company",
    )
    title: str = MEF(
        name="title",
        display_name="Name",
        description="Name of the company",
        sample_value="Maltego Technologies GmbH",
        matching_rule=MATCHING_RULE_STRICT,
    )


class EducationInstitution(Organization):
    TYPE_NAME = "maltego.EducationInstitution"
    Config = MaltegoEntityConfig(
        display_name="Education Institution",
        description="An institution dedicated to education such as a school or university",
        display_name_plural="Education Institutions",
        icon_resource="School",
    )
    title: str = MEF(
        name="title",
        display_name="Name",
        description="Name of the educational institution",
        sample_value="LMU",
        matching_rule=MATCHING_RULE_STRICT,
    )


class Gang(Organization):
    TYPE_NAME = "maltego.Gang"
    Config = MaltegoEntityConfig(
        display_name="Gang",
        description="An organized group of criminals",
        display_name_plural="Gangs",
        icon_resource="Gang",
    )
    title: str = MEF(
        name="title",
        display_name="Name",
        description="Name of the gang",
        sample_value="Latin Kings",
        matching_rule=MATCHING_RULE_STRICT,
    )


class PoliticalMovement(Organization):
    TYPE_NAME = "maltego.PoliticalMovement"
    Config = MaltegoEntityConfig(
        display_name="Political Movement",
        description="A group of people working together to achieve a political goal",
        display_name_plural="Political Movements",
        icon_resource="PoliticalParty",
    )
    title: str = MEF(
        name="title",
        display_name="Name",
        description="Name of the organization",
        sample_value="Democrats",
        matching_rule=MATCHING_RULE_STRICT,
    )


class ReligiousGroup(Organization):
    TYPE_NAME = "maltego.ReligiousGroup"
    Config = MaltegoEntityConfig(
        display_name="Religious Group",
        description="A group of people who share religious or spiritual beliefs",
        display_name_plural="Religious Groups",
        icon_resource="Church",
    )
    title: str = MEF(
        name="title",
        display_name="Name",
        description="Name of the religious group",
        sample_value="Pastafarians",
        matching_rule=MATCHING_RULE_STRICT,
    )
