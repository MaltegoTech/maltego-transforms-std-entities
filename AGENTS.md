# AGENTS.md

Guidance for AI coding agents working in **`maltego-transforms-std-entities`**.

## What this repo is

`maltego-transforms-std-entities` provides the standard entity classes used with
the public `maltego-transforms` SDK. These entities model common Maltego graph
objects such as phrases, people, domains, IP addresses, files, and related
properties.

This repository is not accepting external contributions. Public issue reports
may still be useful, but code changes are maintained by the Maltego team.

## Setup, build, test

Supported Python: **>=3.11, <3.14**. The repo uses **Poetry**.

```bash
poetry install
poetry run pytest -q
poetry run ruff check .
poetry build
```

The package depends on the public `maltego-transforms` package. Do not add
non-public package indexes, organization-specific infrastructure references,
credentials, or generated artifacts to public-bound files.

## Conventions

- Prefer extending existing entity patterns before adding new abstractions.
- Keep entity names, display names, and property names stable unless the change
  is explicitly a breaking change.
- Add or update tests for entity contracts and package behavior when changing
  public entities.
- Keep release automation public and GitHub-native.

For non-trivial changes, prepare a short PRP or equivalent plan before editing
code so scope, non-goals, tests, and verification are clear.
