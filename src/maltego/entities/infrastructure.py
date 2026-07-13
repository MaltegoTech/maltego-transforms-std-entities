# Copyright (c) Maltego Technologies GmbH.
# pylint: disable=too-many-lines
from typing import List

from maltego.categories import EntityCategories
from maltego.entities.groups import Company
from maltego.entities.personal import Phrase
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity import MaltegoEntityRegexConverter
from maltego.model.entity import Overlay
from maltego.model.entity import OverlayPositions
from maltego.model.entity import OverlayTypes
from maltego.model.entity.property import MEF
from maltego.model.types import Color
from maltego.model.types import MATCHING_RULE_LOOSE
from maltego.model.types import MATCHING_RULE_STRICT
from maltego.model.types import Url

__all__ = [
    "MacAddress",
    "AS",
    "CIDR",
    "CPE",
    "DNSName",
    "MXRecord",
    "NSRecord",
    "Website",
    "Domain",
    "IPv4Address",
    "IPv6Address",
    "Netblock",
    "Banner",
    "CVE",
    "CWE",
    "Software",
    "Port",
    "Service",
    "UniqueIdentifier",
    "URL",
    "WebTitle",
    "WHOISRecord",
    "X509Certificate",
    "ISP",
    "AAAARecord",
    "ARecord",
]


class MacAddress(MaltegoEntity):
    TYPE_NAME = "maltego.MacAddress"
    Config = MaltegoEntityConfig(
        value_property="macaddress",
        display_name="MAC Address",
        description="The unique hardware address of a network device",
        display_property="macaddress",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="MAC Addresses",
        icon_resource="MacAddress",
        _visible=True,
    )
    macaddress: str = MEF(
        name="macaddress",
        display_name="MAC Address",
        sample_value="01:21:33:71:33:75",
        matching_rule=MATCHING_RULE_STRICT,
    )


class AS(MaltegoEntity):
    TYPE_NAME = "maltego.AS"
    Config = MaltegoEntityConfig(
        value_property="as.number",
        display_name="AS",
        description="An internet Autonomous System (AS)",
        display_property="as.number",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="ASs",
        icon_resource="NetworkDistribution",
        _visible=True,
    )
    number: str = MEF(
        name="as.number",
        display_name="AS Number",
        sample_value="188",
    )


class CIDR(MaltegoEntity):
    TYPE_NAME = "maltego.CIDR"
    Config = MaltegoEntityConfig(
        value_property="cidr",
        display_name="Netblock CIDR",
        description="CIDR representation of a Netblock",
        display_property="cidr",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="Netblock CIDRs",
        icon_resource="Cluster",
        conversion_order=70,
        _visible=True,
    )
    cidr: str = MEF(
        name="cidr",
        display_name="CIDR Range",
        sample_value="198.51.100.0/24",
        matching_rule=MATCHING_RULE_STRICT,
    )


class CPE(MaltegoEntity):
    TYPE_NAME = "maltego.CPE"
    Config = MaltegoEntityConfig(
        value_property="text",
        display_name="CPE",
        description="Common Platform Enumeration",
        display_property="text",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="CPEs",
        icon_resource="NetworkMonitor",
        _visible=True,
    )
    text: str = MEF(
        name="text",
        display_name="CPE",
        sample_value="cpe:2.3:o:microsoft:windows_10",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    vulnerable: str = MEF(
        name="vulnerable",
        display_name="Vulnerable",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    names: str = MEF(
        name="names",
        display_name="CPE Names",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    version: str = MEF(
        name="version",
        display_name="Version",
        sample_value="2.3",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class DNSName(MaltegoEntity):
    TYPE_NAME = "maltego.DNSName"
    Config = MaltegoEntityConfig(
        value_property="fqdn",
        display_name="DNS Name",
        description="Domain Name System server name",
        display_property="fqdn",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="DNS Names",
        icon_resource="ServerDNS",
        conversion_order=100,
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"[-\w]{1,120}\.[-\w]{1,120}\.[-\w]{0,120}\.*[-\w]{1,4}\.*[a-zA-Z]+[-\w]{1,3}",
        ),
    )
    fqdn: str = MEF(
        name="fqdn",
        display_name="DNS Name",
        sample_value="maltego.com",
        matching_rule=MATCHING_RULE_STRICT,
    )


class MXRecord(DNSName):
    TYPE_NAME = "maltego.MXRecord"
    Config = MaltegoEntityConfig(
        display_name="MX Record",
        description="A DNS mail exchange record",
        display_name_plural="MX Records",
        icon_resource="MXRecord",
    )
    fqdn: str = MEF(
        name="fqdn",
        display_name="MX Record",
        sample_value="maltego.com",
        matching_rule=MATCHING_RULE_STRICT,
    )
    priority: int = MEF(
        name="mxrecord.priority",
        display_name="Priority",
        sample_value=0,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class NSRecord(DNSName):
    TYPE_NAME = "maltego.NSRecord"
    Config = MaltegoEntityConfig(
        display_name="NS Record",
        description="A DNS name server record",
        display_name_plural="NS Records",
        icon_resource="NSRecord",
    )
    fqdn: str = MEF(
        name="fqdn",
        display_name="NS Record",
        sample_value="a.iana-servers.net.",
        matching_rule=MATCHING_RULE_STRICT,
    )


class Website(DNSName):
    TYPE_NAME = "maltego.Website"
    Config = MaltegoEntityConfig(
        display_name="Website",
        description="An internet website",
        display_name_plural="Websites",
        conversion_order=100,
        icon_resource="Website",
        converter=MaltegoEntityRegexConverter(
            regex=r"(http://|https://)[-\w\.\:]*/*",
        ),
        overlays=[
            Overlay(
                OverlayTypes.IMAGE,
                OverlayPositions.SOUTHWEST,
                "$property(fqdn)/favicon.ico",
            ),
        ],
    )
    fqdn: str = MEF(
        name="fqdn",
        display_name="Website",
        sample_value="www.maltego.com",
        matching_rule=MATCHING_RULE_STRICT,
    )
    ssl_enabled: bool = MEF(
        name="website.ssl-enabled",
        display_name="SSL Enabled",
        sample_value=False,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    ports: List[int] = MEF(
        name="ports",
        display_name="Ports",
        value=[80],
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Domain(MaltegoEntity):
    TYPE_NAME = "maltego.Domain"
    Config = MaltegoEntityConfig(
        value_property="fqdn",
        display_name="Domain",
        description="An internet domain",
        display_property="fqdn",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="Domains",
        icon_resource="NetworkGlobal",
        _visible=True,
        conversion_order=120,
        converter=MaltegoEntityRegexConverter(
            regex=r"[-\w]{1,120}\.[-\w]{1,4}\.*[-\w]{0,4}",
        ),
    )
    fqdn: str = MEF(
        name="fqdn",
        display_name="Domain Name",
        sample_value="maltego.com",
    )
    whois_info: str = MEF(
        name="whois-info",
        display_name="WHOIS Info",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class IPv4Address(MaltegoEntity):
    TYPE_NAME = "maltego.IPv4Address"
    Config = MaltegoEntityConfig(
        value_property="ipv4-address",
        display_name="IPv4 Address",
        description="An IP version 4 address",
        display_property="ipv4-address",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="IPv4 Addresses",
        icon_resource="NetworkCard",
        _visible=True,
        conversion_order=60,
        converter=MaltegoEntityRegexConverter(
            regex=r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",
        ),
    )
    ipv4_address: str = MEF(
        name="ipv4-address",
        display_name="IP Address",
        sample_value="93.184.216.34",
        matching_rule=MATCHING_RULE_STRICT,
    )
    internal: bool = MEF(
        name="ipaddress.internal",
        display_name="Internal",
        sample_value=False,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class IPv6Address(MaltegoEntity):
    TYPE_NAME = "maltego.IPv6Address"
    Config = MaltegoEntityConfig(
        value_property="ipv6-address",
        display_name="IPv6 Address",
        description="An IP version 6 address",
        display_property="ipv6-address",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="IPv6 Addresses",
        icon_resource="Technology/NetworkCard",
        _visible=True,
        conversion_order=60,
        converter=MaltegoEntityRegexConverter(
            regex=r"((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))",  # pylint: disable=line-too-long
        ),
    )
    ipv6_address: str = MEF(
        name="ipv6-address",
        display_name="IP Address",
        sample_value="2606:2800:220:1:248:1893:25c8:1946",
        matching_rule=MATCHING_RULE_STRICT,
    )
    internal: bool = MEF(
        name="ipaddress.internal",
        display_name="Internal",
        sample_value=False,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Netblock(MaltegoEntity):
    TYPE_NAME = "maltego.Netblock"
    Config = MaltegoEntityConfig(
        value_property="ipv4-range",
        display_name="Netblock",
        description="A range of IP version 4 addresses",
        display_property="ipv4-range",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="Netblocks",
        icon_resource="Cluster",
        _visible=True,
        conversion_order=70,
        converter=MaltegoEntityRegexConverter(
            regex=r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) *- *(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",  # pylint: disable=line-too-long
        ),
    )
    ipv4_range: str = MEF(
        name="ipv4-range",
        display_name="IP Range",
        sample_value="198.51.100.0-198.51.100.255",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Banner(Phrase):
    TYPE_NAME = "maltego.Banner"
    Config = MaltegoEntityConfig(
        value_property="banner.text",
        display_property="banner.text",
        display_name="Banner",
        description="Banner",
        display_name_plural="Banners",
        category=EntityCategories.INFRASTRUCTURE.value,
        icon_resource="Banner",
    )

    banner_text: str = MEF(
        name="banner.text",
        display_name="Service banner",
        description="",
        sample_value="Apache 9",
    )


class CVE(Phrase):
    TYPE_NAME = "maltego.CVE"
    Config = MaltegoEntityConfig(
        display_name="CVE",
        description="Represent a Common Vulnerabilities and Exposures",
        display_name_plural="CVEs",
        icon_resource="Alarm",
        category=EntityCategories.INFRASTRUCTURE.value,
        conversion_order=50,
        converter=MaltegoEntityRegexConverter(
            regex=r"CVE-(1999|2\d{3})-(0\d{2}[1-9]|[1-9]\d{3,})",
        ),
        overlays=[
            Overlay(
                OverlayTypes.COLOR,
                OverlayPositions.NORTHWEST,
                "cvssRatingColor",
            ),
        ],
    )
    cvss: float = MEF(
        name="cvss",
        display_name="CVSS",
        description="CVSS score assigned to this vulnerability",
        sample_value=7.5,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    cvss_rating_color: Color = MEF(
        name="cvssRatingColor",
        display_name="CVSS Rating Color",
        description="No Color (Unknown CVSS) or Grey #7f7f7f; Green #78d663 (low): 0.1-3.9; Yellow #e5e500 (Medium): 4.0-6.9; Orange #f86000 (High): 7.0-8.9; Red #c2171d (Critical): 9.0-10.0;",  # pylint: disable=line-too-long
        sample_value="#f86000",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    text: str = MEF(
        name="text",
        display_name="CVE",
        sample_value="CVE-2019-19781",
        matching_rule=MATCHING_RULE_STRICT,
    )
    epss: float = MEF(
        name="epss",
        display_name="EPSS",
        description="EPSS score assigned to this vulnerability",
        sample_value=0.00715,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class CWE(MaltegoEntity):
    TYPE_NAME = "maltego.CWE"
    Config = MaltegoEntityConfig(
        value_property="text",
        display_name="CWE",
        description="Common Weakness Enumeration",
        icon_resource="SoftwareBlocking",
        display_property="text",
        category=EntityCategories.INFRASTRUCTURE.value,
    )

    text: str = MEF(
        display_name="CWE",
        matching_rule="strict",
        value="CWE-20",
    )


class Software(MaltegoEntity):
    TYPE_NAME = "maltego.Software"

    Config = MaltegoEntityConfig(
        value_property="name",
        display_property="name",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name="Software",
        display_name_plural="Software",
        description="A collection of programs and data that tell a computer how to perform specific tasks.",
        icon_resource="Software",
    )

    name: str = MEF(name="name", display_name="Name")
    version: str = MEF(name="version", display_name="Version")


class Port(MaltegoEntity):
    TYPE_NAME = "maltego.Port"
    Config = MaltegoEntityConfig(
        value_property="port.number",
        display_name="Port",
        description="A TCP/UDP network port",
        display_property="port.number",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="Ports",
        icon_resource="Port",
        _visible=True,
    )
    number: int = MEF(
        name="port.number",
        display_name="Port number",
        value=80,
        sample_value=0,
        matching_rule=MATCHING_RULE_STRICT,
    )
    port: str = MEF(
        name="properties.port",
        display_name="Port",
        value=" ",
        sample_value="443",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Service(MaltegoEntity):
    TYPE_NAME = "maltego.Service"
    Config = MaltegoEntityConfig(
        value_property="service.name",
        display_name="Service",
        description="Network service (port and banner combination)",
        display_property="service.name",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="Services",
        icon_resource="Service",
        _visible=True,
    )
    name: str = MEF(
        name="service.name",
        display_name="Description",
        value="80/Apache 9",
        matching_rule=MATCHING_RULE_STRICT,
    )
    number: int = MEF(
        name="port.number",
        display_name="Port",
        value=80,
        sample_value=0,
        matching_rule=MATCHING_RULE_STRICT,
    )
    text: str = MEF(
        name="banner.text",
        display_name="Service banner",
        value="Apache 9",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    service: str = MEF(
        name="properties.service",
        display_name="Service",
        value=" ",
        sample_value="80:Apache",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class UniqueIdentifier(MaltegoEntity):
    TYPE_NAME = "maltego.UniqueIdentifier"
    Config = MaltegoEntityConfig(
        value_property="properties.uniqueidentifier",
        display_name="Tracking Code",
        description="Represents a tracking code for a web service.",
        display_property="properties.uniqueidentifier",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="UniqueIdentifiers",
        icon_resource="Log",
        _visible=True,
    )
    uniqueidentifier: str = MEF(
        name="properties.uniqueidentifier",
        display_name="UniqueIdentifier",
        value=" ",
        sample_value="UA-1553321-*",
        matching_rule=MATCHING_RULE_STRICT,
    )
    identifier_type: str = MEF(
        name="identifierType",
        display_name="Identifier Type",
        sample_value="Google Analytics ID",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class URL(MaltegoEntity):
    TYPE_NAME = "maltego.URL"
    Config = MaltegoEntityConfig(
        value_property="url",
        display_name="URL",
        description="An internet Uniform Resource Locator (URL)",
        display_property="short-title",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="URLs",
        icon_resource="URL",
        conversion_order=90,
        _visible=True,
        converter=MaltegoEntityRegexConverter(
            regex=r"(http[s]*://([-\w\.\:]*)[-\w\.\:/]*/[^\s\?]*(\?[^\s]*)?)",
            groups=[
                "url",
                "short-title",
            ],
        ),
    )
    short_title: str = MEF(
        name="short-title",
        display_name="Short title",
        sample_value="URL Title",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    url: Url = MEF(
        name="url",
        display_name="URL",
        sample_value="https://www.example.com",
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        sample_value="URL Title",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class WebTitle(MaltegoEntity):
    TYPE_NAME = "maltego.WebTitle"
    Config = MaltegoEntityConfig(
        value_property="title",
        display_name="Website Title",
        description="Title of a website",
        display_property="title",
        category=EntityCategories.INFRASTRUCTURE.value,
        allowed_root=False,
        display_name_plural="Website Titles",
        icon_resource="Alarm",
        _visible=True,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        sample_value="Homepage - Maltego",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class WHOISRecord(MaltegoEntity):
    TYPE_NAME = "maltego.WHOISRecord"
    Config = MaltegoEntityConfig(
        value_property="name",
        display_name="WHOIS Record",
        description="WHOIS Records of a Domain name or an IP Address",
        display_property="name",
        category=EntityCategories.INFRASTRUCTURE.value,
        allowed_root=False,
        display_name_plural="WHOIS Records",
        # overlays=[EntityOverlays.Overlay(property_name='updatedDate', position='N', type='text')] TODO
        # overlay_image_property TODO
        icon_resource="General/Book",
        _visible=True,
        overlays=[
            Overlay(
                OverlayTypes.IMAGE,
                OverlayPositions.WEST,
                "registrantCountryCode",
            ),
            Overlay(OverlayTypes.TEXT, OverlayPositions.NORTH, "updatedDate"),
        ],
    )
    name: str = MEF(
        name="name",
        display_name="Name",
        sample_value="maltego.com",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    whois_info: str = MEF(
        name="whoisInfo",
        display_name="WHOIS Info",
        sample_value="""Domain Name: MALTEGO.COM
                    Registry Domain ID: 1265032016_DOMAIN_COM-VRSN
                    Registrar WHOIS Server: whois.godaddy.com
                    ...
                """,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registry_domain_id: str = MEF(
        name="registryDomainId",
        display_name="Registry Domain ID",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    domain_name: str = MEF(
        name="domainName",
        display_name="Domain Name",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    creation_date: str = MEF(
        name="creationDate",
        display_name="Created Date",
        description="Created On",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registry_expiry_date: str = MEF(
        name="registryExpiryDate",
        display_name="Registry Expiry Date",
        description="Expires On",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    updated_date: str = MEF(
        name="updatedDate",
        display_name="Updated Date",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    transfer_date: str = MEF(
        name="transferDate",
        display_name="Transfer Date",
        description="Transferred On",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    nameservers: str = MEF(
        name="nameservers",
        display_name="Nameservers",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    nameserver_ip_addresses: str = MEF(
        name="nameserverIpAddresses",
        display_name="Name Server IP Addresses",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    maintainer: str = MEF(
        name="maintainer",
        display_name="Mantainer",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    created_by: str = MEF(
        name="createdBy",
        display_name="Created By",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    updated_by: str = MEF(
        name="updatedBy",
        display_name="Updated By",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    dnssec: str = MEF(
        name="dnssec",
        display_name="DNSSEC",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    domain_status: str = MEF(
        name="domainStatus",
        display_name="Domain Status",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    ens_auth_id: str = MEF(
        name="ensAuthId",
        display_name="ENS AuthId",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registry_registrant_id: str = MEF(
        name="registryRegistrantId",
        display_name="Registry Registrant ID",
        description="Registrant ID",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_name: str = MEF(
        name="registrantName",
        display_name="Registrant Name",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_organization: str = MEF(
        name="registrantOrganization",
        display_name="Registrant Organization",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_address: str = MEF(
        name="registrantAddress",
        display_name="Registrant Address",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_street: str = MEF(
        name="registrantStreet",
        display_name="Registrant Street",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_city: str = MEF(
        name="registrantCity",
        display_name="Registrant City",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_state_province: str = MEF(
        name="registrantStateProvince",
        display_name="Registrant State/Province",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_country: str = MEF(
        name="registrantCountry",
        display_name="Registrant Country",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_country_code: str = MEF(
        name="registrantCountryCode",
        display_name="Registrant Country Code",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_postal_code: str = MEF(
        name="registrantPostalCode",
        display_name="Registrant Postal Code",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_phone: str = MEF(
        name="registrantPhone",
        display_name="Registrant Phone",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_phone_ext: str = MEF(
        name="registrantPhoneExt",
        display_name="Registrant Phone Ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_fax: str = MEF(
        name="registrantFax",
        display_name="Registrant Fax",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_fax_ext: str = MEF(
        name="registrantFaxExt",
        display_name="Registrant Fax Ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrant_email: str = MEF(
        name="registrantEmail",
        display_name="Registrant Email",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_id: str = MEF(
        name="adminId",
        display_name="Admin ID",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registry_admin_id: str = MEF(
        name="registryAdminId",
        display_name="Admin ID",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_name: str = MEF(
        name="adminName",
        display_name="Admin Name",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_organization: str = MEF(
        name="adminOrganization",
        display_name="Admin Organization",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_address: str = MEF(
        name="adminAddress",
        display_name="Admin Address",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_street: str = MEF(
        name="adminStreet",
        display_name="Admin Street",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_city: str = MEF(
        name="adminCity",
        display_name="Admin City",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_state_province: str = MEF(
        name="adminStateProvince",
        display_name="Admin State/Province",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_country: str = MEF(
        name="adminCountry",
        display_name="Admin Country",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_country_code: str = MEF(
        name="adminCountryCode",
        display_name="Admin Country Code",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_postal_code: str = MEF(
        name="adminPostalCode",
        display_name="Admin Postal Code",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_phone: str = MEF(
        name="adminPhone",
        display_name="Admin Phone",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_phone_ext: str = MEF(
        name="adminPhoneExt",
        display_name="Admin Phone Ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_fax: str = MEF(
        name="adminFax",
        display_name="Admin Fax",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_fax_ext: str = MEF(
        name="adminFaxExt",
        display_name="Admin Fax Ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    admin_email: str = MEF(
        name="adminEmail",
        display_name="Admin Email",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registry_tech_id: str = MEF(
        name="registryTechId",
        display_name="Tech ID",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_name: str = MEF(
        name="techName",
        display_name="Tech Name",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_organization: str = MEF(
        name="techOrganization",
        display_name="Tech Organization",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_address: str = MEF(
        name="techAddress",
        display_name="Tech Address",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_city: str = MEF(
        name="techCity",
        display_name="Tech City",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_state_province: str = MEF(
        name="techStateProvince",
        display_name="Tech State/Province",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_country: str = MEF(
        name="techCountry",
        display_name="Tech Country",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_postal_code: str = MEF(
        name="techPostalCode",
        display_name="Tech Postal Code",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_phone: str = MEF(
        name="techPhone",
        display_name="Tech Phone",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_phone_ext: str = MEF(
        name="techPhoneExt",
        display_name="Tech Phone Ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_fax: str = MEF(
        name="techFax",
        display_name="Tech Fax",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_fax_ext: str = MEF(
        name="techFaxExt",
        display_name="Tech Fax Ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    tech_email: str = MEF(
        name="techEmail",
        display_name="Tech Email",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_id: str = MEF(
        name="registrarId",
        display_name="Registrar ID",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_iana_id: str = MEF(
        name="registrarIanaId",
        display_name="Registrar IANA ID",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar: str = MEF(
        name="registrar",
        display_name="Registrar",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_registration_expiration_date: str = MEF(
        name="registrarRegistrationExpirationDate",
        display_name="Registrar Registration Expiration Date",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_url: str = MEF(
        name="registrarUrl",
        display_name="Registrar URL",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_whois_server: str = MEF(
        name="registrarWhoisServer",
        display_name="Registrar WHOIS Server",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_status: str = MEF(
        name="registrarStatus",
        display_name="Registrar Status",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_address: str = MEF(
        name="registrarAddress",
        display_name="Registrar Address",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_city: str = MEF(
        name="registrarCity",
        display_name="Registrar City",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_state_province: str = MEF(
        name="registrarStateProvince",
        display_name="Registrar State/Province",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_country: str = MEF(
        name="registrarCountry",
        display_name="Registrar Country",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_postal_code: str = MEF(
        name="registrarPostalCode",
        display_name="Registrar Postal Code",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_phone: str = MEF(
        name="registrarPhone",
        display_name="Registrar Phone",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_fax: str = MEF(
        name="registrarFax",
        display_name="Registrar Fax",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_fax_ext: str = MEF(
        name="registrarFaxExt",
        display_name="Registrar Fax Ext",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_email: str = MEF(
        name="registrarEmail",
        display_name="Registrar Email",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_abuse_contact_email: str = MEF(
        name="registrarAbuseContactEmail",
        display_name="Registrar Abuse Contact Email",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    registrar_abuse_contact_phone: str = MEF(
        name="registrarAbuseContactPhone",
        display_name="Registrar Abuse Contact Phone",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    sponsoring_registrar: str = MEF(
        name="sponsoringRegistrar",
        display_name="Sponsoring Registrar",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    entity_version: str = MEF(
        name="entityVersion",
        display_name="Maltego Entity Version",
        hidden=True,
        readonly=True,
        nullable=False,
        value="0.1.0",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class X509Certificate(MaltegoEntity):
    TYPE_NAME = "maltego.X509Certificate"
    Config = MaltegoEntityConfig(
        value_property="subject",
        display_name="SSL Certificate",
        description="Certificate used by SSL/TLS servers and clients",
        display_property="subject",
        category=EntityCategories.INFRASTRUCTURE.value,
        display_name_plural="SSL Certificates",
        icon_resource="Technology/Certificate",
        _visible=True,
        overlays=[
            Overlay(OverlayTypes.TEXT, OverlayPositions.NORTH, "issuer"),
            Overlay(OverlayTypes.IMAGE, OverlayPositions.SOUTHWEST, "country"),
        ],
    )
    subject: str = MEF(
        name="subject",
        display_name="Subject",
        description="Entity identified by this certificate",
        value=" ",
        sample_value="www.maltego.com",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    issuer: str = MEF(
        name="issuer",
        display_name="Issuer",
        description="Issuer of this certificate",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    subject_d_n: str = MEF(
        name="subjectDN",
        display_name="Subject DN",
        description="Subject's Distinguished Name",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    issuer_d_n: str = MEF(
        name="issuerDN",
        display_name="Issuer DN",
        description="Issuer Distinguished Name",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    ski: str = MEF(
        name="ski",
        display_name="SKI",
        description="Subject Key Identifier",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    aki: str = MEF(
        name="aki",
        display_name="AKI",
        description="Authority Key Identifier",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    serial: str = MEF(
        name="serial",
        display_name="Serial",
        description="Serial Number",
        matching_rule=MATCHING_RULE_STRICT,
    )
    san: List[str] = MEF(
        name="san",
        display_name="SAN",
        description="Alternative subject names identified by this certificate",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    usage: List[str] = MEF(
        name="usage",
        display_name="Usage",
        description="Key Usage",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    issuance_id: str = MEF(
        name="issuanceId",
        display_name="Issuance ID",
        description="CT log ID of this cerficate's issuance",
        sample_value="0",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    valid_from: str = MEF(
        name="validFrom",
        display_name="Valid From",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    valid_to: str = MEF(
        name="validTo",
        display_name="Valid Until",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    organization: str = MEF(
        name="organization",
        display_name="Organization",
        description="Subject's organization",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class ISP(Company):
    TYPE_NAME = "maltego.ISP"
    Config = MaltegoEntityConfig(
        display_name="ISP",
        description="Represents an Internet Service Provider",
        display_name_plural="ISPs",
        icon_resource="Technology/InternetISP",
        category=EntityCategories.INFRASTRUCTURE.value,
    )


class AAAARecord(DNSName):
    TYPE_NAME = "maltego.AAAARecord"
    Config = MaltegoEntityConfig(
        display_name="AAAA Record",
        description="DNS AAAA Record",
        display_name_plural="AAAA Records",
        icon_resource="Technology/ServerDNS",
    )
    ipv6_address: str = MEF(
        name="ipv6-address",
        display_name="IPv6 Address",
        description="The IPv6 address the AAAA record points to.",
        sample_value="2606:2800:220:1:248:1893:25c8:1946",
        matching_rule=MATCHING_RULE_STRICT,
    )
    time_to_live: int = MEF(
        name="time-to-live",
        display_name="Time to Live (TTL)",
        description="The time-to-live in seconds. This is the amount of time "
        "the record is allowed to be cached by a resolver.",
        sample_value=3600,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class ARecord(DNSName):
    TYPE_NAME = "maltego.ARecord"
    Config = MaltegoEntityConfig(
        display_name="A Record",
        description="DNS A Record",
        display_name_plural="A Records",
        icon_resource="Technology/ServerDNS",
    )
    ipv4_address: str = MEF(
        name="ipv4-address",
        display_name="IPv4 Address",
        description="The IPv4 address the A record points to.",
        sample_value="104.198.14.52",
        matching_rule=MATCHING_RULE_STRICT,
    )
    time_to_live: int = MEF(
        name="time-to-live",
        display_name="Time to Live (TTL)",
        description="The time-to-live in seconds. "
        "This is the amount of time the record is allowed to be cached by a resolver.",
        sample_value=3600,
        matching_rule=MATCHING_RULE_LOOSE,
    )
