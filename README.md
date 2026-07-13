# Maltego Standard Entities

`maltego-transforms-std-entities` exposes Maltego's standard entity catalog as Python classes for transform authors.

Maltego Graph Browser and Maltego Graph Desktop discover standard entity definitions from standard entity servers. Installing this package gives Python transforms reusable classes for the same standard entity type names, so transforms can emit and consume entities that pivot cleanly between each other in the graph.

## Installation

```bash
pip install maltego-transforms-std-entities
```

## Basic Usage

```python
from maltego.entities import Domain, EmailAddress, IPv4Address, Website

domain = Domain("example.org")
website = Website("https://example.org")
address = IPv4Address("203.0.113.10")
email = EmailAddress("analyst@example.org")

print(domain.TYPE_NAME, website.TYPE_NAME, address.TYPE_NAME, email.TYPE_NAME)
```

Casefile entities are part of the same catalog and can also be imported from `maltego.entities.casefile`:

```python
from maltego.entities import BankAccount, Gun
from maltego.entities.casefile import Businessman, IdentificationNumber

print(BankAccount.TYPE_NAME, Gun.TYPE_NAME)
print(Businessman.TYPE_NAME, IdentificationNumber.TYPE_NAME)
```

## When To Extend

Prefer an existing standard entity when its type name and properties match the data your transform returns. Reusing standard entities makes downstream pivots easier because other transforms already know those schemas.

Extend a standard class when your data is the same kind of thing but needs additional properties:

```python
from maltego.entities import Person
from maltego.server import MaltegoEntityConfig, MaltegoEntityProperty


class StaffMember(Person):
    Config = MaltegoEntityConfig(display_name="Staff Member")

    employee_id: str = MaltegoEntityProperty(
        display_name="Employee ID",
        sample_value="E-42",
    )
```

Create a custom entity only when no standard entity expresses the object without losing meaning or overloading unrelated fields.

## Package Scope

This package provides the shared Python catalog for Maltego standard entities. It includes reusable entity classes, Casefile entity classes, icon classes with packaged icon assets, category definitions, and inline type information for transform authors and server implementations.

Maltego already provides discovery for these standard entities in the Graph Browser and Desktop clients, so you don't need to register them yourself. Import the classes and use them directly in your transforms.
