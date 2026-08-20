# Changelog

All notable changes to this project will be documented in this file.

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
