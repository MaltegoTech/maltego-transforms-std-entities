# Copyright (c) Maltego Technologies GmbH.
from maltego.categories import EntityCategories
from maltego.server import MaltegoIcon

from maltego.icons._assets import icon_path

__all__ = [
    "Fitbit",
    "GitHub",
    "Google",
    "Weibo",
    "Nikerunclub",
    "OK",
    "Skype",
    "Twitch",
    "Vivino",
    "Vkontakte",
    "Telegram",
    "TikTok",
    "Quora",
    "Discord",
]


class Fitbit(MaltegoIcon):
    filename = icon_path("Social Network", "Fitbit.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class GitHub(MaltegoIcon):
    filename = icon_path("Social Network", "GitHub.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Google(MaltegoIcon):
    filename = icon_path("Social Network", "Google.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Weibo(MaltegoIcon):
    filename = icon_path("Social Network", "Weibo.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Nikerunclub(MaltegoIcon):
    filename = icon_path("Social Network", "Nikerunclub.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class OK(MaltegoIcon):
    filename = icon_path("Social Network", "OK.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Skype(MaltegoIcon):
    filename = icon_path("Social Network", "Skype.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Twitch(MaltegoIcon):
    filename = icon_path("Social Network", "Twitch.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Vivino(MaltegoIcon):
    filename = icon_path("Social Network", "Vivino.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Vkontakte(MaltegoIcon):
    filename = icon_path("Social Network", "Vkontakte.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Telegram(MaltegoIcon):
    filename = icon_path("Social Network", "Telegram.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class TikTok(MaltegoIcon):
    filename = icon_path("Social Network", "TikTok.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Quora(MaltegoIcon):
    filename = icon_path("Social Network", "Quora.png")
    category = EntityCategories.SOCIAL_NETWORK.value


class Discord(MaltegoIcon):
    filename = icon_path("Social Network", "Discord.png")
    category = EntityCategories.SOCIAL_NETWORK.value
