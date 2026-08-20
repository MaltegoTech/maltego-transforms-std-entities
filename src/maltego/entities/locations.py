# Copyright (c) Maltego Technologies GmbH.
from maltego.categories import EntityCategories
from maltego.entities.constants import REPLACE_EVALUATOR
from maltego.model.entity import MaltegoActionType
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityAction
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity import MaltegoEntityRegexConverter
from maltego.model.entity import Overlay
from maltego.model.entity import OverlayPositions
from maltego.model.entity import OverlayTypes
from maltego.model.entity.property import MEF
from maltego.model.types import MATCHING_RULE_LOOSE
from maltego.model.types import MATCHING_RULE_STRICT

__all__ = [
    "CircularArea",
    "GPS",
    "Location",
    "Church",
    "City",
    "Country",
    "CrimeScene",
    "Home",
    "Office",
    "Prison",
    "Region",
    "Shop",
    "TransportHub",
    "Airport",
    "Harbor",
    "TrainStation",
]


class CircularArea(MaltegoEntity):
    TYPE_NAME = "maltego.CircularArea"
    Config = MaltegoEntityConfig(
        value_property="area.circular",
        display_name="Circular Area",
        description="A circular area somewhere on Earth",
        display_property="area.circular",
        category=EntityCategories.LOCATION.value,
        display_name_plural="Circular Areas",
        icon_resource="CircularArea",
        _visible=True,
        conversion_order=250,
        actions=[
            MaltegoEntityAction(
                name="maltego.spec.action.googlemaps",
                display_name="Google Maps Me!",
                action_type=MaltegoActionType.BROWSER,
                config="http://maps.google.com/maps?ll=$property(latitude),$property(longitude)",
            ),
        ],
        converter=MaltegoEntityRegexConverter(
            regex=r"^\s*([\-\d.]+)\s*,\s*([\-\d.]+)\s*,\s*([\d]+)m?\s*$",
            groups=[
                "latitude",
                "longitude",
                "radius",
            ],
        ),
    )
    circular: str = MEF(
        name="area.circular",
        display_name="Circular Area",
        value="$property(latitude),$property(longitude),$property(radius)m",
        matching_rule=MATCHING_RULE_LOOSE,
        evaluator=REPLACE_EVALUATOR,
    )
    latitude: float = MEF(
        name="latitude",
        display_name="Latitude",
        sample_value=38.951633,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    longitude: float = MEF(
        name="longitude",
        display_name="Longitude",
        sample_value=-77.14462,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    radius: int = MEF(
        name="radius",
        display_name="Radius (m)",
        sample_value=1000,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class GPS(MaltegoEntity):
    TYPE_NAME = "maltego.GPS"
    Config = MaltegoEntityConfig(
        value_property="gps.coordinate",
        display_name="GPS Coordinate",
        description="A location on a World Geodetic System coordinate frame for Earth",
        display_property="gps.coordinate",
        category=EntityCategories.LOCATION.value,
        display_name_plural="GPS Coordinates",
        icon_resource="GPS",
        _visible=True,
        conversion_order=200,
        actions=[
            MaltegoEntityAction(
                name="maltego.spec.action.googlemaps",
                display_name="Google Maps Me!",
                action_type=MaltegoActionType.BROWSER,
                config="http://maps.google.com/maps?ll=$property(latitude),$property(longitude)",
            ),
        ],
        converter=MaltegoEntityRegexConverter(
            regex=r"^\s*([\-\d.]+)\s*,\s*([\-\d.]+)\s*$",
            groups=[
                "latitude",
                "longitude",
            ],
        ),
    )
    coordinate: str = MEF(
        name="gps.coordinate",
        display_name="GPS Coordinate",
        value="$property(latitude),$property(longitude)",
        matching_rule=MATCHING_RULE_LOOSE,
        evaluator=REPLACE_EVALUATOR,
    )
    latitude: float = MEF(
        name="latitude",
        display_name="Latitude",
        sample_value=38.951633,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    longitude: float = MEF(
        name="longitude",
        display_name="Longitude",
        sample_value=-77.14462,
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Location(MaltegoEntity):
    TYPE_NAME = "maltego.Location"
    Config = MaltegoEntityConfig(
        value_property="location.name",
        display_name="Location",
        description="A location on Mother Earth",
        display_property="location.name",
        category=EntityCategories.LOCATION.value,
        display_name_plural="Locations",
        # overlays=[EntityOverlays.Overlay(property_name='countrycode', position='SW', type='image')] TODO
        # overlay_image_property TODO
        icon_resource="Location",
        _visible=True,
        overlays=[
            Overlay(
                OverlayTypes.IMAGE,
                OverlayPositions.SOUTHWEST,
                "countrycode",
            ),
        ],
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        value="$trim($property(city), $property(country))",
        evaluator=REPLACE_EVALUATOR,
        matching_rule=MATCHING_RULE_STRICT,
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        sample_value="Germany",
    )
    city: str = MEF(
        name="city",
        display_name="City",
        sample_value="Munich",
    )
    streetaddress: str = MEF(
        name="streetaddress",
        display_name="Street Address",
        matching_rule=MATCHING_RULE_STRICT,
    )
    area: str = MEF(
        name="location.area",
        display_name="Area",
        matching_rule=MATCHING_RULE_STRICT,
    )
    areacode: str = MEF(
        name="location.areacode",
        display_name="Area Code",
        matching_rule=MATCHING_RULE_STRICT,
    )
    countrycode: str = MEF(
        name="countrycode",
        display_name="Country Code",
        sample_value="DE",
        matching_rule=MATCHING_RULE_STRICT,
    )
    longitude: float = MEF(
        name="longitude",
        display_name="Longitude",
        sample_value=11.576124,
    )
    latitude: float = MEF(
        name="latitude",
        display_name="Latitude",
        sample_value=48.137154,
    )


class Church(Location):
    TYPE_NAME = "maltego.Church"
    Config = MaltegoEntityConfig(
        display_name="Church",
        description="A place of worship",
        display_name_plural="Churches",
        icon_resource="Church",
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        sample_value="Notre Dame Cathedral",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        sample_value="France",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    city: str = MEF(
        name="city",
        display_name="City",
        sample_value="Paris",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    countrycode: str = MEF(
        name="countrycode",
        display_name="Country Code",
        sample_value="FR",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class City(Location):
    TYPE_NAME = "maltego.City"
    Config = MaltegoEntityConfig(
        display_name="City",
        description="A relatively large and permanent settlement",
        display_name_plural="Cities",
        icon_resource="Geography",
    )


class Country(Location):
    TYPE_NAME = "maltego.Country"
    Config = MaltegoEntityConfig(
        display_name="Country",
        description="A nation with its own government, occupying a particular territory",
        display_name_plural="Countries",
        icon_resource="Geography",
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        sample_value="Germany",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    city: str = MEF(
        name="city",
        display_name="City",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class CrimeScene(Location):
    TYPE_NAME = "maltego.CrimeScene"
    Config = MaltegoEntityConfig(
        display_name="Crime Scene",
        description="A location where an illegal act took place",
        display_name_plural="Crime Scenes",
        icon_resource="CrimeScene",
    )


class Home(Location):
    TYPE_NAME = "maltego.Home"
    Config = MaltegoEntityConfig(
        display_name="Home",
        description="A place of living",
        display_name_plural="Homes",
        icon_resource="Home",
    )


class Office(Location):
    TYPE_NAME = "maltego.Office"
    Config = MaltegoEntityConfig(
        display_name="Office",
        description="A place of work",
        display_name_plural="Offices",
        icon_resource="User2",
    )


class Prison(Location):
    TYPE_NAME = "maltego.Prison"
    Config = MaltegoEntityConfig(
        display_name="Prison",
        description="A building to which people are legally committed as a "
        "punishment for crimes they have committed or while awaiting trial",
        display_name_plural="Prisons",
        icon_resource="Prison",
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        sample_value="Alcatraz",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        sample_value="United States",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    city: str = MEF(
        name="city",
        display_name="City",
        sample_value="San Francisco",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    countrycode: str = MEF(
        name="countrycode",
        display_name="Country Code",
        sample_value="US",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Region(Location):
    TYPE_NAME = "maltego.Region"
    Config = MaltegoEntityConfig(
        display_name="Region",
        description="An area having definable characteristics but not always fixed boundaries or borders",
        display_name_plural="Regions",
        icon_resource="Geography",
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        sample_value="Area 51",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        sample_value="United States",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    city: str = MEF(
        name="city",
        display_name="City",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    countrycode: str = MEF(
        name="countrycode",
        display_name="Country Code",
        sample_value="US",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Shop(Location):
    TYPE_NAME = "maltego.Shop"
    Config = MaltegoEntityConfig(
        display_name="Shop",
        description="A building or part of a building where goods or services are sold",
        display_name_plural="Shops",
        icon_resource="Shop",
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        sample_value="Walmart",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        sample_value="Mexico",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    city: str = MEF(
        name="city",
        display_name="City",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    countrycode: str = MEF(
        name="countrycode",
        display_name="Country Code",
        sample_value="MEX",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class TransportHub(Location):
    TYPE_NAME = "maltego.TransportHub"
    Config = MaltegoEntityConfig(
        display_name="Transport Hub",
        description="A place where passengers and cargo are exchanged between vehicles",
        display_name_plural="Transport Hubs",
        icon_resource="TrainStation",
        allowed_root=False,
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        sample_value="Transport Hub",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Airport(TransportHub):
    TYPE_NAME = "maltego.Airport"
    Config = MaltegoEntityConfig(
        display_name="Airport",
        description="A complex of runways and buildings for the takeoff, landing, and maintenance of aircraft",
        display_name_plural="Airports",
        icon_resource="Airport",
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        sample_value="Munich International Airport",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Harbor(TransportHub):
    TYPE_NAME = "maltego.Harbor"
    Config = MaltegoEntityConfig(
        display_name="Harbor",
        description="A sheltered port where ships can load or unload passengers or goods",
        display_name_plural="Harbors",
        icon_resource="Ship",
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        sample_value="Port of Hamburg",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    country: str = MEF(
        name="country",
        display_name="Country",
        sample_value="Germany",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    city: str = MEF(
        name="city",
        display_name="City",
        sample_value="Hamburg",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    countrycode: str = MEF(
        name="countrycode",
        display_name="Country Code",
        sample_value="DE",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class TrainStation(TransportHub):
    TYPE_NAME = "maltego.TrainStation"
    Config = MaltegoEntityConfig(
        display_name="Train Station",
        description="A terminal where trains load or unload passengers or goods",
        display_name_plural="Train Stations",
        icon_resource="TrainStation",
    )
    name: str = MEF(
        name="location.name",
        display_name="Name",
        sample_value="Munich Central Station",
        matching_rule=MATCHING_RULE_LOOSE,
    )
