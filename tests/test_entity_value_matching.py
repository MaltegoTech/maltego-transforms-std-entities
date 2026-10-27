"""Documents which entity schemas a pasted value converts to, and in what order.

The client tests a pasted value against every ``Config.converter`` regex and
takes the lowest ``Config.conversion_order`` among the hits. Cases list
``matches`` in that order; the numbers themselves are never asserted, only the
relative precedence.

``Phrase`` matches everything and sorts last, so it is excluded from cases and
asserted once in ``test_phrase_matches_every_value``. Only entities declaring
their own converter are evaluated -- subclasses like ``MXRecord`` inherit one
and are not separate paste targets.
"""

from typing import NamedTuple

import pytest
import regex as re

import maltego.entities
from maltego.model.entity import MaltegoEntity

DEFAULT_CONVERSION_ORDER = 2147483647


def get_declared_converter_regex(entity_type: type) -> str | None:
    """The converter regex this class declares, ignoring inherited ones."""

    def regex_of(klass: type) -> str | None:
        config = klass.__dict__.get("Config")
        return getattr(getattr(config, "converter", None), "regex", None)

    declared = regex_of(entity_type)
    if declared is None:
        return None
    inherited = next(
        (r for base in entity_type.__mro__[1:] if (r := regex_of(base))), None
    )
    return None if declared == inherited else declared


def get_conversion_order(entity_type: type) -> int:
    for klass in entity_type.__mro__:
        config = klass.__dict__.get("Config")
        order = getattr(config, "conversion_order", None)
        if order is not None:
            return order
    return DEFAULT_CONVERSION_ORDER


def build_registry() -> dict[str, tuple[int, "re.Pattern[str]"]]:
    """Every entity declaring a converter, keyed by TYPE_NAME.

    Compilation is deliberately not guarded: a pattern this cannot compile is
    a pattern some client cannot run either, and that should fail loudly.
    """
    registry: dict[str, tuple[int, re.Pattern[str]]] = {}
    for value in vars(maltego.entities).values():
        if not isinstance(value, type) or not issubclass(value, MaltegoEntity):
            continue
        type_name = getattr(value, "TYPE_NAME", None)
        pattern = get_declared_converter_regex(value)
        if not type_name or not pattern:
            continue
        registry[type_name] = (get_conversion_order(value), re.compile(pattern))
    return registry


CONVERTIBLE_ENTITIES = build_registry()


PHRASE = "maltego.Phrase"
"""The catch-all: its regex is `.*`, so it matches every value and always
sorts last. Excluded from `matching_entities` so cases only list the entities
that actually distinguish one value from another."""


def matching_entities(value: str) -> list[str]:
    """TYPE_NAMEs matching the value, in the order the client considers them.

    Uses `search`, not `fullmatch`: the client scans the pasted value rather
    than anchoring implicitly, so an unanchored converter must fail its
    `does_not_match` assertions here rather than be silently rescued.
    Precedence comes from each entity's conversion_order as declared in the
    schema; the caller asserts the sequence, not the numbers behind it.
    `Phrase` is omitted -- see `test_phrase_matches_every_value`.
    """
    return [
        type_name
        for _, type_name in sorted(
            (order, type_name)
            for type_name, (order, pattern) in CONVERTIBLE_ENTITIES.items()
            if type_name != PHRASE and pattern.search(value)
        )
    ]


class Case(NamedTuple):
    value: str
    """The text a user pastes onto the graph."""

    matches: list[str]
    """Every entity the value matches, best first. The client converts the
    value to the first one and discards the rest."""

    does_not_match: list[str]
    """Entities asserted absent from the match set. Implied by `matches`, but
    stated so the negative expectation reads as its own test."""


# ---------------------------------------------------------------------------
# URLs
#
# A URL must convert to maltego.URL and nothing more specific. Before the
# converter patterns were anchored, the host inside the URL matched DNSName and
# Domain, and a numeric path segment matched PhoneNumber.
# ---------------------------------------------------------------------------
URL_CASES = [
    Case(
        value="https://docs.maltego.com/a/tickets/157095",
        matches=["maltego.URL"],
        does_not_match=["maltego.DNSName", "maltego.Domain", "maltego.PhoneNumber"],
    ),
    Case(
        value="https://docs.maltego.com/en/support/home",
        matches=["maltego.URL"],
        does_not_match=["maltego.DNSName", "maltego.Domain", "maltego.PhoneNumber"],
    ),
    Case(
        # Website's converter is scheme-plus-host only, so it drops out for the
        # two paths above but is a real second match here.
        value="http://maltego.com/",
        matches=["maltego.URL", "maltego.Website"],
        does_not_match=["maltego.DNSName", "maltego.Domain", "maltego.PhoneNumber"],
    ),
]

# ---------------------------------------------------------------------------
# Host names
#
# DNSName needs three or more labels; a two-label name falls through to Domain.
# MXRecord and NSRecord inherit DNSName's converter rather than declaring one,
# so nothing distinguishes a mail or nameserver host from any other host name.
# ---------------------------------------------------------------------------
HOSTNAME_CASES = [
    Case(
        value="docs.maltego.com",
        matches=["maltego.DNSName"],
        does_not_match=["maltego.URL", "maltego.Domain", "maltego.MXRecord"],
    ),
    Case(
        value="www.maltego.com",
        matches=["maltego.DNSName"],
        does_not_match=["maltego.URL", "maltego.Domain"],
    ),
    Case(
        value="mail.maltego.com",
        matches=["maltego.DNSName"],
        does_not_match=["maltego.MXRecord", "maltego.NSRecord", "maltego.URL"],
    ),
    Case(
        value="ns1.maltego.com",
        matches=["maltego.DNSName"],
        does_not_match=["maltego.NSRecord", "maltego.URL"],
    ),
    Case(
        value="maltego.com",
        matches=["maltego.Domain"],
        does_not_match=["maltego.DNSName", "maltego.URL"],
    ),
    Case(
        value="maltego.co.uk",
        matches=["maltego.Domain"],
        does_not_match=["maltego.DNSName", "maltego.URL"],
    ),
]

# ---------------------------------------------------------------------------
# Network infrastructure
# ---------------------------------------------------------------------------
INFRA_CASES = [
    Case(
        value="8.8.8.8",
        matches=["maltego.IPv4Address"],
        does_not_match=["maltego.Domain", "maltego.DNSName", "maltego.IPv6Address"],
    ),
    Case(
        value="2001:0db8:85a3:0000:0000:8a2e:0370:7334",
        matches=["maltego.IPv6Address"],
        does_not_match=["maltego.IPv4Address", "maltego.DNSName"],
    ),
    Case(
        value="2001:db8::1",
        matches=["maltego.IPv6Address"],
        does_not_match=["maltego.IPv4Address", "maltego.DNSName"],
    ),
    Case(
        value="::1",
        matches=["maltego.IPv6Address"],
        does_not_match=["maltego.IPv4Address"],
    ),
    Case(
        # Zone index (RFC 4007), previously unmatched.
        value="fe80::1%eth0",
        matches=["maltego.IPv6Address"],
        does_not_match=["maltego.IPv4Address", "maltego.DNSName"],
    ),
    Case(
        # IPv4-mapped form. The dotted-quad branches were dead until the
        # literal `d`/`.` in the pattern were corrected to `\d`/`\.`.
        value="::ffff:192.168.1.1",
        matches=["maltego.IPv6Address"],
        does_not_match=["maltego.IPv4Address"],
    ),
    Case(
        value="192.168.0.0-192.168.255.255",
        matches=["maltego.Netblock"],
        does_not_match=["maltego.IPv4Address", "maltego.Domain", "maltego.CIDR"],
    ),
    Case(
        value="192.168.0.0/16",
        matches=["maltego.CIDR"],
        does_not_match=["maltego.Netblock", "maltego.IPv4Address"],
    ),
    Case(
        value="AS15169",
        matches=["maltego.AS"],
        does_not_match=["maltego.PhoneNumber", "maltego.Hash"],
    ),
    Case(
        # A bare AS number is not converted: it would swallow any integer.
        value="15169",
        matches=[],
        does_not_match=["maltego.AS", "maltego.PhoneNumber"],
    ),
    Case(
        value="00:1B:44:11:3A:B7",
        matches=["maltego.MacAddress"],
        does_not_match=["maltego.IPv6Address", "maltego.PhoneNumber"],
    ),
    Case(
        value="00-1B-44-11-3A-B7",
        matches=["maltego.MacAddress"],
        does_not_match=["maltego.IPv6Address", "maltego.PhoneNumber"],
    ),
]

# ---------------------------------------------------------------------------
# Phone numbers
#
# The converter models "optional +NN or 00NN country code, optional city or
# area code, then two digit groups". Separators are spaces and hyphens only,
# which is what keeps dotted values such as IPs and coordinates out.
# ---------------------------------------------------------------------------
PHONE_NUMBERS = [
    "+1 555 123 4567",
    "+1-555-123-4567",
    "(555) 123-4567",
    "555-1234",
    "+44 20 7946 0958",
    "020 7946 0958",
    "07700 900123",
    "+49 30 12345678",
    "0049 30 12345678",
    "+33 1 42 68 53 00",
    "+55 11 91234 5678",
    "+81 3 1234 5678",
    "+91 22 1234 5678",
    "+61 2 9374 4000",
    "+27 11 234 5678",
]

PHONE_CASES = [
    Case(
        value=number,
        matches=["maltego.PhoneNumber"],
        does_not_match=["maltego.DNSName", "maltego.Domain", "maltego.URL"],
    )
    for number in PHONE_NUMBERS
] + [
    Case(
        # Six digits is the shortest the pattern accepts: \d{3,4} plus a
        # trailing group of at least three characters.
        value="1234",
        matches=[],
        does_not_match=["maltego.PhoneNumber"],
    ),
]

# ---------------------------------------------------------------------------
# People
#
# Person's converter uses the Unicode property classes \p{Lu} and \p{Ll}. These
# run natively in Java and in JS with the `u` flag, and need the `regex`
# package in Python.
#
# The non-Latin names below are the point of this section: replacing \p{Lu}
# with [A-Z] drops every accented name, and even Latin-1 ranges drop Polish,
# Cyrillic and Greek. They exist so that "simplifying" the pattern to ASCII
# fails here instead of silently shrinking who can be pasted onto a graph.
# ---------------------------------------------------------------------------
PERSON_NAMES = [
    "John Smith",  # ASCII; the only one a [A-Z][a-z] pattern would keep
    "José Álvarez",  # Spanish
    "Åsa Ek",  # Swedish
    "Zoë Müller",  # German
    "Ünal Öztürk",  # Turkish
    "Łukasz Nowak",  # Polish -- outside Latin-1
    "Иван Петров",  # Russian -- Cyrillic
    "Γιώργος Παπας",  # Greek
]

PERSON_CASES = [
    Case(
        value=name,
        matches=["maltego.Person"],
        does_not_match=["maltego.DNSName", "maltego.Domain", "maltego.PhoneNumber"],
    )
    for name in PERSON_NAMES
] + [
    Case(
        # Known gap: the pattern is two to four capitalised-ish words, so short
        # prose still converts to a Person. Anchoring stops it matching a
        # fragment of a longer string, not this.
        value="Contact John Smith",
        matches=["maltego.Person"],
        does_not_match=["maltego.DNSName", "maltego.Domain"],
    ),
    Case(
        value="hello world",
        matches=[],
        does_not_match=["maltego.Person"],
    ),
]

# ---------------------------------------------------------------------------
# Other identifiers
# ---------------------------------------------------------------------------
OTHER_CASES = [
    Case(
        value="aw@maltego.com",
        matches=["maltego.EmailAddress"],
        does_not_match=["maltego.Domain", "maltego.DNSName"],
    ),
    Case(
        value="aw+helloworld@maltego.com",
        matches=["maltego.EmailAddress"],
        does_not_match=["maltego.Domain", "maltego.DNSName"],
    ),
    Case(
        value="first.last+tag@sub.maltego.co.uk",
        matches=["maltego.EmailAddress"],
        does_not_match=["maltego.Domain", "maltego.DNSName"],
    ),
    Case(
        value="51.5074, -0.1278",
        matches=["maltego.GPS"],
        does_not_match=["maltego.Domain", "maltego.PhoneNumber"],
    ),
    Case(
        # Third component is a radius, which is what separates this from GPS.
        value="51.5074, -0.1278, 500",
        matches=["maltego.CircularArea"],
        does_not_match=["maltego.GPS", "maltego.PhoneNumber"],
    ),
    Case(
        value="d41d8cd98f00b204e9800998ecf8427e",
        matches=["maltego.Hash"],
        does_not_match=["maltego.AS", "maltego.PhoneNumber"],
    ),
    Case(
        value="da39a3ee5e6b4b0d3255bfef95601890afd80709",
        matches=["maltego.Hash"],
        does_not_match=["maltego.AS", "maltego.PhoneNumber"],
    ),
    Case(
        # SHA-256. Hash sits at 95, above Phrase's 10000, so it actually wins.
        value="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        matches=["maltego.Hash"],
        does_not_match=["maltego.AS", "maltego.PhoneNumber"],
    ),
    Case(
        # Uppercase MD5: certutil and PowerShell's Get-FileHash emit this form,
        # so the pattern accepts [a-fA-F0-9] rather than lowercase only.
        value="D41D8CD98F00B204E9800998ECF8427E",
        matches=["maltego.Hash"],
        does_not_match=["maltego.AS", "maltego.PhoneNumber"],
    ),
    Case(
        # Uppercase SHA-1, the same shape at the 40-char branch.
        value="DA39A3EE5E6B4B0D3255BFEF95601890AFD80709",
        matches=["maltego.Hash"],
        does_not_match=["maltego.AS", "maltego.PhoneNumber"],
    ),
    Case(
        # Mixed case is still hex and still a hash.
        value="d41D8cd98F00b204E9800998eCF8427e",
        matches=["maltego.Hash"],
        does_not_match=["maltego.AS", "maltego.PhoneNumber"],
    ),
    Case(
        # A non-hex letter disqualifies it at any length.
        value="g41d8cd98f00b204e9800998ecf8427e",
        matches=[],
        does_not_match=["maltego.Hash"],
    ),
    Case(
        # 31 hex chars: between the 32/40/64 branches, so nothing claims it.
        value="d41d8cd98f00b204e9800998ecf8427",
        matches=[],
        does_not_match=["maltego.Hash"],
    ),
    Case(
        value="CVE-2021-44228",
        matches=["maltego.CVE"],
        does_not_match=["maltego.Domain", "maltego.PhoneNumber", "maltego.Hash"],
    ),
    Case(
        # Anchoring stops CVE claiming the identifier out of a sentence.
        value="Log4Shell is CVE-2021-44228 and it is critical",
        matches=[],
        does_not_match=["maltego.CVE", "maltego.Person"],
    ),
    Case(
        value="https://maltego.com/img/logo.png",
        matches=["maltego.Image", "maltego.URL"],
        does_not_match=["maltego.Website", "maltego.DNSName", "maltego.Domain"],
    ),
    Case(
        # Not an image extension, so Image drops out and URL takes it.
        value="https://maltego.com/img/logo.tiff",
        matches=["maltego.URL"],
        does_not_match=["maltego.Image", "maltego.Website"],
    ),
    Case(
        # Scheme plus host only: Website's shape, and no path for URL.
        value="https://maltego.com",
        matches=["maltego.Website"],
        does_not_match=["maltego.URL", "maltego.Image", "maltego.DNSName"],
    ),
    Case(
        # An email inside prose must not convert now that it is anchored.
        value="mail me at aw@maltego.com please",
        matches=[],
        does_not_match=["maltego.EmailAddress", "maltego.Person"],
    ),
    Case(
        # A URL inside prose, likewise.
        value="see https://maltego.com/img/logo.png for the logo",
        matches=[],
        does_not_match=["maltego.URL", "maltego.Image", "maltego.Website"],
    ),
]

CASES = (
    URL_CASES
    + HOSTNAME_CASES
    + INFRA_CASES
    + PHONE_CASES
    + PERSON_CASES
    + OTHER_CASES
)


def _id(case: Case) -> str:
    return case.value


@pytest.mark.parametrize("case", CASES, ids=_id)
def test_value_matches_expected_entities_in_precedence_order(case: Case):
    assert matching_entities(case.value) == case.matches


@pytest.mark.parametrize("case", CASES, ids=_id)
def test_value_does_not_match_unrelated_entities(case: Case):
    """Spelled out separately so the negative cases are visible as tests."""
    unexpected = sorted(set(case.does_not_match) & set(matching_entities(case.value)))
    assert not unexpected, f"{case.value!r} must not match {unexpected}"


CONVERTIBLE_ENTITY_NAMES = tuple(
    sorted(
        type_name
        for type_name, (_, pattern) in CONVERTIBLE_ENTITIES.items()
        # Phrase is the deliberate catch-all; STIX2 entities are not paste targets.
        if type_name != PHRASE and not type_name.startswith("maltego.STIX2.")
    )
)


def _exercising_value(type_name: str) -> str:
    """A case value this converter matches outright, for the anchoring probe."""
    _, pattern = CONVERTIBLE_ENTITIES[type_name]
    return next(case.value for case in CASES if pattern.fullmatch(case.value))


@pytest.mark.parametrize("type_name", CONVERTIBLE_ENTITY_NAMES)
def test_converter_is_anchored(type_name: str):
    """A converter must match a whole value or none of it.

    Padding a value the converter accepts must stop it matching. An unanchored
    pattern instead finds itself *inside* the padded value -- ``DNSName`` in a
    URL's host, ``IPv4Address`` in a CIDR block -- and outranks the converter
    that should have won. The `matching_entities` cases cover this for the
    values they list; this covers every converter, listed or not.
    """
    _, pattern = CONVERTIBLE_ENTITIES[type_name]
    assert pattern.pattern.startswith("^") and pattern.pattern.endswith("$"), (
        f"{type_name}'s converter is not wrapped in ^...$"
    )
    value = _exercising_value(type_name)
    assert pattern.fullmatch(value), f"{type_name} should match {value!r}"
    # Separators, not letters: appending "xx" to a domain yields another valid
    # domain, so that would prove nothing. Padding that cannot be absorbed does.
    # Bare whitespace is not used either -- GPS and CircularArea tolerate it
    # inside their anchors by design.
    for padded in (f"see {value} here", f"({value})"):
        assert not pattern.search(padded), (
            f"{type_name} matches inside {padded!r}; the pattern is not anchored"
        )


def test_every_converter_is_exercised_by_a_case():
    """Anchoring is only proven for converters some case value reaches."""
    unexercised = [
        type_name
        for type_name in CONVERTIBLE_ENTITY_NAMES
        if not any(
            CONVERTIBLE_ENTITIES[type_name][1].fullmatch(case.value)
            for case in CASES
        )
    ]
    assert not unexercised, f"no case value exercises: {unexercised}"


def test_phrase_matches_every_value():
    """Asserted once here rather than in every case's `matches` list."""
    _, pattern = CONVERTIBLE_ENTITIES[PHRASE]
    unmatched = [case.value for case in CASES if not pattern.fullmatch(case.value)]
    assert not unmatched, f"Phrase must match every value; missed {unmatched}"


def test_phone_number_capture_groups_are_populated_in_order():
    """The converter feeds its groups into the phone number sub-properties."""
    from maltego.entities import PhoneNumber

    converter = PhoneNumber.Config.converter
    assert converter.groups == [
        "phonenumber.countrycode",
        "phonenumber.citycode",
        "phonenumber.areacode",
        "phonenumber.lastnumbers",
    ]

    pattern = re.compile(converter.regex)
    assert pattern.fullmatch("+44 20 7946 0958").groups() == (
        "+44",
        "20",
        "7946",
        "0958",
    )
    # No country code, no city code: the leading groups stay empty rather than
    # stealing digits from the area code.
    assert pattern.fullmatch("555-1234").groups() == (None, None, "555", "1234")
    # The parenthesised, `00`-prefix and bare-city forms were rewritten along
    # with the anchoring, so each is pinned here: a regrouping that still
    # matched would otherwise silently drop a sub-property.
    assert pattern.fullmatch("(555) 123-4567").groups() == (
        None,
        "(555)",
        "123",
        "4567",
    )
    assert pattern.fullmatch("(555) 123 4567").groups() == (
        None,
        "(555)",
        "123",
        "4567",
    )
    assert pattern.fullmatch("0044 20 7946 0958").groups() == (
        "0044",
        "20",
        "7946",
        "0958",
    )
    assert pattern.fullmatch("020 7946 0958").groups() == (
        None,
        "020",
        "7946",
        "0958",
    )


@pytest.mark.parametrize("type_name", CONVERTIBLE_ENTITY_NAMES)
def test_converter_outranks_phrase(type_name: str):
    """A converter sorting after Phrase's 10000 can never win a paste.

    `MacAddress`, `AS` and `Hash` all shipped on the 2147483647 default, which
    sorts *after* the catch-all, so their patterns were dead on arrival. Derived
    over every converter rather than a hand-listed few, so a new entity left on
    the default is caught on the way in.
    """
    phrase_order, _ = CONVERTIBLE_ENTITIES[PHRASE]
    order, _ = CONVERTIBLE_ENTITIES[type_name]
    assert order < phrase_order, (
        f"{type_name} (order {order}) sorts after Phrase ({phrase_order}) "
        "and can never win a paste"
    )


def test_registry_only_holds_entities_declaring_a_converter():
    assert CONVERTIBLE_ENTITIES, "no entities with converter regexes were found"
    for type_name in ("maltego.DNSName", "maltego.PhoneNumber", "maltego.URL"):
        assert type_name in CONVERTIBLE_ENTITIES
    # These inherit their parent's converter and are not separate paste targets.
    for type_name in ("maltego.MXRecord", "maltego.PhoneNumberMobile"):
        assert type_name not in CONVERTIBLE_ENTITIES
