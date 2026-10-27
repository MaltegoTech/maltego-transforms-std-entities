---
name: entity-schema-maintenance
description: Rules for adding or changing entity schemas in src/maltego/entities/ — converter regexes, conversion_order, and the client constraints both must satisfy. Use when adding an entity, editing a converter regex, changing a conversion_order, or reviewing a diff that touches either.
---

# Entity Schema Maintenance

Constraints that apply whenever `Config.converter` or `Config.conversion_order`
changes. Both feed the client's paste-conversion: a user drops text on the
graph, every converter regex is tested against it, and the match with the
lowest `conversion_order` wins.

Scoped to converters and ordering; `readonly` / `hidden` / `matching_rule` on
properties are out of scope.

## The clients are JavaScript/TypeScript and Java

Regexes are executed by both. Write only what runs identically in each, and
never assume Python semantics — the tests use the `regex` PyPI package
precisely because `re` is the odd one out.

**Safe:** character classes, quantifiers, alternation, anchors, non-capturing
groups `(?:…)`, lookahead `(?=…)` / `(?!…)`, backreferences.

**Rules:**

- **`\p{...}` Unicode properties are allowed, but need the `u` flag in JS.**
  Without it, JS reads `\p` as a literal `p` and matches the wrong thing
  silently. Java is fine unconditionally. If you use these, confirm the TS
  client compiles with `u`.

  Do not "simplify" them to ASCII ranges. `\p{Lu}`/`\p{Ll}` is what lets
  `Person` match names outside English — `[A-Z][a-z]` drops every accented
  name, and even a Latin-1 range drops Polish, Cyrillic and Greek.
- **No lookbehind.** Support is uneven across JS runtimes; Java's is
  fixed-width only.
- **No named groups.** Syntax differs (`(?<n>…)` vs Java's stricter naming);
  converters map groups positionally anyway.
- **No inline flags** (`(?i)`, `(?m)`). JS rejects them outright.
- **No possessive quantifiers or atomic groups** (`a++`, `(?>…)`). Java-only.
- **Escape literal dots.** A bare `.` matches any character. This has already
  shipped as a bug: `IPv6Address` carried `2[0-4]d` and `.` where `\d` and
  `\.` belonged, leaving its IPv4-mapped branches dead.
- **Avoid nested unbounded quantifiers** (`(a+)+`) — catastrophic backtracking
  hangs the client on a paste.

## Anchor every converter

Patterns must be anchored with `^` and `$`. An unanchored converter matches a
*substring*, so a URL converts to whatever it happens to contain:

```
https://docs.maltego.com/a/tickets/157095
        └─ DNSName matched the host ─┘ └─ PhoneNumber matched this ─┘
```

`$` alone is not enough — `PhoneNumber` had a trailing `$` and no `^`, and
still matched inside URLs.

Anchoring is enforced by `test_converters_do_not_match_substrings` in
`tests/test_entity_value_matching.py`.

## conversion_order

- **Leave it alone unless a test fails.** Renumbering is churn: it touches
  files no behaviour change requires and makes the diff hard to review. Change
  a number only when a failing case in
  `tests/test_entity_value_matching.py` shows the wrong entity winning.
- **Collisions are allowed.** Two entities may share a number. Precedence
  between them is then undefined, but that only matters if some value matches
  both regexes — and usually none does. Most of STIX2 sits on `1`.
- **Use 0–100 for new entries.** Lower wins. Leave room between neighbours.
- **Nudge by small amounts** (±2 to ±5) when a test does force a change, so
  the surrounding relative precedence is preserved.
- **More specific wins.** A pattern matching a narrow format sorts before a
  general one: `IPv4Address` before `Domain`, both before `Phrase`.
- **`Phrase` is the catch-all and sorts last.** Its regex is `.*`, so it
  matches everything. Any entity that must beat free text needs a lower
  number.

Anchoring the regex is usually the real fix. A value that wrongly converts is
far more often a pattern matching a substring than an ordering problem —
correct the pattern before reaching for `conversion_order`.

To see what is already in use, read it out of the schemas rather than from any
list — the code is the source of truth:

```
grep -rn "conversion_order=" src/maltego/entities/ | sort -t= -k2 -n
```

## Inherited converters

A subclass that declares no `converter` inherits its parent's regex but is
**not** a separate paste target — `MXRecord` and `NSRecord` inherit
`DNSName`'s, `PhoneNumberMobile` inherits `PhoneNumber`'s. Giving one its own
converter makes it a paste target that competes with its parent; set a
`conversion_order` only if a test shows the two resolving the wrong way.

## Capture groups

When a converter declares `groups`, the list maps positionally onto entity
properties, and the entity's value template concatenates them. Adding or
reordering a group silently changes what lands in each property — keep the
count and order stable, and prefer non-capturing `(?:…)` for grouping that is
not meant to populate a property.

## Before you finish

Add or update a case in `tests/test_entity_value_matching.py` with `value`,
`matches` (in precedence order) and `does_not_match`, then run:

```
poetry run pytest tests/test_entity_value_matching.py
```

Assert the *sequence* of entities, never the `conversion_order` numbers — the
numbers are read from the schema so they can be renumbered freely.

A regex change is not done until you have checked what it now *stops* matching
as well as what it starts matching.
