# Copyright (c) Maltego Technologies GmbH.
from maltego.categories import EntityCategories
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity.property import MEF
from maltego.model.types import MATCHING_RULE_LOOSE

__all__ = [
    "Device",
    "Computer",
    "DesktopComputer",
    "MobileComputer",
    "MobilePhone",
    "Smartphone",
    "Camera",
    "Lens",
]


class Device(MaltegoEntity):
    TYPE_NAME = "maltego.Device"
    Config = MaltegoEntityConfig(
        value_property="device",
        overlay_image_property="device",
        display_name="Device",
        description="A device such as a phone or camera",
        display_property="device",
        category=EntityCategories.DEVICES.value,
        display_name_plural="Devices",
        icon_resource="RemoteControl",
        _visible=True,
    )
    device: str = MEF(
        name="device",
        display_name="Device",
        description="device",
        sample_value="Device",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Computer(Device):
    TYPE_NAME = "maltego.Computer"
    Config = MaltegoEntityConfig(
        display_name="Computer",
        description="An electronic device for storing and processing data",
        display_name_plural="Computers",
        icon_resource="Terminal",
        allowed_root=False,
    )
    device: str = MEF(
        name="device",
        display_name="Device",
        description="device",
        sample_value="PC",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class DesktopComputer(Computer):
    TYPE_NAME = "maltego.DesktopComputer"
    Config = MaltegoEntityConfig(
        value_property="id",
        display_name="Desktop Computer",
        description="A personal computer in a form intended for regular use at a single location",
        display_property="id",
        category=EntityCategories.DEVICES.value,
        display_name_plural="Desktop Computers",
        icon_resource="Terminal",
    )
    id: str = MEF(
        name="id",
        display_name="ID",
        description="The identifier of the desktop computer",
    )


class MobileComputer(Computer):
    TYPE_NAME = "maltego.MobileComputer"
    Config = MaltegoEntityConfig(
        display_name="Mobile Computer",
        description="A portable computer suitable for use while traveling",
        display_name_plural="Mobile Computers",
        icon_resource="MobileComputer",
    )
    device: str = MEF(
        name="device",
        display_name="Device",
        description="device",
        sample_value="MacBook",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class MobilePhone(Device):
    TYPE_NAME = "maltego.MobilePhone"
    Config = MaltegoEntityConfig(
        display_name="Mobile Phone",
        description="A device which can make and receive telephone calls over a radio link "
                    "whilst moving around a wide geographic area",
        display_name_plural="Mobile Phones",
        icon_resource="MobilePhone2",
    )
    device: str = MEF(
        name="device",
        display_name="Device",
        description="device",
        sample_value="Nokia",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Smartphone(MobilePhone):
    TYPE_NAME = "maltego.Smartphone"
    Config = MaltegoEntityConfig(
        display_name="Smartphone",
        description="A mobile phone that offers more advanced computing ability and connectivity",
        display_name_plural="Smartphones",
        icon_resource="MobilePhone",
    )
    device: str = MEF(
        name="device",
        display_name="Device",
        description="device",
        sample_value="HTC",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Camera(Device):
    TYPE_NAME = "maltego.Camera"

    Config = MaltegoEntityConfig(
        value_property="device",
        display_property="device",
        display_name="Camera",
        display_name_plural="Cameras",
        icon_resource="Camera",
        description="A camera.",
        allowed_root=False,
    )

    device: str = MEF(
        name="device",
        display_name="Device",
        readonly=True,
    )

    make: str = MEF(
        name="make",
        display_name="Make",
        description="",
        readonly=False,
        sample_value="Canon",
    )

    model: str = MEF(
        name="model",
        display_name="Model",
        description="",
        readonly=False,
        sample_value="EOS 5D Mark",
    )

    serial_number: str = MEF(
        name="serial_number",
        display_name="Serial Number",
        description="",
        readonly=False,
    )

    internal_serial_number: str = MEF(
        name="internal_serial_number",
        display_name="Internal Serial Number",
        description="",
        readonly=False,
    )


class Lens(Device):
    TYPE_NAME = "maltego.Lens"

    Config = MaltegoEntityConfig(
        value_property="device",
        display_property="device",
        display_name="Lens",
        display_name_plural="Lenses",
        description="A camera lens.",
        icon_resource="Camera",
        allowed_root=False,
    )

    device: str = MEF(
        name="device",
        display_name="Device",
        readonly=True,
    )

    model: str = MEF(
        name="model", display_name="Model", description=""
    )

    serial_number: str = MEF(
        name="serial_number", display_name="Serial Number", description=""
    )

    lens_id: str = MEF(
        name="lens_id", display_name="Id", description=""
    )
