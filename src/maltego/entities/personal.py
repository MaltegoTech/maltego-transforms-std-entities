# Copyright (c) Maltego Technologies GmbH.
from maltego.categories import EntityCategories
from maltego.entities.constants import REPLACE_EVALUATOR
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity import MaltegoEntityRegexConverter
from maltego.model.entity.property import MEF
from maltego.model.types import MATCHING_RULE_LOOSE, MATCHING_RULE_STRICT
from maltego.model.types import Url

__all__ = [
    "Identifier",
    "OnlineIdentifier",
    "InternalIdentifier",
    "Name",
    "Alias",
    "Document",
    "EmailAddress",
    "File",
    "Image",
    "Person",
    "PhoneNumber",
    "PhoneNumberMobile",
    "PhoneNumberOffice",
    "PhoneNumberResidential",
    "Phrase",
    "Sentiment",
    "Tag",
    "HashPassword",
    "PlaintextPassword",
]




class Identifier(MaltegoEntity):
    TYPE_NAME = "maltego.Identifier"
    Config = MaltegoEntityConfig(
        display_name="Identifier",
        display_name_plural="Identifiers",
        description="A general identifier used for distinguishing entities. "
                    "Note that instances of identifiers in isolation are in "
                    "general not to be treated as unique or "
                    "unambiguously distinguishing an associated entity.",
        category=EntityCategories.PERSONAL.value,
        icon_resource="AccessCard",
        display_property="is_partial",
        value_property="is_partial",
        allowed_root=False,
    )

    is_partial: bool = MEF(
        name="is_partial",
        display_name="Is Partial",
        matching_rule="loose",
    )


class OnlineIdentifier(Identifier):
    TYPE_NAME = "maltego.OnlineIdentifier"
    Config = MaltegoEntityConfig(
        display_name="Online Identifier",
        display_name_plural="Online Identifiers",
        description="An identifier used in an online context "
                    "to distinguish individuals or entities.",
        category=EntityCategories.PERSONAL.value,
        icon_resource="AccessCard",
        display_property="is_partial",
        value_property="is_partial",
        allowed_root=False,
    )


class InternalIdentifier(OnlineIdentifier):
    TYPE_NAME = "maltego.InternalIdentifier"
    Config = MaltegoEntityConfig(
        display_name="Internal Identifier",
        display_name_plural="Internal Identifiers",
        description="An identifier used within internal systems, typically not exposed to the public.",
        value_property="internal_identifier",
        display_property="internal_identifier",
        category=EntityCategories.PERSONAL.value,
        icon_resource="ID",
    )

    internal_identifier: str = MEF(
        name="internal_identifier",
        display_name="Internal Identifier",
        matching_rule="loose",
    )


class Name(OnlineIdentifier):
    TYPE_NAME = "maltego.Name"
    Config = MaltegoEntityConfig(
        display_name="Name",
        display_name_plural="Names",
        description="Previously known as Person. "
                    "An alternate name or pseudonym used by an entity. "
                    "This is an alias that the entity chose at its own discretion.",
        value_property="name",
        display_property="name",
        category=EntityCategories.PERSONAL.value,
        icon_resource="Field",
    )

    name: str = MEF(
        name="name",
        display_name="Name",
        matching_rule="loose",
    )


class Alias(OnlineIdentifier):
    TYPE_NAME = "maltego.Alias"
    Config = MaltegoEntityConfig(
        value_property="alias",
        display_name="Alias",
        description="An alias for a person",
        display_property="alias",
        category=EntityCategories.PERSONAL.value,
        display_name_plural="Aliases",
        icon_resource="Alias",
        _visible=True,
    )
    alias: str = MEF(
        name="alias",
        display_name="Alias",
        description="An Alias for a person",
        sample_value="maltegohq",
        matching_rule=MATCHING_RULE_STRICT,
    )


class Document(MaltegoEntity):
    TYPE_NAME = "maltego.Document"
    Config = MaltegoEntityConfig(
        value_property="url",
        display_name="Document",
        description="A document on the Internet",
        display_property="title",
        category=EntityCategories.PERSONAL.value,
        display_name_plural="Documents",
        icon_resource="InternetDocument",
        _visible=True,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        sample_value="Some Document",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    meta_data: str = MEF(
        name="document.meta-data",
        display_name="Meta-Data",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    url: Url = MEF(
        name="url",
        display_name="URL",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class EmailAddress(OnlineIdentifier):
    TYPE_NAME = "maltego.EmailAddress"
    Config = MaltegoEntityConfig(
        value_property="email",
        display_name="Email Address",
        description="An email mailbox to which email messages may be delivered",
        display_property="email",
        category=EntityCategories.PERSONAL.value,
        display_name_plural="Email Addresses",
        icon_resource="Email2",
        _visible=True,
        conversion_order=80,
        converter=MaltegoEntityRegexConverter(
            regex=r"(([ \t]*([a-zA-Z0-9\!\#\$\%\&\'\*\+\-\/\=\?\^\_\`\{\|\}\~]+(\.[a-zA-Z0-9\!\#\$\%\&\'\*\+\-\/\=\?\^\_\`\{\|\}\~]+)*)[ \t]*)|(\"([ \t]*([\x01-\x08\x0B\x0C\x0E-\x1F\x7F\x21\x23-\x5B\x5D-\x7E]|(\\[\x01-\x09\x0B\x0C\x0E-\x7F])))*[ \t]*\"))@[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,6}",  # pylint: disable=line-too-long
        ),
    )
    email: str = MEF(
        name="email",
        display_name="Email Address",
        sample_value="support@maltego.com",
        matching_rule=MATCHING_RULE_STRICT,
    )


class File(MaltegoEntity):
    TYPE_NAME = "maltego.File"
    Config = MaltegoEntityConfig(
        value_property="description",
        display_name="File",
        description="A file stored internally in the graph",
        display_property="description",
        category=EntityCategories.PERSONAL.value,
        allowed_root=False,
        display_name_plural="Files",
        icon_resource="File",
        _visible=True,
    )
    source: Url = MEF(
        name="source",
        display_name="Source",
        matching_rule=MATCHING_RULE_STRICT,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        sample_value="File",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Image(MaltegoEntity):
    TYPE_NAME = "maltego.Image"
    Config = MaltegoEntityConfig(
        value_property="description",
        display_name="Image",
        description="A visual representation of something",
        display_property="description",
        category=EntityCategories.PERSONAL.value,
        display_name_plural="Images",
        icon_resource="Image",
        conversion_order=85,
        overlay_image_property="url",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"(http[s]*://[-\w\.\:]*[^\s]*/([^\s]+\.(bmp|jpg|jpeg|png|gif|svg|webp))(\?[^\s]*)?)",
            groups=[
                "url",
                "description",
            ],
        ),
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        sample_value="Image",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    url: Url = MEF(
        name="url",
        display_name="URL",
    )

    base64: str = MEF(
        name="base64",
        display_name="Base64",
        description="Base64 encoded image data",
        matching_rule=MATCHING_RULE_STRICT,
    )


class Person(MaltegoEntity):
    TYPE_NAME = "maltego.Person"
    Config = MaltegoEntityConfig(
        value_property="person.fullname",
        display_name="Person",
        description="Entity representing a human",
        display_property="person.fullname",
        category=EntityCategories.PERSONAL.value,
        display_name_plural="People",
        icon_resource="Person",
        _visible=True,
        conversion_order=50,
        converter=MaltegoEntityRegexConverter(
            regex=r"(\p{Lu}{1,15}\p{Ll}{0,15}) (\p{Lu}{0,15}\p{Ll}{0,15} *\p{Lu}{0,15}\p{Ll}{0,15} *\p{Lu}{0,15}\p{Ll}{0,15})",  # pylint: disable=line-too-long
            groups=["person.firstnames", "person.lastname"],
        ),
    )
    fullname: str = MEF(
        name="person.fullname",
        display_name="Full Name",
        value="$trim($property(person.firstnames) $property(person.lastname))",
        matching_rule=MATCHING_RULE_LOOSE,
        evaluator=REPLACE_EVALUATOR,
    )
    firstnames: str = MEF(
        name="person.firstnames",
        display_name="First Names",
        sample_value="John",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lastname: str = MEF(
        name="person.lastname",
        display_name="Surname",
        sample_value="Doe",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class PhoneNumber(OnlineIdentifier):
    TYPE_NAME = "maltego.PhoneNumber"
    Config = MaltegoEntityConfig(
        value_property="phonenumber",
        display_name="Phone Number",
        description="A telephone number",
        display_property="phonenumber",
        category=EntityCategories.PERSONAL.value,
        display_name_plural="Phone Numbers",
        icon_resource="PhoneNumber",
        _visible=True,
        conversion_order=110,
        converter=MaltegoEntityRegexConverter(
            regex=r"(\+\d{1,3})??[\-\ ]??([\(]?\d{1,3}[\)]?)??[\-\ ]?(\d{3,4})[\-\ ]?(\d{3,4})$",
            groups=[
                "phonenumber.countrycode",
                "phonenumber.citycode",
                "phonenumber.areacode",
                "phonenumber.lastnumbers",
            ],
        ),
    )
    phonenumber: str = MEF(
        name="phonenumber",
        display_name="Phone Number",
        value="$trim($property(phonenumber.countrycode) $property(phonenumber.citycode) $property(phonenumber.areacode) $property(phonenumber.lastnumbers))",  # pylint: disable=line-too-long
        matching_rule=MATCHING_RULE_STRICT,
        evaluator=REPLACE_EVALUATOR,
    )
    countrycode: str = MEF(
        name="phonenumber.countrycode",
        display_name="Country Code",
        sample_value="+49",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    citycode: str = MEF(
        name="phonenumber.citycode",
        display_name="City Code",
        sample_value="89",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    areacode: str = MEF(
        name="phonenumber.areacode",
        display_name="Area Code",
        sample_value="2441849",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lastnumbers: str = MEF(
        name="phonenumber.lastnumbers",
        display_name="Last Digits",
        sample_value="0",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class PhoneNumberMobile(PhoneNumber):
    TYPE_NAME = "maltego.PhoneNumberMobile"
    Config = MaltegoEntityConfig(
        display_name="Phone Number (Mobile)",
        description="A phone number of a mobile phone",
        display_name_plural="Phone Numbers (Mobile)",
        icon_resource="MobilePhone2",
    )


class PhoneNumberOffice(PhoneNumber):
    TYPE_NAME = "maltego.PhoneNumberOffice"
    Config = MaltegoEntityConfig(
        display_name="Phone Number (Office)",
        description="A phone number for a place of work",
        display_name_plural="Phone Numbers (Office)",
        icon_resource="PhoneLandlineOffice",
    )


class PhoneNumberResidential(PhoneNumber):
    TYPE_NAME = "maltego.PhoneNumberResidential"
    Config = MaltegoEntityConfig(
        display_name="Phone Number (Residential)",
        description="A phone number for a place of residence",
        display_name_plural="Phone Numbers (Residential)",
        icon_resource="PhoneLandlineResidential",
    )


class Phrase(MaltegoEntity):
    TYPE_NAME = "maltego.Phrase"
    Config = MaltegoEntityConfig(
        value_property="text",
        display_name="Phrase",
        description="Any text or part thereof",
        display_property="text",
        category=EntityCategories.PERSONAL.value,
        display_name_plural="Phrases",
        conversion_order=10000,
        icon_resource="Phrase",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r".*",
        ),
    )
    text: str = MEF(
        name="text",
        display_name="Text",
        sample_value="Some phrase",
    )


class Sentiment(MaltegoEntity):
    TYPE_NAME = "maltego.Sentiment"
    Config = MaltegoEntityConfig(
        value_property="properties.sentiment",
        display_name="Sentiment",
        description="This represent the sentiment towards an entity.",
        display_property="properties.sentiment",
        category=EntityCategories.PERSONAL.value,
        display_name_plural="Sentiments",
        icon_resource="Smile",
        _visible=True,
    )
    sentiment: str = MEF(
        name="properties.sentiment",
        display_name="Sentiment",
        value=" ",
        sample_value="Positive",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Tag(Phrase):
    TYPE_NAME = "maltego.Tag"

    Config = MaltegoEntityConfig(
        value_property="text",
        display_property="text",
        category=EntityCategories.PERSONAL.value,
        display_name="Tag",
        display_name_plural="Tags",
        icon_resource="Tag",
        description="A label or metadata assigned to a specific item "
        "or concept to aid in categorization and organization.",
    )


class HashPassword(Phrase):
    TYPE_NAME = "maltego.HashPassword"
    Config = MaltegoEntityConfig(
        display_name="Hash Password",
        description="Hashed string of characters used to verify the identity "
        "of a user during the authentication process.",
        display_name_plural="Hash Passwords",
        icon_resource="Password",
        allowed_root=False,
    )
    text: str = MEF(
        name="text",
        display_name="Text",
        sample_value="***E99",
        matching_rule=MATCHING_RULE_STRICT,
    )
    encrypt_method: str = MEF(
        name="encrypt_method",
        display_name="Encryption Method",
        sample_value="md5",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class PlaintextPassword(Phrase):
    TYPE_NAME = "maltego.PlaintextPassword"
    Config = MaltegoEntityConfig(
        display_name="Plaintext Password",
        description="A string of characters in plaintext used to verify the "
        "identity of a user during the authentication process.",
        display_name_plural="Plaintext Passwords",
        icon_resource="Password",
        allowed_root=False,
    )
    text: str = MEF(
        name="text",
        display_name="Text",
        sample_value="123456",
        matching_rule=MATCHING_RULE_STRICT,
    )
