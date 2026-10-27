# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

## v1.0.3 (2026-10-27)

### Changed

- Require `maltego-transforms` 1.4.0 or later within the 1.x series and update the dependency lockfile.

### Fix

- Use the category-qualified icon `Technology/ID` for `maltego.InternalIdentifier`. The bare name `ID` is also the
  country code alias of Indonesia's flag, so icon lookups could draw the flag instead of the ID card.
- Match complete pasted values when converting domains, websites, IP addresses, email addresses, images, people, and phone numbers.
- Add MAC address, autonomous-system number, and CIDR converters; correct IPv6 matching and hash conversion precedence.

## v1.0.2 (2026-10-09)

### Fix

- Require `maltego-transforms` 1.3.0 or later within the 1.x series.
- Update the dependency lockfile to SDK 1.3.0.

## v1.0.1 (2026-08-20)

### Fix

- Use Munich's non-zero default coordinates for `maltego.Location` so its
  default entity can register as a valid map location.
- Require `maltego-transforms` 1.0.1 and resolve `cryptography` 50.0.0.
- Prepare, attest, and attach release assets before publishing immutable
  GitHub releases.

## v1.0.0 (2026-06-19)

### Feat

- Provide Python classes for the Maltego standard entity catalog.
- Include Casefile entities under `maltego.entities.casefile`.
- Export standard and Casefile entities from `maltego.entities`.
- Include icon classes, category definitions, packaged icon assets, and `py.typed`.
