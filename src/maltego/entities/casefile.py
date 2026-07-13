# pylint: disable=invalid-name, line-too-long, too-many-lines
# THIS FILE IS AUTO GENERATED
# EDIT WITH CARE
import datetime
from maltego.model.entity import MEF, MaltegoEntityConfig, MaltegoEntity
from maltego.model.types import MATCHING_RULE_LOOSE
from maltego.entities.personal import Person

__all__ = [
    "BankAccount",
    "FlightNumber",
    "IdentificationNumber",
    "PassportNumber",
    "BadGuy",
    "DrugDealer",
    "GangMember",
    "GangLeader",
    "SexOffender",
    "Terrorist",
    "TerroristLeader",
    "Unsub",
    "Businessman",
    "BusinessLeader",
    "Child",
    "Female",
    "GoodGuy",
    "Judge",
    "LawOfficer",
    "MilitaryOfficer",
    "GovernmentOfficial",
    "Lawyer",
    "Male",
    "Transport",
    "Bike",
    "Boat",
    "Bus",
    "Car",
    "Plane",
    "Train",
    "VehicleRegistration",
    "VinNumber",
    "Weapon",
    "Ammunition",
    "Blade",
    "Explosive",
    "Gun",
    "IED",
    "Missile",
    "WMD",
    "BioWeapon",
    "ChemicalWeapon",
    "NuclearWeapon",
]


def _copy_parent_config(parent: type[MaltegoEntity], display_name: str) -> MaltegoEntityConfig:
    config = parent.Config.copy()
    config.display_name = display_name
    return config


class BankAccount(MaltegoEntity):
    TYPE_NAME = "maltego.BankAccount"
    Config = MaltegoEntityConfig(
        value_property="bank.accnumber",
        display_name="Bank Account",
        description="A bank account identified by a bank name, branch number and account number",
        display_property="bank.accnumber",
        category="Tracking",
        display_name_plural="Bank Accounts",
        icon_resource="BankAccount",
        _visible=True
    )
    accnumber: str = MEF(
        name="bank.accnumber",
        display_name="Account Number",
        description="Bank account number",
        sample_value='1122334455',
        matching_rule=MATCHING_RULE_LOOSE,
    )
    name: str = MEF(
        name="bank.name",
        display_name="Bank",
        description="Bank name",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    branch: str = MEF(
        name="bank.branch",
        display_name="Branch Code",
        description="Bank branch code",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class FlightNumber(MaltegoEntity):
    TYPE_NAME = "maltego.FlightNumber"
    Config = MaltegoEntityConfig(
        value_property="flight.id",
        display_name="Flight Number",
        description="A number, when combined with the name of the airline and the date, that identifies a particular flight",
        display_property="flight.id",
        category="Tracking",
        display_name_plural="Flight Numbers",
        icon_resource="FlightNumber",
        _visible=True
    )
    id: str = MEF(
        name="flight.id",
        display_name="Flight ID",
        description="The airline and number of the flight",
        value='$trim($property(flight.airline) $property(flight.number))',
        matching_rule=MATCHING_RULE_LOOSE,
        evaluator="maltego.replace",
    )
    number: str = MEF(
        name="flight.number",
        display_name="Flight Number",
        description="The flight number",
        sample_value='LH573',
        matching_rule=MATCHING_RULE_LOOSE,
    )
    airline: str = MEF(
        name="flight.airline",
        display_name="Airline",
        description="The airline of the flight",
        sample_value='Lufthansa',
        matching_rule=MATCHING_RULE_LOOSE,
    )
    date: datetime.date = MEF(
        name="flight.date",
        display_name="Date",
        description="The flight date",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class IdentificationNumber(MaltegoEntity):
    TYPE_NAME = "maltego.IdentificationNumber"
    Config = MaltegoEntityConfig(
        value_property="identification.number",
        display_name="Identification Number",
        description="A number which may be used to verify aspects of a person's personal identity",
        display_property="identification.number",
        category="Tracking",
        display_name_plural="Identification Numbers",
        icon_resource="Identification",
        _visible=True
    )
    number: str = MEF(
        name="identification.number",
        display_name="Number",
        description="Identification number",
        sample_value='1122334455',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class PassportNumber(IdentificationNumber):
    TYPE_NAME = "maltego.PassportNumber"
    Config = _copy_parent_config(IdentificationNumber, "PassportNumber")


class BadGuy(Person):
    TYPE_NAME = "maltego.BadGuy"
    Config = _copy_parent_config(Person, "BadGuy")


class DrugDealer(BadGuy):
    TYPE_NAME = "maltego.DrugDealer"
    Config = _copy_parent_config(BadGuy, "DrugDealer")


class GangMember(BadGuy):
    TYPE_NAME = "maltego.GangMember"
    Config = _copy_parent_config(BadGuy, "GangMember")


class GangLeader(GangMember):
    TYPE_NAME = "maltego.GangLeader"
    Config = _copy_parent_config(GangMember, "GangLeader")


class SexOffender(BadGuy):
    TYPE_NAME = "maltego.SexOffender"
    Config = _copy_parent_config(BadGuy, "SexOffender")


class Terrorist(BadGuy):
    TYPE_NAME = "maltego.Terrorist"
    Config = _copy_parent_config(BadGuy, "Terrorist")


class TerroristLeader(Terrorist):
    TYPE_NAME = "maltego.TerroristLeader"
    Config = _copy_parent_config(Terrorist, "TerroristLeader")


class Unsub(BadGuy):
    TYPE_NAME = "maltego.Unsub"
    Config = _copy_parent_config(BadGuy, "Unsub")


class Businessman(Person):
    TYPE_NAME = "maltego.Businessman"
    Config = _copy_parent_config(Person, "Businessman")


class BusinessLeader(Businessman):
    TYPE_NAME = "maltego.BusinessLeader"
    Config = _copy_parent_config(Businessman, "BusinessLeader")


class Child(Person):
    TYPE_NAME = "maltego.Child"
    Config = _copy_parent_config(Person, "Child")


class Female(Person):
    TYPE_NAME = "maltego.Female"
    Config = _copy_parent_config(Person, "Female")
    firstnames: str = MEF(
        name="person.firstnames",
        display_name="First Names",
        sample_value='Jane',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class GoodGuy(Person):
    TYPE_NAME = "maltego.GoodGuy"
    Config = _copy_parent_config(Person, "GoodGuy")


class Judge(GoodGuy):
    TYPE_NAME = "maltego.Judge"
    Config = _copy_parent_config(GoodGuy, "Judge")


class LawOfficer(GoodGuy):
    TYPE_NAME = "maltego.LawOfficer"
    Config = _copy_parent_config(GoodGuy, "LawOfficer")


class MilitaryOfficer(GoodGuy):
    TYPE_NAME = "maltego.MilitaryOfficer"
    Config = _copy_parent_config(GoodGuy, "MilitaryOfficer")


class GovernmentOfficial(Person):
    TYPE_NAME = "maltego.GovernmentOfficial"
    Config = _copy_parent_config(Person, "GovernmentOfficial")


class Lawyer(Person):
    TYPE_NAME = "maltego.Lawyer"
    Config = _copy_parent_config(Person, "Lawyer")


class Male(Person):
    TYPE_NAME = "maltego.Male"
    Config = _copy_parent_config(Person, "Male")


class Transport(MaltegoEntity):
    TYPE_NAME = "maltego.Transport"
    Config = MaltegoEntityConfig(
        value_property="transport.name",
        display_name="Transport",
        description="A device that is used to transport people or cargo",
        display_property="transport.name",
        category="Transportation",
        allowed_root=False,
        display_name_plural="Transports",
        icon_resource="Car",
        _visible=True
    )
    name: str = MEF(
        name="transport.name",
        display_name="Name",
        description="Name of the airplane",
        value='$trim($property(transport.make) $property(transport.model))',
        matching_rule=MATCHING_RULE_LOOSE,
        evaluator="maltego.replace",
    )
    make: str = MEF(
        name="transport.make",
        display_name="Make",
        description="Make of the transport",
        sample_value='Shuttle',
        matching_rule=MATCHING_RULE_LOOSE,
    )
    model: str = MEF(
        name="transport.model",
        display_name="Model",
        description="Model of the transport",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Bike(Transport):
    TYPE_NAME = "maltego.Bike"
    Config = _copy_parent_config(Transport, "Bike")
    make: str = MEF(
        name="transport.make",
        display_name="Make",
        description="Make of the bike / bicycle",
        sample_value='Yamaha',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Boat(Transport):
    TYPE_NAME = "maltego.Boat"
    Config = _copy_parent_config(Transport, "Boat")
    make: str = MEF(
        name="transport.make",
        display_name="Make",
        description="Make of the bike / bicycle",
        sample_value='Ferry',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Bus(Transport):
    TYPE_NAME = "maltego.Bus"
    Config = _copy_parent_config(Transport, "Bus")
    make: str = MEF(
        name="transport.make",
        display_name="Make",
        description="Make of the bus",
        sample_value='Transit bus',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Car(Transport):
    TYPE_NAME = "maltego.Car"
    Config = _copy_parent_config(Transport, "Car")
    make: str = MEF(
        name="transport.make",
        display_name="Make",
        description="Make of the airplane",
        sample_value='Toyota',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Plane(Transport):
    TYPE_NAME = "maltego.Plane"
    Config = _copy_parent_config(Transport, "Plane")
    make: str = MEF(
        name="transport.make",
        display_name="Make",
        description="Make of the airplane",
        sample_value='Airbus',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Train(Transport):
    TYPE_NAME = "maltego.Train"
    Config = _copy_parent_config(Transport, "Train")
    make: str = MEF(
        name="transport.make",
        display_name="Make",
        description="Make of the train",
        sample_value='Maglev',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class VehicleRegistration(MaltegoEntity):
    TYPE_NAME = "maltego.VehicleRegistration"
    Config = MaltegoEntityConfig(
        value_property="vehicle.registration",
        display_name="Vehicle Registration",
        description="The registration or license number usually mounted on a vehicle for identification",
        display_property="vehicle.registration",
        category="Tracking",
        display_name_plural="Vehicle Registrations",
        icon_resource="RegistrationPlate",
        _visible=True
    )
    registration: str = MEF(
        name="vehicle.registration",
        display_name="Registration Number",
        description="A vehicle registration or license number",
        sample_value='ABC123',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class VinNumber(MaltegoEntity):
    TYPE_NAME = "maltego.VinNumber"
    Config = MaltegoEntityConfig(
        value_property="vinnumber",
        display_name="VIN Number",
        description="A Vehicle Identification Number",
        display_property="vinnumber",
        category="Tracking",
        display_name_plural="VIN Numbers",
        icon_resource="VinNumber",
        _visible=True
    )
    vinnumber: str = MEF(
        name="vinnumber",
        display_name="VIN Number",
        description="Vehicle Identification Number",
        sample_value='5GZCZ43D13S812715',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Weapon(MaltegoEntity):
    TYPE_NAME = "maltego.Weapon"
    Config = MaltegoEntityConfig(
        value_property="weapon.type",
        display_name="Weapon",
        description="Something used for inflicting bodily harm or physical damage",
        display_property="weapon.type",
        category="Weapons",
        allowed_root=False,
        display_name_plural="Weapons",
        icon_resource="Gun",
        _visible=True
    )
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='Weapon',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Ammunition(Weapon):
    TYPE_NAME = "maltego.Ammunition"
    Config = _copy_parent_config(Weapon, "Ammunition")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='Shotgun shells',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Blade(Weapon):
    TYPE_NAME = "maltego.Blade"
    Config = _copy_parent_config(Weapon, "Blade")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='Knife',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Explosive(Weapon):
    TYPE_NAME = "maltego.Explosive"
    Config = _copy_parent_config(Weapon, "Explosive")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='C4',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Gun(Weapon):
    TYPE_NAME = "maltego.Gun"
    Config = _copy_parent_config(Weapon, "Gun")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='Handgun',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class IED(Weapon):
    TYPE_NAME = "maltego.IED"
    Config = _copy_parent_config(Weapon, "IED")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='Roadside bomb',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Missile(Weapon):
    TYPE_NAME = "maltego.Missile"
    Config = _copy_parent_config(Weapon, "Missile")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='RPG',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class WMD(Weapon):
    TYPE_NAME = "maltego.WMD"
    Config = _copy_parent_config(Weapon, "WMD")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='WMD',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class BioWeapon(WMD):
    TYPE_NAME = "maltego.BioWeapon"
    Config = _copy_parent_config(WMD, "BioWeapon")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='Biological agent',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class ChemicalWeapon(WMD):
    TYPE_NAME = "maltego.ChemicalWeapon"
    Config = _copy_parent_config(WMD, "ChemicalWeapon")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='Chemical agent',
        matching_rule=MATCHING_RULE_LOOSE,
    )


class NuclearWeapon(WMD):
    TYPE_NAME = "maltego.NuclearWeapon"
    Config = _copy_parent_config(WMD, "NuclearWeapon")
    type: str = MEF(
        name="weapon.type",
        display_name="Type",
        description="Weapon type",
        sample_value='Nuclear device',
        matching_rule=MATCHING_RULE_LOOSE,
    )
