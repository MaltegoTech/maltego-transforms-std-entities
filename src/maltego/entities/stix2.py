# Copyright (c) Maltego Technologies GmbH.
# pylint: disable=line-too-long,too-many-lines
from typing import List

from maltego.categories import EntityCategories
from maltego.entities.events import ConversationEmail
from maltego.entities.events import Event
from maltego.entities.events import Incident
from maltego.entities.groups import Organization
from maltego.entities.infrastructure import AS
from maltego.entities.infrastructure import CVE
from maltego.entities.infrastructure import Domain
from maltego.entities.infrastructure import IPv4Address
from maltego.entities.infrastructure import IPv6Address
from maltego.entities.infrastructure import MacAddress
from maltego.entities.infrastructure import URL
from maltego.entities.infrastructure import X509Certificate
from maltego.entities.locations import Location
from maltego.entities.personal import Alias
from maltego.entities.personal import EmailAddress
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity import MaltegoEntityRegexConverter
from maltego.model.entity import Overlay
from maltego.model.entity import OverlayPositions
from maltego.model.entity import OverlayTypes
from maltego.model.entity.property import MEF
from maltego.model.types import MATCHING_RULE_LOOSE
from maltego.model.types import MATCHING_RULE_STRICT
from maltego.model.types import Url

__all__ = [
    "STIX2Core",
    "STIX2emailmessage",
    "STIX2vulnerability",
    "STIX2domainname",
    "STIX2emailaddr",
    "STIX2campaign",
    "STIX2incident",
    "STIX2ipv4addr",
    "STIX2ipv6addr",
    "STIX2location",
    "STIX2macaddr",
    "STIX2identity",
    "STIX2threatactor",
    "STIX2useraccount",
    "STIX2autonomoussystem",
    "STIX2artifact",
    "STIX2attackpattern",
    "STIX2courseofaction",
    "STIX2directory",
    "STIX2file",
    "STIX2grouping",
    "STIX2indicator",
    "STIX2infrastructure",
    "STIX2intrusionset",
    "STIX2malware",
    "STIX2malwareanalysis",
    "STIX2mutex",
    "STIX2networktraffic",
    "STIX2note",
    "STIX2observeddata",
    "STIX2opinion",
    "STIX2process",
    "STIX2relationship",
    "STIX2report",
    "STIX2sighting",
    "STIX2software",
    "STIX2tool",
    "STIX2windowsregistrykey",
    "STIX2url",
    "STIX2x509certificate",
]

X_MALTEGO_RECOVERY_PROPERTY_MAPPING_VALUE = '{"title": ["name"]}'
STIX2_LANGUAGE_PROPERTY_DESCRIPTION = (
    "Identifies the language of the text content in this object."
)
STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION = (
    "The set of granular markings that apply to this object."
)
STIX2_REVOKED_PROPERTY_DESCRIPTION = (
    "The revoked property indicates whether the object has been revoked."
)
STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION = (
    "The version of the STIX specification used to represent this object."
)
STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION = "The version of the STIX specification used to represent the content in this cyber-observable."
STIX2_DEFANGED_PROPERTY_DESCRIPTION = "Defines whether or not the data contained within the object has been defanged."
STIX2_EXTENSIONS_PROPERTY_DESCRIPTION = (
    "Specifies any extensions of the object, as a dictionary."
)
STIX2_LABELS_PROPERTY_DESCRIPTION = "The labels property specifies a set of terms used to describe this object."
STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION = (
    "The list of marking-definition objects to be applied to this object."
)
STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION = (
    "A list of external references which refers to non-STIX information."
)
STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION = (
    "The ID of the Source object that describes who created this object."
)
STIX2_CONFIDENCE_PROPERTY_DESCRIPTION = "Identifies the confidence that the creator has in the correctness of their data."
STIX2_MODIFIED_PROPERTY_DESCRIPTION = (
    "The modified property represents the time that this particular version of the object was modified. "
    "The timstamp value MUST be precise to the nearest millisecond."
)
STIX2_CREATED_PROPERTY_DESCRIPTION = (
    "The created property represents the time at which the first version of this object was created. "
    "The timstamp value MUST be precise to the nearest millisecond."
)
X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION = (
    "The mapping of Maltego internal property names "
    "to STIX property names used for this entity."
)


class STIX2Core(MaltegoEntity):
    TYPE_NAME = "maltego.STIX2.core"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Core",
        description="Abstract entity from which all STIX entities inherit common properties",
        display_property="id",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        allowed_root=False,
        display_name_plural="Core",
        # overlays=[EntityOverlay(property_name='x_maltego_marking_color', position='NW', type='colour'), EntityOverlay(property_name='x_maltego_marking_text', position='W', type='text')] TODO
        # overlay_image_property TODO
        icon_resource="stix_two_default_icon",
        _visible=True,
        overlays=[
            Overlay(
                OverlayTypes.TEXT,
                OverlayPositions.WEST,
                "x_maltego_marking_text",
            ),
            Overlay(
                OverlayTypes.COLOR,
                OverlayPositions.NORTHWEST,
                "x_maltego_marking_color",
            ),
        ],
    )

    id: str = MEF(
        name="id",
        display_name="Id",
        matching_rule=MATCHING_RULE_STRICT,
    )
    x_maltego_marking_color: str = MEF(
        name="x_maltego_marking_color",
        display_name="X_Maltego_Marking_Color",
        description="A color to be used in graphic display to show a marking sign (eg TLP)",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_marking_text: str = MEF(
        name="x_maltego_marking_text",
        display_name="X_Maltego_Marking_Text",
        description="A text to be used in graphic display to show a marking sign (eg TLP)",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2emailmessage(ConversationEmail, STIX2Core):
    TYPE_NAME = "maltego.STIX2.email-message"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Email Message",
        description="The Email Message Object represents an instance of an email message.",
        display_property="id",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Email Message",
        conversion_order=1,
        icon_resource="stix_two_email_msg",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(email-message--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `email-message`.",
        value="email-message",
        sample_value="email-message",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    email: str = MEF(
        name="email",
        display_name="Email",
        description="Specifies the value of the 'From:' header of the email message.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    recipients: List[str] = MEF(
        name="email.recipients",
        display_name="Email.Recipients",
        description="Specifies the mailboxes that are 'To:' recipients of the email message.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="Specifies the subject of the email message.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    date: str = MEF(
        name="date",
        display_name="Date",
        description="Specifies the date/time that the email message was sent.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    content_type: str = MEF(
        name="content_type",
        display_name="Content_Type",
        description="Specifies the value of the 'Content-Type' header of the email message.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    sender_ref: str = MEF(
        name="sender_ref",
        display_name="Sender_Ref",
        description="Specifies the value of the 'From' field of the email message.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    cc_refs: List[str] = MEF(
        name="cc_refs",
        display_name="Cc_Refs",
        description="Specifies the mailboxes that are 'CC:' recipients of the email message.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    bcc_refs: List[str] = MEF(
        name="bcc_refs",
        display_name="Bcc_Refs",
        description="Specifies the mailboxes that are 'BCC:' recipients of the email message.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    message_id: str = MEF(
        name="message_id",
        display_name="Message_Id",
        description="Specifies the Message-ID field of the email message.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    received_lines: List[str] = MEF(
        name="received_lines",
        display_name="Received_Lines",
        description="Specifies one or more Received header fields that may be included in the email headers.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    additional_header_fields: str = MEF(
        name="additional_header_fields",
        display_name="Additional_Header_Fields",
        description="Specifies any other header fields found in the email message, as a dictionary.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    raw_email_ref: str = MEF(
        name="raw_email_ref",
        display_name="Raw_Email_Ref",
        description="Specifies the raw binary contents of the email message, including both the headers and body, as a reference to an Artifact Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"email": ["from_ref"], "email.recipients": ["to_refs"], "title": ["subject"]}',
        sample_value='{"email": ["from_ref"], "email.recipients": ["to_refs"], "title": ["subject"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )
    is_multipart: str = MEF(
        name="is_multipart",
        display_name="Is_Multipart",
        readonly=True,
        description="Indicates whether the email body contains multiple MIME parts.",
        value="True",
        sample_value="True",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    body: str = MEF(
        name="body",
        display_name="Body",
        description="Specifies a string containing the email body. This field MAY only be used if is_multipart is false.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    body_multipart: List[str] = MEF(
        name="body_multipart",
        display_name="Body_Multipart",
        description="Specifies a list of the MIME parts that make up the email body. This property MAY only be used if is_multipart is true.",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2vulnerability(CVE, STIX2Core):
    TYPE_NAME = "maltego.STIX2.vulnerability"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Vulnerability",
        description="A Vulnerability is a mistake in software that can be directly used by a hacker to gain access to a system or network.",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Vulnerability",
        conversion_order=1,
        icon_resource="stix_two_vulnerability",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(vulnerability--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `vulnerability`.",
        value="vulnerability",
        sample_value="vulnerability",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    text: str = MEF(
        name="text",
        display_name="Text",
        description="The name used to identify the Vulnerability.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about the Vulnerability.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"text": ["name"]}',
        sample_value='{"text": ["name"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2domainname(Domain, STIX2Core):
    TYPE_NAME = "maltego.STIX2.domain-name"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Domain Name",
        description="The Domain Name represents the properties of a network domain name.",
        display_property="fqdn",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Domain Name",
        conversion_order=1,
        icon_resource="stix_two_domain_name",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(domain-name--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `domain-name`.",
        value="domain-name",
        sample_value="domain-name",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    fqdn: str = MEF(
        name="fqdn",
        display_name="Fqdn",
        description="Specifies the value of the domain name.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    resolves_to_refs: List[str] = MEF(
        name="resolves_to_refs",
        display_name="Resolves_To_Refs",
        description="Specifies a list of references to one or more IP addresses or domain names that the domain name resolves to.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"fqdn": ["value"]}',
        sample_value='{"fqdn": ["value"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2emailaddr(EmailAddress, STIX2Core):
    TYPE_NAME = "maltego.STIX2.email-addr"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Email Addr",
        description="The Email Address Object represents a single email address.",
        display_property="email",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Email Addr",
        conversion_order=1,
        icon_resource="stix_two_email_addr",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(email-addr--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `email-addr`.",
        value="email-addr",
        sample_value="email-addr",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    email: str = MEF(
        name="email",
        display_name="Email",
        description="Specifies a single email address. This MUST not include the display name.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    display_name: str = MEF(
        name="display_name",
        display_name="Display_Name",
        description="Specifies a single email display name, i.e., the name that is displayed to the human user of a mail application.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    belongs_to_ref: str = MEF(
        name="belongs_to_ref",
        display_name="Belongs_To_Ref",
        description="Specifies the user account that the email address belongs to, as a reference to a User Account Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"email": ["value"]}',
        sample_value='{"email": ["value"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2campaign(Event, STIX2Core):
    TYPE_NAME = "maltego.STIX2.campaign"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Campaign",
        description="A Campaign is a grouping of adversary behavior that describes a set of malicious activities or attacks that occur over a period of time against a specific set of targets.",
        display_property="title",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Campaign",
        conversion_order=1,
        icon_resource="stix_two_campaign",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(campaign--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `campaign`.",
        value="campaign",
        sample_value="campaign",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="The name used to identify the Campaign.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    starttime: str = MEF(  # type: ignore
        name="starttime",
        display_name="Starttime",
        description="The time that this Campaign was first seen.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    stoptime: str = MEF(  # type: ignore
        name="stoptime",
        display_name="Stoptime",
        description="The time that this Campaign was last seen.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about the Campaign, potentially including its purpose and its key characteristics.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    aliases: List[str] = MEF(
        name="aliases",
        display_name="Aliases",
        description="Alternative names used to identify this campaign.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    objective: str = MEF(
        name="objective",
        display_name="Objective",
        description="This field defines the Campaign’s primary goal, objective, desired outcome, or intended effect.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"title": ["name"], "starttime": ["first_seen"], "stoptime": ["last_seen"]}',
        sample_value='{"title": ["name"], "starttime": ["first_seen"], "stoptime": ["last_seen"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2incident(Incident, STIX2Core):
    TYPE_NAME = "maltego.STIX2.incident"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Incident",
        description="The Incident object in STIX 2.1 is a stub, to be expanded in future STIX 2 releases.",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Incident",
        conversion_order=1,
        icon_resource="stix_two_incident",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(incident--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `incident`.",
        value="incident",
        sample_value="incident",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="The name used to identify the Incident.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about the Incident.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_VALUE,
        sample_value=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_VALUE,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2ipv4addr(IPv4Address, STIX2Core):
    TYPE_NAME = "maltego.STIX2.ipv4-addr"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Ipv4 Addr",
        description="The IPv4 Address Object represents one or more IPv4 addresses expressed using CIDR notation.",
        display_property="ipv4-address",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Ipv4 Addr",
        conversion_order=1,
        icon_resource="stix_two_ipvfour_addr",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(ipv4-addr--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `ipv4-addr`.",
        value="ipv4-addr",
        sample_value="ipv4-addr",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    ipv4_address: str = MEF(
        name="ipv4-address",
        display_name="Ipv4-Address",
        description="Specifies one or more IPv4 addresses expressed using CIDR notation.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    resolves_to_refs: List[str] = MEF(
        name="resolves_to_refs",
        display_name="Resolves_To_Refs",
        description="Specifies a list of references to one or more Layer 2 Media Access Control (MAC) addresses that the IPv4 address resolves to.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    belongs_to_refs: List[str] = MEF(
        name="belongs_to_refs",
        display_name="Belongs_To_Refs",
        description="Specifies a reference to one or more autonomous systems (AS) that the IPv4 address belongs to.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"ipv4-address": ["value"]}',
        sample_value='{"ipv4-address": ["value"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2ipv6addr(IPv6Address, STIX2Core):
    TYPE_NAME = "maltego.STIX2.ipv6-addr"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Ipv6 Addr",
        description="The IPv6 Address Object represents one or more IPv6 addresses expressed using CIDR notation.",
        display_property="ipv6-address",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Ipv6 Addr",
        conversion_order=1,
        icon_resource="stix_two_ipvsix_addr",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(ipv6-addr--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `ipv6-addr`.",
        value="ipv6-addr",
        sample_value="ipv6-addr",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    ipv6_address: str = MEF(
        name="ipv6-address",
        display_name="Ipv6-Address",
        description="Specifies one or more IPv6 addresses expressed using CIDR notation.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    resolves_to_refs: List[str] = MEF(
        name="resolves_to_refs",
        display_name="Resolves_To_Refs",
        description="Specifies a list of references to one or more Layer 2 Media Access Control (MAC) addresses that the IPv6 address resolves to.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    belongs_to_refs: List[str] = MEF(
        name="belongs_to_refs",
        display_name="Belongs_To_Refs",
        description="Specifies a reference to one or more autonomous systems (AS) that the IPv6 address belongs to.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"ipv6-address": ["value"]}',
        sample_value='{"ipv6-address": ["value"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2location(Location, STIX2Core):
    TYPE_NAME = "maltego.STIX2.location"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Location",
        description="A Location represents a geographic location. The location may be described as any, some or all of the following: region (e.g., North America), civic address (e.g. New York, US), latitude and longitude.",
        display_property="location.name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Location",
        conversion_order=1,
        icon_resource="stix_two_location",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(location--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `location`.",
        value="location",
        sample_value="location",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="location.name",
        display_name="Location.Name",
        description="A name used to identify the Location.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    latitude: str = MEF(  # type: ignore
        name="latitude",
        display_name="Latitude",
        description="The latitude of the Location in decimal degrees.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    longitude: str = MEF(  # type: ignore
        name="longitude",
        display_name="Longitude",
        description="The longitude of the Location in decimal degrees.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        description="The country that this Location describes.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    area: str = MEF(
        name="location.area",
        display_name="Location.Area",
        description="The state, province, or other sub-national administrative area that this Location describes.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    city: str = MEF(
        name="city",
        display_name="City",
        description="The city that this Location describes.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    streetaddress: str = MEF(
        name="streetaddress",
        display_name="Streetaddress",
        description="The street address that this Location describes.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    areacode: str = MEF(
        name="location.areacode",
        display_name="Location.Areacode",
        description="The postal code for this Location.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A textual description of the Location.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    precision: str = MEF(
        name="precision",
        display_name="Precision",
        description="Defines the precision of the coordinates specified by the latitude and longitude properties, measured in meters.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    region: str = MEF(
        name="region",
        display_name="Region",
        description="The region that this Location describes.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"location.name": ["name"], "latitude": ["latitude"], "longitude": ["longitude"], "country": ["country"], "city": ["city"], "streetaddress": ["street_address"], "location.area": ["administrative_area"], "location.areacode": ["postal_code"]}',
        sample_value='{"location.name": ["name"], "latitude": ["latitude"], "longitude": ["longitude"], "country": ["country"], "city": ["city"], "streetaddress": ["street_address"], "location.area": ["administrative_area"], "location.areacode": ["postal_code"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2macaddr(MacAddress, STIX2Core):
    TYPE_NAME = "maltego.STIX2.mac-addr"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Mac Addr",
        description="The MAC Address Object represents a single Media Access Control (MAC) address.",
        display_property="macaddress",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Mac Addr",
        conversion_order=1,
        icon_resource="stix_two_mac_addr",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(mac-addr--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `mac-addr`.",
        value="mac-addr",
        sample_value="mac-addr",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    macaddress: str = MEF(
        name="macaddress",
        display_name="Macaddress",
        description="Specifies one or more mac addresses expressed using CIDR notation.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"macaddress": ["value"]}',
        sample_value='{"macaddress": ["value"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2identity(Organization, STIX2Core):
    TYPE_NAME = "maltego.STIX2.identity"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Identity",
        description="Identities can represent actual individuals, organizations, or groups (e.g., ACME, Inc.) as well as classes of individuals, organizations, or groups.",
        display_property="title",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Identity",
        conversion_order=1,
        icon_resource="stix_two_identity",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(identity--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `identity`.",
        value="identity",
        sample_value="identity",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="The name of this Identity.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    roles: List[str] = MEF(
        name="roles",
        display_name="Roles",
        description="The list of roles that this Identity performs (e.g., CEO, Domain Administrators, Doctors, Hospital, or Retailer). No open vocabulary is yet defined for this property.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about the Identity.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    identity_class: str = MEF(
        name="identity_class",
        display_name="Identity_Class",
        description="The type of entity that this Identity describes, e.g., an individual or organization. Open Vocab - identity-class-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    sectors: List[str] = MEF(
        name="sectors",
        display_name="Sectors",
        description="The list of sectors that this Identity belongs to. Open Vocab - industry-sector-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    contact_information: str = MEF(
        name="contact_information",
        display_name="Contact_Information",
        description="The contact information (e-mail, phone number, etc.) for this Identity.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_VALUE,
        sample_value=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_VALUE,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2threatactor(Organization, STIX2Core):
    TYPE_NAME = "maltego.STIX2.threat-actor"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Threat Actor",
        description="Threat Actors are actual individuals, groups, or organizations believed to be operating with malicious intent.",
        display_property="title",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Threat Actor",
        conversion_order=1,
        icon_resource="stix_two_threat_actor",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(threat-actor--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `threat-actor`.",
        value="threat-actor",
        sample_value="threat-actor",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="A name used to identify this Threat Actor or Threat Actor group.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    threat_actor_types: List[str] = MEF(
        name="threat_actor_types",
        display_name="Threat_Actor_Types",
        description="This field specifies the type of threat actor. Open Vocab - threat-actor-type-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about the Threat Actor.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    aliases: List[str] = MEF(
        name="aliases",
        display_name="Aliases",
        description="A list of other names that this Threat Actor is believed to use.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    roles: List[str] = MEF(
        name="roles",
        display_name="Roles",
        description="This is a list of roles the Threat Actor plays. Open Vocab - threat-actor-role-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    goals: List[str] = MEF(
        name="goals",
        display_name="Goals",
        description="The high level goals of this Threat Actor, namely, what are they trying to do.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    first_seen: str = MEF(
        name="first_seen",
        display_name="First_Seen",
        description="The time that this Threat Actor was first seen.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    last_seen: str = MEF(
        name="last_seen",
        display_name="Last_Seen",
        description="The time that this Threat Actor was last seen.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    sophistication: str = MEF(
        name="sophistication",
        display_name="Sophistication",
        description="The skill, specific knowledge, special training, or expertise a Threat Actor must have to perform the attack. Open Vocab - threat-actor-sophistication-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    resource_level: str = MEF(
        name="resource_level",
        display_name="Resource_Level",
        description="This defines the organizational level at which this Threat Actor typically works. Open Vocab - attack-resource-level-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    primary_motivation: str = MEF(
        name="primary_motivation",
        display_name="Primary_Motivation",
        description="The primary reason, motivation, or purpose behind this Threat Actor. Open Vocab - attack-motivation-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    secondary_motivations: List[str] = MEF(
        name="secondary_motivations",
        display_name="Secondary_Motivations",
        description="The secondary reasons, motivations, or purposes behind this Threat Actor. Open Vocab - attack-motivation-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    personal_motivations: List[str] = MEF(
        name="personal_motivations",
        display_name="Personal_Motivations",
        description="The personal reasons, motivations, or purposes of the Threat Actor regardless of organizational goals. Open Vocab - attack-motivation-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_VALUE,
        sample_value=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_VALUE,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2useraccount(Alias, STIX2Core):
    TYPE_NAME = "maltego.STIX2.user-account"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 User Account",
        description="The User Account Object represents an instance of any type of user account, including but not limited to operating system, device, messaging service, and social media platform accounts.",
        display_property="alias",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="User Account",
        conversion_order=1,
        icon_resource="stix_two_user_account",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(user-account--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `user-account`.",
        value="user-account",
        sample_value="user-account",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description="The User Account Object defines the following extensions. In addition to these, producers MAY create their own. Extensions: unix-account-ext.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    alias: str = MEF(
        name="alias",
        display_name="Alias",
        description="Specifies the identifier of the account.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    credential: str = MEF(
        name="credential",
        display_name="Credential",
        description="Specifies a cleartext credential. This is only intended to be used in capturing metadata from malware analysis (e.g., a hard-coded domain administrator password that the malware attempts to use for lateral movement) and SHOULD NOT be used for sharing of PII.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    account_login: str = MEF(
        name="account_login",
        display_name="Account_Login",
        description="Specifies the account login string, used in cases where the user_id property specifies something other than what a user would type when they login.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    account_type: str = MEF(
        name="account_type",
        display_name="Account_Type",
        description="Specifies the type of the account. This is an open vocabulary and values SHOULD come from the account-type-ov vocabulary.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    display_name: str = MEF(
        name="display_name",
        display_name="Display_Name",
        description="Specifies the display name of the account, to be shown in user interfaces, if applicable.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    is_service_account: str = MEF(
        name="is_service_account",
        display_name="Is_Service_Account",
        description="Indicates that the account is associated with a network service or system process (daemon), not a specific individual.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    is_privileged: str = MEF(
        name="is_privileged",
        display_name="Is_Privileged",
        description="Specifies that the account has elevated privileges (i.e., in the case of root on Unix or the Windows Administrator account).",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    can_escalate_privs: str = MEF(
        name="can_escalate_privs",
        display_name="Can_Escalate_Privs",
        description="Specifies that the account has the ability to escalate privileges (i.e., in the case of sudo on Unix or a Windows Domain Admin account).",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    is_disabled: str = MEF(
        name="is_disabled",
        display_name="Is_Disabled",
        description="Specifies if the account is disabled.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    account_created: str = MEF(
        name="account_created",
        display_name="Account_Created",
        description="Specifies when the account was created.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    account_expires: str = MEF(
        name="account_expires",
        display_name="Account_Expires",
        description="Specifies the expiration date of the account.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    credential_last_changed: str = MEF(
        name="credential_last_changed",
        display_name="Credential_Last_Changed",
        description="Specifies when the account credential was last changed.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    account_first_login: str = MEF(
        name="account_first_login",
        display_name="Account_First_Login",
        description="Specifies when the account was first accessed.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    account_last_login: str = MEF(
        name="account_last_login",
        display_name="Account_Last_Login",
        description="Specifies when the account was last accessed.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"alias": ["user_id"]}',
        sample_value='{"alias": ["user_id"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2autonomoussystem(AS, STIX2Core):
    TYPE_NAME = "maltego.STIX2.autonomous-system"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Autonomous System",
        description="The AS object represents the properties of an Autonomous Systems (AS).",
        display_property="as.number",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Autonomous System",
        conversion_order=1,
        icon_resource="stix_two_autonomous_system",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(autonomous-system--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `autonomous-system`.",
        value="autonomous-system",
        sample_value="autonomous-system",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    number: str = MEF(
        name="as.number",
        display_name="As.Number",
        description="Specifies the number assigned to the AS. Such assignments are typically performed by a Regional Internet Registries (RIR).",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="Specifies the name of the AS.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    rir: str = MEF(
        name="rir",
        display_name="Rir",
        description="Specifies the name of the Regional Internet Registry (RIR) that assigned the number to the AS.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"as.number": ["number"]}',
        sample_value='{"as.number": ["number"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2artifact(STIX2Core):
    TYPE_NAME = "maltego.STIX2.artifact"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Artifact",
        description="The Artifact Object permits capturing an array of bytes (8-bits), as a base64-encoded string string, or linking to a file-like payload.",
        display_property="id",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Artifact",
        icon_resource="stix_two_default_icon",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(artifact--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        readonly=True,
        description="The value of this property MUST be `artifact`.",
        value="artifact",
        sample_value="artifact",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    mime_type: str = MEF(
        name="mime_type",
        display_name="Mime_Type",
        description="The value of this property MUST be a valid MIME type as specified in the IANA Media Types registry.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    payload_bin: str = MEF(
        name="payload_bin",
        display_name="Payload_Bin",
        description="Specifies the binary data contained in the artifact as a base64-encoded string.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    url: str = MEF(
        name="url",
        display_name="Url",
        description="The value of this property MUST be a valid URL that resolves to the unencoded content.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    hashes: str = MEF(
        name="hashes",
        display_name="Hashes",
        description="Specifies a dictionary of hashes for the contents of the url or the payload_bin.  This MUST be provided when the url property is present.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    encryption_algorithm: str = MEF(
        name="encryption_algorithm",
        display_name="Encryption_Algorithm",
        description="If the artifact is encrypted, specifies the type of encryption algorithm the binary data  (either via payload_bin or url) is encoded in.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    decryption_key: str = MEF(
        name="decryption_key",
        display_name="Decryption_Key",
        description="Specifies the decryption key for the encrypted binary data (either via payload_bin or url).",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2attackpattern(STIX2Core):
    TYPE_NAME = "maltego.STIX2.attack-pattern"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Attack Pattern",
        description="Attack Patterns are a type of TTP that describe ways that adversaries attempt to compromise targets.",
        display_property="name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Attack Pattern",
        icon_resource="stix_two_attack_pattern",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(attack-pattern--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `attack-pattern`.",
        value="attack-pattern",
        sample_value="attack-pattern",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    aliases: List[str] = MEF(
        name="aliases",
        display_name="Aliases",
        description="Alternative names used to identify this Attack Pattern.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="The name used to identify the Attack Pattern.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about the Attack Pattern, potentially including its purpose and its key characteristics.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    kill_chain_phases: List[str] = MEF(
        name="kill_chain_phases",
        display_name="Kill_Chain_Phases",
        description="The list of kill chain phases for which this attack pattern is used.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2courseofaction(STIX2Core):
    TYPE_NAME = "maltego.STIX2.course-of-action"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Course Of Action",
        description="A Course of Action is an action taken either to prevent an attack or to respond to an attack that is in progress.",
        display_property="name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Course Of Action",
        icon_resource="stix_two_course_of_action",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(course-of-action--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `course-of-action`.",
        value="course-of-action",
        sample_value="course-of-action",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="The name used to identify the Course of Action.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about this object, potentially including its purpose and its key characteristics.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2directory(STIX2Core):
    TYPE_NAME = "maltego.STIX2.directory"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Directory",
        description="The Directory Object represents the properties common to a file system directory.",
        display_property="id",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Directory",
        icon_resource="stix_two_default_icon",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(directory--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `directory`.",
        value="directory",
        sample_value="directory",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    path: str = MEF(
        name="path",
        display_name="Path",
        description="Specifies the path, as originally observed, to the directory on the file system.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    path_enc: str = MEF(
        name="path_enc",
        display_name="Path_Enc",
        description="Specifies the observed encoding for the path.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    ctime: str = MEF(
        name="ctime",
        display_name="Ctime",
        description="Specifies the date/time the directory was created.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    mtime: str = MEF(
        name="mtime",
        display_name="Mtime",
        description="Specifies the date/time the directory was last written to/modified.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    atime: str = MEF(
        name="atime",
        display_name="Atime",
        description="Specifies the date/time the directory was last accessed.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    contains_refs: List[str] = MEF(
        name="contains_refs",
        display_name="Contains_Refs",
        description="Specifies a list of references to other File and/or Directory Objects contained within the directory.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2file(STIX2Core):
    TYPE_NAME = "maltego.STIX2.file"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 File",
        description="The File Object represents the properties of a file.",
        display_property="name",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="File",
        icon_resource="stix_two_default_icon",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(file--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `file`.",
        value="file",
        sample_value="file",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description="The File Object defines the following extensions. In addition to these, producers MAY create their own. Extensions: ntfs-ext, raster-image-ext, pdf-ext, archive-ext, windows-pebinary-ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    hashes: str = MEF(
        name="hashes",
        display_name="Hashes",
        description="Specifies a dictionary of hashes for the file.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    size: str = MEF(
        name="size",
        display_name="Size",
        description="Specifies the size of the file, in bytes, as a non-negative integer.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="Specifies the name of the file.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name_enc: str = MEF(
        name="name_enc",
        display_name="Name_Enc",
        description="Specifies the observed encoding for the name of the file.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    magic_number_hex: str = MEF(
        name="magic_number_hex",
        display_name="Magic_Number_Hex",
        description="Specifies the hexadecimal constant ('magic number') associated with a specific file format that corresponds to the file, if applicable.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    mime_type: str = MEF(
        name="mime_type",
        display_name="Mime_Type",
        description="Specifies the MIME type name specified for the file, e.g., 'application/msword'.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    ctime: str = MEF(
        name="ctime",
        display_name="Ctime",
        description="Specifies the date/time the file was created.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    mtime: str = MEF(
        name="mtime",
        display_name="Mtime",
        description="Specifies the date/time the file was last written to/modified.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    atime: str = MEF(
        name="atime",
        display_name="Atime",
        description="Specifies the date/time the file was last accessed.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    parent_directory_ref: str = MEF(
        name="parent_directory_ref",
        display_name="Parent_Directory_Ref",
        description="Specifies the parent directory of the file, as a reference to a Directory Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    contains_refs: List[str] = MEF(
        name="contains_refs",
        display_name="Contains_Refs",
        description="Specifies a list of references to other Observable Objects contained within the file.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    content_ref: str = MEF(
        name="content_ref",
        display_name="Content_Ref",
        description="Specifies the content of the file, represented as an Artifact Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2grouping(STIX2Core):
    TYPE_NAME = "maltego.STIX2.grouping"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_property="name",
        display_name="STIX2 Grouping",
        description="A Grouping object explicitly asserts that the referenced STIX Objects have a shared content.",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Grouping",
        icon_resource="stix_two_grouping",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(grouping--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `grouping`.",
        value="grouping",
        sample_value="grouping",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="A name used to identify the Grouping.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description which provides more details and context about the Grouping, potentially including the purpose and key characteristics.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    context: str = MEF(
        name="context",
        display_name="Context",
        description="A short description of the particular context shared by the content referenced by the Grouping.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_refs: List[str] = MEF(
        name="object_refs",
        display_name="Object_Refs",
        description="The STIX Objects (SDOs and SROs) that  are referred to by this Grouping.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2indicator(STIX2Core):
    TYPE_NAME = "maltego.STIX2.indicator"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Indicator",
        description="Indicators contain a pattern that can be used to detect suspicious or malicious cyber activity.",
        display_property="name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Indicator",
        icon_resource="stix_two_indicator",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(indicator--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `indicator`.",
        value="indicator",
        sample_value="indicator",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    indicator_types: List[str] = MEF(
        name="indicator_types",
        display_name="Indicator_Types",
        description="This field is an Open Vocabulary that specifies the type of indicator. Open vocab - indicator-type-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="The name used to identify the Indicator.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides the recipient with context about this Indicator potentially including its purpose and its key characteristics.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    pattern: str = MEF(
        name="pattern",
        display_name="Pattern",
        description="The detection pattern for this indicator.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    pattern_type: str = MEF(
        name="pattern_type",
        display_name="Pattern_Type",
        description="The type of pattern used in this indicator.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    pattern_version: str = MEF(
        name="pattern_version",
        display_name="Pattern_Version",
        description="The version of the pattern that is used.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    valid_from: str = MEF(
        name="valid_from",
        display_name="Valid_From",
        description="The time from which this indicator should be considered valuable intelligence.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    valid_until: str = MEF(
        name="valid_until",
        display_name="Valid_Until",
        description="The time at which this indicator should no longer be considered valuable intelligence.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    kill_chain_phases: List[str] = MEF(
        name="kill_chain_phases",
        display_name="Kill_Chain_Phases",
        description="The phases of the kill chain that this indicator detects.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2infrastructure(STIX2Core):
    TYPE_NAME = "maltego.STIX2.infrastructure"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Infrastructure",
        description="Infrastructure objects describe systems, software services, and associated physical or virtual resources.",
        display_property="name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Infrastructure",
        icon_resource="stix_two_infrastructure",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(infrastructure--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `infrastructure`.",
        value="infrastructure",
        sample_value="infrastructure",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="The name used to identify the Infrastructure.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about this Infrastructure potentially including its purpose and its key characteristics.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    infrastructure_types: List[str] = MEF(
        name="infrastructure_types",
        display_name="Infrastructure_Types",
        description="This field is an Open Vocabulary that specifies the type of infrastructure. Open vocab - infrastructure-type-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    aliases: List[str] = MEF(
        name="aliases",
        display_name="Aliases",
        description="Alternative names used to identify this Infrastructure.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    kill_chain_phases: List[str] = MEF(
        name="kill_chain_phases",
        display_name="Kill_Chain_Phases",
        description="The list of kill chain phases for which this infrastructure is used.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    first_seen: str = MEF(
        name="first_seen",
        display_name="First_Seen",
        description="The time that this infrastructure was first seen performing malicious activities.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    last_seen: str = MEF(
        name="last_seen",
        display_name="Last_Seen",
        description="The time that this infrastructure was last seen performing malicious activities.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2intrusionset(STIX2Core):
    TYPE_NAME = "maltego.STIX2.intrusion-set"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Intrusion Set",
        description="An Intrusion Set is a grouped set of adversary behavior and resources with common properties that is believed to be orchestrated by a single organization.",
        display_property="name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Intrusion Set",
        icon_resource="stix_two_intrusion_set",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(intrusion-set--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `intrusion-set`.",
        value="intrusion-set",
        sample_value="intrusion-set",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="The name used to identify the Intrusion Set.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="Provides more context and details about the Intrusion Set object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    aliases: List[str] = MEF(
        name="aliases",
        display_name="Aliases",
        description="Alternative names used to identify this Intrusion Set.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    first_seen: str = MEF(
        name="first_seen",
        display_name="First_Seen",
        description="The time that this Intrusion Set was first seen.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    last_seen: str = MEF(
        name="last_seen",
        display_name="Last_Seen",
        description="The time that this Intrusion Set was last seen.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    roles: List[str] = MEF(
        name="goals",
        display_name="Goals",
        description="The high level goals of this Intrusion Set, namely, what are they trying to do.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    resource_level: str = MEF(
        name="resource_level",
        display_name="Resource_Level",
        description="This defines the organizational level at which this Intrusion Set typically works. Open Vocab - attack-resource-level-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    primary_motivation: str = MEF(
        name="primary_motivation",
        display_name="Primary_Motivation",
        description="The primary reason, motivation, or purpose behind this Intrusion Set. Open Vocab - attack-motivation-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    secondary_motivations: List[str] = MEF(
        name="secondary_motivations",
        display_name="Secondary_Motivations",
        description="The secondary reasons, motivations, or purposes behind this Intrusion Set. Open Vocab - attack-motivation-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2malware(STIX2Core):
    TYPE_NAME = "maltego.STIX2.malware"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Malware",
        description="Malware is a type of TTP that is also known as malicious code and malicious software, refers to a program that is inserted into a system, usually covertly, with the intent of compromising the confidentiality, integrity, or availability of the victim's data, applications, or operating system (OS) or of otherwise annoying or disrupting the victim.",
        display_property="name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Malware",
        icon_resource="stix_two_malware",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(malware--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `malware`.",
        value="malware",
        sample_value="malware",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    aliases: List[str] = MEF(
        name="aliases",
        display_name="Aliases",
        description="Alternative names used to identify this Malware or Malware family.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    first_seen: str = MEF(
        name="first_seen",
        display_name="First_Seen",
        description="The time that the malware instance or family was first seen.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    last_seen: str = MEF(
        name="last_seen",
        display_name="Last_Seen",
        description="The time that the malware family or malware instance was last seen.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    operating_system_refs: List[str] = MEF(
        name="operating_system_refs",
        display_name="Operating_System_Refs",
        description="The operating systems that the malware family or malware instance is executable on.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    architecture_execution_envs: List[str] = MEF(
        name="architecture_execution_envs",
        display_name="Architecture_Execution_Envs",
        description="The processor architectures (e.g., x86, ARM, etc.) that the malware instance or family is executable on. Open Vocab - processor-architecture-os.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    implementation_languages: List[str] = MEF(
        name="implementation_languages",
        display_name="Implementation_Languages",
        description="The programming language(s) used to implement the malware instance or family. Open Vocab - implementation-language-ov.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    capabilities: List[str] = MEF(
        name="capabilities",
        display_name="Capabilities",
        description="Specifies any capabilities identified for the malware instance or family. Open Vocab - malware-capabilities-ov.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    sample_refs: List[str] = MEF(
        name="sample_refs",
        display_name="Sample_Refs",
        description="The sample_refs property specifies a list of identifiers of the SCO file or artifact objects associated with this malware instance(s) or family.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    malware_types: List[str] = MEF(
        name="malware_types",
        display_name="Malware_Types",
        description="The type of malware being described. Open Vocab - malware-type-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="The name used to identify the Malware.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="Provides more context and details about the Malware object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    kill_chain_phases: List[str] = MEF(
        name="kill_chain_phases",
        display_name="Kill_Chain_Phases",
        description="The list of kill chain phases for which this Malware instance can be used.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    is_family: str = MEF(
        name="is_family",
        display_name="Is_Family",
        readonly=True,
        description="Whether the object represents a malware family (if true) or a malware instance (if false).",
        value="True",
        sample_value="True",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2malwareanalysis(STIX2Core):
    TYPE_NAME = "maltego.STIX2.malware-analysis"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Malware Analysis",
        description="Malware Analysis captures the metadata and results of a particular analysis performed (static or dynamic) on the malware instance or family.",
        display_property="id",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Malware Analysis",
        icon_resource="stix_two_malware_analysis",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(malware-analysis--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `malware-analysis`.",
        value="malware-analysis",
        sample_value="malware-analysis",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    product: str = MEF(
        name="product",
        display_name="Product",
        description="The name of the analysis engine or product that was used for this analysis.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    version: str = MEF(
        name="version",
        display_name="Version",
        description="The version of the analysis product that was used to perform this analysis.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    configuration_version: str = MEF(
        name="configuration_version",
        display_name="Configuration_Version",
        description="The version of the analysis product configuration that was used to perform this analysis.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modules: List[str] = MEF(
        name="modules",
        display_name="Modules",
        description="The particular analysis product modules that were used to perform the analysis.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    analysis_engine_version: str = MEF(
        name="analysis_engine_version",
        display_name="Analysis_Engine_Version",
        description="The version of the analysis engine or product that was used to perform this analysis.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    analysis_definition_version: str = MEF(
        name="analysis_definition_version",
        display_name="Analysis_Definition_Version",
        description="The version of the analysis definitions used by the analysis tool.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    submitted: str = MEF(
        name="submitted",
        display_name="Submitted",
        description="The date and time that this malware was first submitted for scanning or analysis.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    analysis_started: str = MEF(
        name="analysis_started",
        display_name="Analysis_Started",
        description="The date and time that the malware analysis was initiated.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    analysis_ended: str = MEF(
        name="analysis_ended",
        display_name="Analysis_Ended",
        description="The date and time that the malware analysis ended.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    result_name: str = MEF(
        name="result_name",
        display_name="Result_Name",
        description="The classification result or name assigned to the malware instance by the scanner tool.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    result: str = MEF(
        name="result",
        display_name="Result",
        description="The classification result as determined by the scanner or tool analysis process.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    host_vm_ref: str = MEF(
        name="host_vm_ref",
        display_name="Host_Vm_Ref",
        description="A description of the virtual machine environment used to host the guest operating system (if applicable) that was used for the dynamic analysis of the malware instance or family.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    operating_system_ref: str = MEF(
        name="operating_system_ref",
        display_name="Operating_System_Ref",
        description="The operating system that was used to perform the dynamic analysis.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    installed_software_refs: List[str] = MEF(
        name="installed_software_refs",
        display_name="Installed_Software_Refs",
        description="Any non-standard software installed on the operating system used for the dynamic analysis of the malware instance or family.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    analysis_sco_refs: List[str] = MEF(
        name="analysis_sco_refs",
        display_name="Analysis_Sco_Refs",
        description="The list of STIX objects that were captured during the analysis process.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    sample_ref: str = MEF(
        name="sample_ref",
        display_name="Sample_Ref",
        description="Refers to the object this analysis was performed against.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2mutex(STIX2Core):
    TYPE_NAME = "maltego.STIX2.mutex"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Mutex",
        description="The Mutex Object represents the properties of a mutual exclusion (mutex) object.",
        display_property="name",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Mutex",
        icon_resource="stix_two_default_icon",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(mutex--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `mutex`.",
        value="mutex",
        sample_value="mutex",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="Specifies the name of the mutex object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2networktraffic(STIX2Core):
    TYPE_NAME = "maltego.STIX2.network-traffic"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Network Traffic",
        description="The Network Traffic Object represents arbitrary network traffic that originates from a source and is addressed to a destination.",
        display_property="id",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Network Traffic",
        icon_resource="stix_two_network_traffic",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(network-traffic--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `network-traffic`.",
        value="network-traffic",
        sample_value="network-traffic",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description="The Network Traffic Object defines the following extensions. In addition to these, producers MAY create their own. Extensions: http-ext, tcp-ext, icmp-ext, socket-ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    start: str = MEF(
        name="start",
        display_name="Start",
        description="Specifies the date/time the network traffic was initiated, if known.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    end: str = MEF(
        name="end",
        display_name="End",
        description="Specifies the date/time the network traffic ended, if known.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    src_ref: str = MEF(
        name="src_ref",
        display_name="Src_Ref",
        description="Specifies the source of the network traffic, as a reference to an Observable Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    dst_ref: str = MEF(
        name="dst_ref",
        display_name="Dst_Ref",
        description="Specifies the destination of the network traffic, as a reference to an Observable Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    src_port: str = MEF(
        name="src_port",
        display_name="Src_Port",
        description="Specifies the source port used in the network traffic, as an integer. The port value MUST be in the range of 0 - 65535.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    dst_port: str = MEF(
        name="dst_port",
        display_name="Dst_Port",
        description="Specifies the destination port used in the network traffic, as an integer. The port value MUST be in the range of 0 - 65535.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    protocols: List[str] = MEF(
        name="protocols",
        display_name="Protocols",
        description="Specifies the protocols observed in the network traffic, along with their corresponding state.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    src_byte_count: str = MEF(
        name="src_byte_count",
        display_name="Src_Byte_Count",
        description="Specifies the number of bytes sent from the source to the destination.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    dst_byte_count: str = MEF(
        name="dst_byte_count",
        display_name="Dst_Byte_Count",
        description="Specifies the number of bytes sent from the destination to the source.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    src_packets: str = MEF(
        name="src_packets",
        display_name="Src_Packets",
        description="Specifies the number of packets sent from the source to the destination.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    dst_packets: str = MEF(
        name="dst_packets",
        display_name="Dst_Packets",
        description="Specifies the number of packets sent destination to the source.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    ipfix: str = MEF(
        name="ipfix",
        display_name="Ipfix",
        description="Specifies any IP Flow Information Export (IPFIX) data for the traffic.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    src_payload_ref: str = MEF(
        name="src_payload_ref",
        display_name="Src_Payload_Ref",
        description="Specifies the bytes sent from the source to the destination.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    dst_payload_ref: str = MEF(
        name="dst_payload_ref",
        display_name="Dst_Payload_Ref",
        description="Specifies the bytes sent from the source to the destination.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    encapsulates_refs: List[str] = MEF(
        name="encapsulates_refs",
        display_name="Encapsulates_Refs",
        description="Links to other network-traffic objects encapsulated by a network-traffic.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    encapsulated_by_ref: str = MEF(
        name="encapsulated_by_ref",
        display_name="Encapsulated_By_Ref",
        description="Links to another network-traffic object which encapsulates this object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    is_active: str = MEF(
        name="is_active",
        display_name="Is_Active",
        readonly=True,
        description="Indicates whether the network traffic is still ongoing.",
        value="True",
        sample_value="True",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2note(STIX2Core):
    TYPE_NAME = "maltego.STIX2.note"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Note",
        description="A Note is a comment or note containing informative text to help explain the context of one or more STIX Objects (SDOs or SROs) or to provide additional analysis that is not contained in the original object.",
        display_property="id",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Note",
        icon_resource="stix_two_note",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(note--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `note`.",
        value="note",
        sample_value="note",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    abstract: str = MEF(
        name="abstract",
        display_name="Abstract",
        description="A brief summary of the note.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    content: str = MEF(
        name="content",
        display_name="Content",
        description="The content of the note.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    authors: List[str] = MEF(
        name="authors",
        display_name="Authors",
        description="The name of the author(s) of this note (e.g., the analyst(s) that created it).",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_refs: List[str] = MEF(
        name="object_refs",
        display_name="Object_Refs",
        description="The STIX Objects (SDOs and SROs) that the note is being applied to.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2observeddata(STIX2Core):
    TYPE_NAME = "maltego.STIX2.observed-data"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Observed Data",
        description="Observed data conveys information that was observed on systems and networks, such as log data or network traffic, using the Cyber Observable specification.",
        display_property="id",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Observed Data",
        icon_resource="stix_two_observed_data",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(observed-data--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `observed-data`.",
        value="observed-data",
        sample_value="observed-data",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    first_observed: str = MEF(
        name="first_observed",
        display_name="First_Observed",
        description="The beginning of the time window that the data was observed during.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    last_observed: str = MEF(
        name="last_observed",
        display_name="Last_Observed",
        description="The end of the time window that the data was observed during.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    number_observed: str = MEF(
        name="number_observed",
        display_name="Number_Observed",
        description="The number of times the data represented in the objects property was observed. This MUST be an integer between 1 and 999,999,999 inclusive.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    objects: str = MEF(
        name="objects",
        display_name="Objects",
        description="A dictionary of Cyber Observable Objects that describes the single 'fact' that was observed.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_refs: List[str] = MEF(
        name="object_refs",
        display_name="Object_Refs",
        description="A list of SCOs and SROs representing the observation.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2opinion(STIX2Core):
    TYPE_NAME = "maltego.STIX2.opinion"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Opinion",
        description="An Opinion is an assessment of the correctness of the information in a STIX Object produced by a different entity and captures the level of agreement or disagreement using a fixed scale.",
        display_property="opinion",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Opinion",
        conversion_order=1,
        icon_resource="stix_two_opinion",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(opinion--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `opinion`.",
        value="opinion",
        sample_value="opinion",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    explanation: str = MEF(
        name="explanation",
        display_name="Explanation",
        description="An explanation of why the producer has this Opinion.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    authors: List[str] = MEF(
        name="authors",
        display_name="Authors",
        description="The name of the author(s) of this opinion (e.g., the analyst(s) that created it).",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_refs: List[str] = MEF(
        name="object_refs",
        display_name="Object_Refs",
        description="The STIX Objects (SDOs and SROs) that the opinion is being applied to.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    opinion: str = MEF(
        name="opinion",
        display_name="Opinion",
        description="The opinion that the producer has about about all of the STIX Object(s) listed in the object_refs property.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2process(STIX2Core):
    TYPE_NAME = "maltego.STIX2.process"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Process",
        description="The Process Object represents common properties of an instance of a computer program as executed on an operating system.",
        display_property="id",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Process",
        icon_resource="stix_two_default_icon",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(process--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `process`.",
        value="process",
        sample_value="process",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description="The Process Object defines the following extensions. In addition to these, producers MAY create their own. Extensions: windows-process-ext, windows-service-ext.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    is_hidden: str = MEF(
        name="is_hidden",
        display_name="Is_Hidden",
        description="Specifies whether the process is hidden.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    pid: str = MEF(
        name="pid",
        display_name="Pid",
        description="Specifies the Process ID, or PID, of the process.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_time: str = MEF(
        name="created_time",
        display_name="Created_Time",
        description="Specifies the date/time at which the process was created.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    cwd: str = MEF(
        name="cwd",
        display_name="Cwd",
        description="Specifies the current working directory of the process.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    command_line: str = MEF(
        name="command_line",
        display_name="Command_Line",
        description="Specifies the full command line used in executing the process, including the process name (which may be specified individually via the binary_ref.name property) and any arguments.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    environment_variables: str = MEF(
        name="environment_variables",
        display_name="Environment_Variables",
        description="Specifies the list of environment variables associated with the process as a dictionary.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    opened_connection_refs: List[str] = MEF(
        name="opened_connection_refs",
        display_name="Opened_Connection_Refs",
        description="Specifies the list of network connections opened by the process, as a reference to one or more Network Traffic Objects.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    creator_user_ref: str = MEF(
        name="creator_user_ref",
        display_name="Creator_User_Ref",
        description="Specifies the user that created the process, as a reference to a User Account Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    image_ref: str = MEF(
        name="image_ref",
        display_name="Image_Ref",
        description="Specifies the executable binary that was executed as the process image, as a reference to a File Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    parent_ref: str = MEF(
        name="parent_ref",
        display_name="Parent_Ref",
        description="Specifies the other process that spawned (i.e. is the parent of) this one, as represented by a Process Object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    child_refs: List[str] = MEF(
        name="child_refs",
        display_name="Child_Refs",
        description="Specifies the other processes that were spawned by (i.e. children of) this process, as a reference to one or more other Process Objects.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2relationship(STIX2Core):
    TYPE_NAME = "maltego.STIX2.relationship"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Relationship",
        description="The Relationship object is used to link together two SDOs in order to describe how they are related to each other.",
        display_property="relationship_type",
        category=EntityCategories.STIX2_RELATIONSHIP_OBJECTS.value,
        display_name_plural="Relationship",
        icon_resource="stix_two_relationship",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(relationship--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `relationship`.",
        value="relationship",
        sample_value="relationship",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    relationship_type: str = MEF(
        name="relationship_type",
        display_name="Relationship_Type",
        description="The name used to identify the type of relationship.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that helps provide context about the relationship.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    source_ref: str = MEF(
        name="source_ref",
        display_name="Source_Ref",
        description="The ID of the source (from) object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    target_ref: str = MEF(
        name="target_ref",
        display_name="Target_Ref",
        description="The ID of the target (to) object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    start_time: str = MEF(
        name="start_time",
        display_name="Start_Time",
        description="This optional timestamp represents the earliest time at which the Relationship between the objects exists. If this property is a future timestamp, at the time the updated property is defined, then this represents an estimate by the producer of the intelligence of the earliest time at which relationship will be asserted to be true.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    stop_time: str = MEF(
        name="stop_time",
        display_name="Stop_Time",
        description="The latest time at which the Relationship between the objects exists. If this property is a future timestamp, at the time the updated property is defined, then this represents an estimate by the producer of the intelligence of the latest time at which relationship will be asserted to be true.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2report(STIX2Core):
    TYPE_NAME = "maltego.STIX2.report"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Report",
        description="Reports are collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including context and related details.",
        display_property="name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Report",
        icon_resource="stix_two_report",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(report--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `report`.",
        value="report",
        sample_value="report",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    report_types: List[str] = MEF(
        name="report_types",
        display_name="Report_Types",
        description="This field is an Open Vocabulary that specifies the primary subject of this report. The suggested values for this field are in report-type-ov.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="The name used to identify the Report.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about Report.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    published: str = MEF(
        name="published",
        display_name="Published",
        description="The date that this report object was officially published by the creator of this report.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_refs: List[str] = MEF(
        name="object_refs",
        display_name="Object_Refs",
        description="Specifies the STIX Objects that are referred to by this Report.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2sighting(STIX2Core):
    TYPE_NAME = "maltego.STIX2.sighting"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Sighting",
        description="A Sighting denotes the belief that something in CTI (e.g., an indicator, malware, tool, threat actor, etc.) was seen.",
        display_property="id",
        category=EntityCategories.STIX2_RELATIONSHIP_OBJECTS.value,
        display_name_plural="Sighting",
        icon_resource="stix_two_sighting",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(sighting--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `sighting`.",
        value="sighting",
        sample_value="sighting",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="A description that provides more details and context about the Sighting.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    first_seen: str = MEF(
        name="first_seen",
        display_name="First_Seen",
        description="The beginning of the time window during which the SDO referenced by the sighting_of_ref property was sighted.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    last_seen: str = MEF(
        name="last_seen",
        display_name="Last_Seen",
        description="The end of the time window during which the SDO referenced by the sighting_of_ref property was sighted.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    count: str = MEF(
        name="count",
        display_name="Count",
        description="This is an integer between 0 and 999,999,999 inclusive and represents the number of times the object was sighted.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    sighting_of_ref: str = MEF(
        name="sighting_of_ref",
        display_name="Sighting_Of_Ref",
        description="An ID reference to the object that has been sighted.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    observed_data_refs: List[str] = MEF(
        name="observed_data_refs",
        display_name="Observed_Data_Refs",
        description="A list of ID references to the Observed Data objects that contain the raw cyber data for this Sighting.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    where_sighted_refs: List[str] = MEF(
        name="where_sighted_refs",
        display_name="Where_Sighted_Refs",
        description="A list of ID references to the Identity or Location objects describing the entities or types of entities that saw the sighting.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    summary: str = MEF(
        name="summary",
        display_name="Summary",
        description="The summary property indicates whether the Sighting should be considered summary data. ",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2software(STIX2Core):
    TYPE_NAME = "maltego.STIX2.software"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Software",
        description="The Software Object represents high-level properties associated with software, including software products.",
        display_property="name",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Software",
        icon_resource="stix_two_default_icon",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(software--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `software`.",
        value="software",
        sample_value="software",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="Specifies the name of the software.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    cpe: str = MEF(
        name="cpe",
        display_name="Cpe",
        description="Specifies the Common Platform Enumeration (CPE) entry for the software, if available. The value for this property MUST be a CPE v2.3 entry from the official NVD CPE Dictionary.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    swid: str = MEF(
        name="swid",
        display_name="Swid",
        description="Specifies the Software Identification (SWID) Tags entry for the software, if available.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    languages: List[str] = MEF(
        name="languages",
        display_name="Languages",
        description="Specifies the languages supported by the software. The value of each list member MUST be an ISO 639-2 language code.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    vendor: str = MEF(
        name="vendor",
        display_name="Vendor",
        description="Specifies the name of the vendor of the software.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    version: str = MEF(
        name="version",
        display_name="Version",
        description="Specifies the version of the software.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2tool(STIX2Core):
    TYPE_NAME = "maltego.STIX2.tool"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Tool",
        description="Tools are legitimate software that can be used by threat actors to perform attacks.",
        display_property="name",
        category=EntityCategories.STIX2_DOMAIN_OBJECTS.value,
        display_name_plural="Tool",
        icon_resource="stix_two_tool",
        _visible=True,
        conversion_order=1,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(tool--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The type of this object, which MUST be the literal `tool`.",
        value="tool",
        sample_value="tool",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by_ref: str = MEF(
        name="created_by_ref",
        display_name="Created_By_Ref",
        description=STIX2_CREATED_BY_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    labels: List[str] = MEF(
        name="labels",
        display_name="Labels",
        description=STIX2_LABELS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created: str = MEF(
        name="created",
        display_name="Created",
        description=STIX2_CREATED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified: str = MEF(
        name="modified",
        display_name="Modified",
        description=STIX2_MODIFIED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    revoked: str = MEF(
        name="revoked",
        display_name="Revoked",
        description=STIX2_REVOKED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    confidence: str = MEF(
        name="confidence",
        display_name="Confidence",
        description=STIX2_CONFIDENCE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    lang: str = MEF(
        name="lang",
        display_name="Lang",
        description=STIX2_LANGUAGE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    external_references: List[str] = MEF(
        name="external_references",
        display_name="External_References",
        description=STIX2_EXTERNAL_REFERENCES_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    aliases: List[str] = MEF(
        name="aliases",
        display_name="Aliases",
        description="Alternative names used to identify this Tool.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tool_types: List[str] = MEF(
        name="tool_types",
        display_name="Tool_Types",
        description="The kind(s) of tool(s) being described. Open Vocab - tool-type-ov",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        description="The name used to identify the Tool.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    description: str = MEF(
        name="description",
        display_name="Description",
        description="Provides more context and details about the Tool object.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tool_version: str = MEF(
        name="tool_version",
        display_name="Tool_Version",
        description="The version identifier associated with the tool.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    kill_chain_phases: List[str] = MEF(
        name="kill_chain_phases",
        display_name="Kill_Chain_Phases",
        description="The list of kill chain phases for which this Tool instance can be used.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2windowsregistrykey(STIX2Core):
    TYPE_NAME = "maltego.STIX2.windows-registry-key"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Windows Registry Key",
        description="The Registry Key Object represents the properties of a Windows registry key.",
        display_property="id",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Windows Registry Key",
        conversion_order=1,
        icon_resource="stix_two_default_icon",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(windows-registry-key--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `windows-registry-key`.",
        value="windows-registry-key",
        sample_value="windows-registry-key",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    key: str = MEF(
        name="key",
        display_name="Key",
        description="Specifies the full registry key including the hive.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    values: List[str] = MEF(
        name="values",
        display_name="Values",
        description="Specifies the values found under the registry key.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    modified_time: str = MEF(
        name="modified_time",
        display_name="Modified_Time",
        description="Specifies the last date/time that the registry key was modified.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    creator_user_ref: str = MEF(
        name="creator_user_ref",
        display_name="Creator_User_Ref",
        description="Specifies a reference to a user account, represented as a User Account Object, that created the registry key.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    number_of_subkeys: str = MEF(
        name="number_of_subkeys",
        display_name="Number_Of_Subkeys",
        description="Specifies the number of subkeys contained under the registry key.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value="{}",
        sample_value="{}",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2url(URL, STIX2Core):
    TYPE_NAME = "maltego.STIX2.url"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 Url",
        description="The URL Object represents the properties of a uniform resource locator (URL).",
        display_property="url",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="Url",
        conversion_order=1,
        icon_resource="stix_two_url",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(url--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `url`.",
        value="url",
        sample_value="url",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    url: Url = MEF(
        name="url",
        display_name="Url",
        description="Specifies the value of the URL.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"url": ["value"]}',
        sample_value='{"url": ["value"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class STIX2x509certificate(X509Certificate, STIX2Core):
    TYPE_NAME = "maltego.STIX2.x509-certificate"

    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="STIX2 X509 Certificate",
        description="The X509 Certificate Object represents the properties of an X.509 certificate.",
        display_property="id",
        category=EntityCategories.STIX2_OBSERVABLES.value,
        display_name_plural="X509 Certificate",
        conversion_order=1,
        icon_resource="stix_two_default_icon",
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"^(x509-certificate--[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})$",
            groups=["id"],
        ),
    )

    type: str = MEF(
        name="type",
        display_name="Type",
        readonly=True,
        description="The value of this property MUST be `x509-certificate`.",
        value="x509-certificate",
        sample_value="x509-certificate",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    spec_version: str = MEF(
        name="spec_version",
        display_name="Spec_Version",
        description=STIX2_SPEC_VERSION_OBSERVABLE_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    object_marking_refs: List[str] = MEF(
        name="object_marking_refs",
        display_name="Object_Marking_Refs",
        description=STIX2_OBJ_MARKING_REFS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    granular_markings: List[str] = MEF(
        name="granular_markings",
        display_name="Granular_Markings",
        description=STIX2_GRANULAR_MARKINGS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    defanged: str = MEF(
        name="defanged",
        display_name="Defanged",
        description=STIX2_DEFANGED_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )

    extensions: str = MEF(
        name="extensions",
        display_name="Extensions",
        description=STIX2_EXTENSIONS_PROPERTY_DESCRIPTION,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    serial: str = MEF(
        name="serial",
        display_name="Serial",
        description="Specifies the unique identifier for the certificate, as issued by a specific Certificate Authority.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    issuer: str = MEF(
        name="issuer",
        display_name="Issuer",
        description="Specifies the name of the Certificate Authority that issued the certificate.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    valid_from: str = MEF(
        name="validFrom",
        display_name="Validfrom",
        description="Specifies the date on which the certificate validity period begins.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    valid_to: str = MEF(
        name="validTo",
        display_name="Validto",
        description="Specifies the date on which the certificate validity period ends.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    subject: str = MEF(
        name="subject",
        display_name="Subject",
        description="Specifies the name of the entity associated with the public key stored in the subject public key field of the certificate.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    is_self_signed: str = MEF(
        name="is_self_signed",
        display_name="Is_Self_Signed",
        description="Specifies whether the certificate is self-signed, i.e., whether it is signed by the same entity whose identity it certifies.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    hashes: str = MEF(
        name="hashes",
        display_name="Hashes",
        description="Specifies any hashes that were calculated for the entire contents of the certificate.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    version: str = MEF(
        name="version",
        display_name="Version",
        description="Specifies the version of the encoded certificate.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    signature_algorithm: str = MEF(
        name="signature_algorithm",
        display_name="Signature_Algorithm",
        description="Specifies the name of the algorithm used to sign the certificate.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    subject_public_key_algorithm: str = MEF(
        name="subject_public_key_algorithm",
        display_name="Subject_Public_Key_Algorithm",
        description="Specifies the name of the algorithm with which to encrypt data being sent to the subject.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    subject_public_key_modulus: str = MEF(
        name="subject_public_key_modulus",
        display_name="Subject_Public_Key_Modulus",
        description="Specifies the modulus portion of the subject’s public RSA key.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    subject_public_key_exponent: str = MEF(
        name="subject_public_key_exponent",
        display_name="Subject_Public_Key_Exponent",
        description="Specifies the exponent portion of the subject’s public RSA key, as an integer.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x509_v3_extensions: str = MEF(
        name="x509_v3_extensions",
        display_name="X509_V3_Extensions",
        description="Specifies any standard X.509 v3 extensions that may be used in the certificate.",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    x_maltego_recovery_property_mapping: str = MEF(
        name="x_maltego_recovery_property_mapping",
        display_name="x_maltego_recovery_property_mapping",
        readonly=True,
        description=X_MALTEGO_RECOVERY_PROPERTY_MAPPING_DESCRIPTION,
        value='{"subject": ["subject"], "serial": ["serial_number"], "issuer": ["issuer"], "validFrom": ["validity_not_before"], "validTo": ["validity_not_after"]}',
        sample_value='{"subject": ["subject"], "serial": ["serial_number"], "issuer": ["issuer"], "validFrom": ["validity_not_before"], "validTo": ["validity_not_after"]}',
        matching_rule=MATCHING_RULE_LOOSE,
    )
