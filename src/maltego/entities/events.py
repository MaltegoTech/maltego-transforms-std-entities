# Copyright (c) Maltego Technologies GmbH.
import datetime
from typing import List

from maltego.categories import EntityCategories
from maltego.entities.constants import REPLACE_EVALUATOR
from maltego.entities.locations import Location
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity.property import MEF
from maltego.model.types import daterange
from maltego.model.types import MATCHING_RULE_LOOSE

__all__ = [
    "Conversation",
    "ConversationEmail",
    "ConversationPhone",
    "DateTime",
    "Event",
    "Incident",
    "Meeting",
    "MeetingBusiness",
    "MeetingSocial",
]


class Conversation(MaltegoEntity):
    TYPE_NAME = "maltego.Conversation"
    Config = MaltegoEntityConfig(
        value_property="title",
        display_name="Conversation",
        description="A form of communication between two or more people",
        display_property="title",
        category=EntityCategories.EVENTS.value,
        allowed_root=False,
        display_name_plural="Conversations",
        icon_resource="MeetingSocial",
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="The event name",
        sample_value="Conversation",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    people: List[str] = MEF(
        name="people",
        display_name="People",
        description="The people involved",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class ConversationEmail(Conversation):
    TYPE_NAME = "maltego.ConversationEmail"
    Config = MaltegoEntityConfig(
        display_name="Conversation (Email)",
        description="A conversation via email",
        display_name_plural="Conversations (Email)",
        icon_resource="Email",
    )
    email: str = MEF(
        name="email",
        display_name="Sender Email",
        description="The email address of the sender",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    recipients: List[str] = MEF(
        name="email.recipients",
        display_name="Recipient Emails",
        description="The email address of the recipients",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class ConversationPhone(Conversation):
    TYPE_NAME = "maltego.ConversationPhone"
    Config = MaltegoEntityConfig(
        display_name="Conversation (Phone)",
        description="A telephonic conversation",
        display_name_plural="Conversations (Phone)",
        icon_resource="PhoneConversation",
    )
    caller: str = MEF(
        name="phonenumber.caller",
        display_name="Caller Number",
        description="The phone number of the caller",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    callee: str = MEF(
        name="phonenumber.callee",
        display_name="Callee Number",
        description="The phone number of the callee",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    starttime: datetime.datetime = MEF(
        name="starttime",
        display_name="Start time",
        description="The start of the conversation",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    duration: daterange = MEF(
        name="duration",
        display_name="Duration",
        description="The duration of the conversation",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class DateTime(MaltegoEntity):
    TYPE_NAME = "maltego.DateTime"
    Config = MaltegoEntityConfig(
        value_property="datetime",
        display_name="DateTime",
        description="Contains a date and a time",
        display_property="datetime",
        category=EntityCategories.EVENTS.value,
        display_name_plural="DateTimes",
        icon_resource="General/Clock",
        _visible=True,
    )
    datetime: str = MEF(
        name="datetime",
        display_name="Datetime",
        sample_value="1970-01-01 00:00:01.000000",
        matching_rule=MATCHING_RULE_LOOSE,
        evaluator=REPLACE_EVALUATOR,
    )
    date: str = MEF(
        name="date",
        display_name="Date",
        description="Main property. Either entered manually or set by a transform",
        sample_value="1970-01-01",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    month: str = MEF(
        name="month",
        display_name="Month",
        sample_value="01",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    day: str = MEF(
        name="day",
        display_name="Day",
        sample_value="01",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    year: str = MEF(
        name="year",
        display_name="Year",
        sample_value="1970",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    time: str = MEF(
        name="time",
        display_name="Time",
        sample_value="00:00:01.000000",
        matching_rule=MATCHING_RULE_LOOSE,
        evaluator=REPLACE_EVALUATOR,
    )
    hour: str = MEF(
        name="hour",
        display_name="Hour",
        sample_value="00",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    minute: str = MEF(
        name="minute",
        display_name="Minute",
        sample_value="00",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    second: str = MEF(
        name="second",
        display_name="Second",
        sample_value="01",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    offset: str = MEF(
        name="offset",
        display_name="UTC Offset",
        sample_value="000000",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    display: str = MEF(
        name="display",
        display_name="Display",
        description="Optional parameter to use for display a period of time",
        matching_rule=MATCHING_RULE_LOOSE,
    )

class Event(Location):
    TYPE_NAME = "maltego.Event"
    Config = MaltegoEntityConfig(
        value_property="title",
        display_property="title",
        display_name="Event",
        description="An occurrence usually linked with a time and place",
        display_name_plural="Events",
        icon_resource="Event",
        category=EntityCategories.EVENTS.value,
        allowed_root=False,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="The event name",
        sample_value="Event",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    starttime: datetime.datetime = MEF(
        name="starttime",
        display_name="Start Time",
        description="The start of the event",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    stoptime: datetime.datetime = MEF(
        name="stoptime",
        display_name="Stop Time",
        description="The stop of the event",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Incident(Event):
    TYPE_NAME = "maltego.Incident"
    Config = MaltegoEntityConfig(
        value_property="title",
        display_property="title",
        display_name="Incident",
        description="An event or occurrence (for instance a murder or robbery)",
        display_name_plural="Incidents",
        icon_resource="Murder",
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="The event name",
        sample_value="Murder",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Meeting(Event):
    TYPE_NAME = "maltego.Meeting"
    Config = MaltegoEntityConfig(
        value_property="title",
        display_property="title",
        display_name="Meeting",
        description="A gathering of people",
        display_name_plural="Meetings",
        icon_resource="MeetingSocial",
        allowed_root=False,
    )
    title: str = MEF(
        name="title",
        display_name="Title",
        description="The event name",
        sample_value="Meeting",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    people: List[str] = MEF(
        name="people",
        display_name="People",
        description="The people involved",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class MeetingBusiness(Meeting):
    TYPE_NAME = "maltego.MeetingBusiness"
    Config = MaltegoEntityConfig(
        display_name="Meeting (Business)",
        description="A gathering of people for a commercial purpose",
        display_name_plural="Meetings (Business)",
        icon_resource="MeetingBusiness",
    )


class MeetingSocial(Meeting):
    TYPE_NAME = "maltego.MeetingSocial"
    Config = MaltegoEntityConfig(
        display_name="Meeting (Social)",
        description="A gathering of people for discussion or entertainment",
        display_name_plural="Meetings (Social)",
        icon_resource="MeetingSocial",
    )
