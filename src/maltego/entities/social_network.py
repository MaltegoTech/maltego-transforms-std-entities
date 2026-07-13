# Copyright (c) Maltego Technologies GmbH.
from maltego.categories import EntityCategories
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity.property import MEF
from maltego.model.types import MATCHING_RULE_LOOSE

__all__ = [
    "Affiliation",
    "AffiliationBebo",
    "AffiliationDiscord",
    "AffiliationDuolingo",
    "AffiliationFacebook",
    "AffiliationFitbit",
    "AffiliationFlickr",
    "AffiliationGithub",
    "AffiliationGoogle",
    "AffiliationInstagram",
    "AffiliationLinkedIn",
    "AffiliationMyspace",
    "AffiliationNikerunclub",
    "AffiliationOK",
    "AffiliationOrkut",
    "AffiliationPinterest",
    "AffiliationQuora",
    "AffiliationReddit",
    "AffiliationRunkeeper",
    "AffiliationRuntastic",
    "AffiliationSkype",
    "AffiliationSnapchat",
    "AffiliationSpock",
    "AffiliationStrava",
    "AffiliationTelegram",
    "AffiliationTikTok",
    "AffiliationTwitch",
    "AffiliationTwitter",
    "AffiliationVivino",
    "AffiliationVKontakte",
    "AffiliationWeibo",
    "AffiliationYouTube",
    "FacebookObject",
    "Twit",
    "Hashtag",
]


class Affiliation(MaltegoEntity):
    TYPE_NAME = "maltego.Affiliation"
    Config = MaltegoEntityConfig(
        value_property="person.name",
        display_name="Affiliation",
        description="Membership of a social network",
        display_property="person.name",
        category=EntityCategories.SOCIAL_NETWORK.value,
        allowed_root=False,
        display_name_plural="Affiliations",
        icon_resource="Affiliation",
        _visible=True,
    )
    name: str = MEF(
        name="person.name",
        display_name="Name",
        sample_value="John Doe",
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
    )
    uid: str = MEF(
        name="affiliation.uid",
        display_name="UID",
    )
    uid_workaround: str = MEF(
        name="uid",
        display_name="UID"
    )
    profile_url: str = MEF(
        name="affiliation.profile-url",
        display_name="Profile URL",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    alias: str = MEF(
        name="affiliation.alias",
        display_name="Alias",
    )
    profile_image: str = MEF(
        name="affiliation.profile-image",
        display_name="Profile Image",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class AffiliationBebo(Affiliation):
    TYPE_NAME = "maltego.affiliation.Bebo"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Bebo",
        description="Membership of the Bebo social network",
        display_name_plural="Affiliations - Bebo",
        icon_resource="AffiliationBebo",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        value="Bebo",
    )


class AffiliationDiscord(Affiliation):
    TYPE_NAME = "maltego.affiliation.Discord"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Discord",
        description="Membership of Discord",
        display_name_plural="Affiliations - Discord",
        icon_resource="AffiliationDiscord",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Discord",
    )


class AffiliationDuolingo(Affiliation):
    TYPE_NAME = "maltego.affiliation.Duolingo"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Duolingo",
        description="Membership of Duolingo",
        display_name_plural="Affiliations - Duolingo",
        icon_resource="Duolingo",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Duolingo",
    )


class AffiliationFacebook(Affiliation):
    TYPE_NAME = "maltego.affiliation.Facebook"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Facebook",
        description="Membership of Facebook",
        display_name_plural="Affiliations - Facebook",
        icon_resource="AffiliationFacebook",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Facebook",
    )


class AffiliationFitbit(Affiliation):
    TYPE_NAME = "maltego.affiliation.Fitbit"

    Config = MaltegoEntityConfig(
        value_property="person.name",
        display_name="Affiliation - Fitbit",
        icon_resource="Fitbit",
        description="Membership of the Fitbit",
        display_property="person.name",
        category=EntityCategories.SOCIAL_NETWORK.value,
        display_name_plural="Affiliations - Fitbit",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Fitbit",
    )


class AffiliationFlickr(Affiliation):
    TYPE_NAME = "maltego.affiliation.Flickr"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Flickr",
        description="Membership of the Flickr social network",
        display_name_plural="Affiliations - Flickr",
        icon_resource="AffiliationFlickr",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        value="Flickr",
    )


class AffiliationGithub(Affiliation):
    TYPE_NAME = "maltego.affiliation.Github"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Github",
        description="Membership of Github",
        display_name_plural="Affiliations - Github",
        icon_resource="GitHub",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Github",
    )


class AffiliationGoogle(Affiliation):
    TYPE_NAME = "maltego.affiliation.Google"

    Config = MaltegoEntityConfig(
        value_property="person.name",
        display_name="Affiliation - Google",
        icon_resource="Google",
        description="Membership of Google",
        display_property="person.name",
        category="Social Network",
        display_name_plural="Affiliations - Google",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Google",
    )


class AffiliationInstagram(Affiliation):
    TYPE_NAME = "maltego.affiliation.Instagram"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Instagram",
        description="Membership of Instagram",
        display_name_plural="Affiliations - Instagram",
        icon_resource="AffiliationInstagram",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Instagram",
    )


class AffiliationLinkedIn(Affiliation):
    TYPE_NAME = "maltego.affiliation.LinkedIn"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - LinkedIn",
        description="Membership of LinkedIn",
        display_name_plural="Affiliations - LinkedIn",
        icon_resource="AffiliationLinkedIn",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="LinkedIn",
    )


class AffiliationMyspace(Affiliation):
    TYPE_NAME = "maltego.affiliation.Myspace"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Myspace",
        description="Membership of the Myspace social network",
        display_name_plural="Affiliations - Myspace",
        icon_resource="AffiliationMyspace",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        value="Myspace",
    )


class AffiliationNikerunclub(Affiliation):
    TYPE_NAME = "maltego.affiliation.Nikerunclub"

    Config = MaltegoEntityConfig(
        value_property="person.name",
        display_name="Affiliation - Nikerunclub",
        icon_resource="Nikerunclub",
        description="Membership of Nikerunclub",
        display_property="person.name",
        category="Social Network",
        display_name_plural="Affiliations - Nikerunclub",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        value="Nikerunclub",
    )


class AffiliationOK(Affiliation):
    TYPE_NAME = "maltego.affiliation.OK"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - OK",
        description="Membership of OK",
        display_name_plural="Affiliations - OK",
        icon_resource="OK",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="OK",
    )


class AffiliationOrkut(Affiliation):
    TYPE_NAME = "maltego.affiliation.Orkut"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Orkut",
        description="Membership of the Orkut social network",
        display_name_plural="Affiliations - Orkut",
        icon_resource="AffiliationOrkut",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        value="Orkut",
    )


class AffiliationPinterest(Affiliation):
    TYPE_NAME = "maltego.affiliation.Pinterest"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Pinterest",
        description="Membership of Pinterest",
        display_name_plural="Affiliations - Pinterest",
        icon_resource="AffiliationPinterest",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Pinterest",
    )


class AffiliationQuora(Affiliation):
    TYPE_NAME = "maltego.affiliation.Quora"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Quora",
        description="Membership of Quora",
        display_name_plural="Affiliations - Quora",
        icon_resource="Quora",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Quora",
    )


class AffiliationReddit(Affiliation):
    TYPE_NAME = "maltego.affiliation.Reddit"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Reddit",
        description="Membership of Reddit",
        display_name_plural="Affiliations - Reddit",
        icon_resource="AffiliationReddit",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Reddit",
    )


class AffiliationRunkeeper(Affiliation):
    TYPE_NAME = "maltego.affiliation.Runkeeper"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Runkeeper",
        description="Membership of Runkeeper",
        display_name_plural="Affiliations - Runkeeper",
        icon_resource="Runkeeper",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Runkeeper",
    )


class AffiliationRuntastic(Affiliation):
    TYPE_NAME = "maltego.affiliation.Runtastic"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Runtastic",
        description="Membership of Runtastic",
        display_name_plural="Affiliations - Runtastic",
        icon_resource="Runtastic",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Runtastic",
    )


class AffiliationSkype(Affiliation):
    TYPE_NAME = "maltego.affiliation.Skype"

    Config = MaltegoEntityConfig(
        value_property="person.name",
        display_name="Affiliation - Skype",
        icon_resource="Skype",
        description="Membership of the Skype",
        display_property="person.name",
        category="Social Network",
        display_name_plural="Affiliations - Skype",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Skype",
    )


class AffiliationSnapchat(Affiliation):
    TYPE_NAME = "maltego.affiliation.Snapchat"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Snapchat",
        description="Membership of Snapchat",
        display_name_plural="Affiliations - Snapchat",
        icon_resource="AffiliationSnapchat",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Snapchat",
    )


class AffiliationSpock(Affiliation):
    TYPE_NAME = "maltego.affiliation.Spock"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Spock",
        description="A social network membership tracked by Spock",
        display_name_plural="Affiliations - Spock",
        icon_resource="AffiliationSpock",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        value="Spock",
    )


class AffiliationStrava(Affiliation):
    TYPE_NAME = "maltego.affiliation.Strava"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Strava",
        description="Membership of Strava",
        display_name_plural="Affiliations - Strava",
        icon_resource="Strava",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Strava",
    )


class AffiliationTelegram(Affiliation):
    TYPE_NAME = "maltego.affiliation.Telegram"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Telegram",
        description="Membership of Telegram",
        display_name_plural="Affiliations - Telegram",
        icon_resource="Telegram",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Telegram",
    )


class AffiliationTikTok(Affiliation):
    TYPE_NAME = "maltego.affiliation.TikTok"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - TikTok",
        description="Membership of TikTok",
        display_name_plural="Affiliations - TikTok",
        icon_resource="TikTok",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="TikTok",
    )


class AffiliationTwitch(Affiliation):
    TYPE_NAME = "maltego.affiliation.Twitch"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Twitch",
        description="Membership of Twitch",
        display_name_plural="Affiliations - Twitch",
        icon_resource="Twitch",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Twitch",
    )


class AffiliationTwitter(Affiliation):
    TYPE_NAME = "maltego.affiliation.Twitter"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Twitter",
        description="Membership of Twitter",
        display_name_plural="Affiliations - Twitter",
        icon_resource="AffiliationTwitter",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Twitter",
    )


class AffiliationVivino(Affiliation):
    TYPE_NAME = "maltego.affiliation.Vivino"

    Config = MaltegoEntityConfig(
        value_property="person.name",
        display_name="Affiliation - Vivino",
        icon_resource="Vivino",
        description="Membership of Vivino",
        display_property="person.name",
        category="Social Network",
        display_name_plural="Affiliations - Vivino",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Vivino",
    )


class AffiliationVKontakte(Affiliation):
    TYPE_NAME = "maltego.affiliation.VKontakte"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - VKontakte",
        description="Membership of VKontakte",
        display_name_plural="Affiliations - VKontakte",
        icon_resource="Vkontakte",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="VKontakte",
    )


class AffiliationWeibo(Affiliation):
    TYPE_NAME = "maltego.affiliation.Weibo"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - Weibo",
        description="Membership of Weibo",
        display_name_plural="Affiliations - Weibo",
        icon_resource="Weibo",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="Weibo",
    )


class AffiliationYouTube(Affiliation):
    TYPE_NAME = "maltego.affiliation.YouTube"
    Config = MaltegoEntityConfig(
        display_name="Affiliation - YouTube",
        description="Membership of YouTube",
        display_name_plural="Affiliations - YouTube",
        icon_resource="AffiliationYouTube",
        allowed_root=False,
    )
    network: str = MEF(
        name="affiliation.network",
        display_name="Network",
        readonly=True,
        sample_value="YouTube",
    )


class FacebookObject(MaltegoEntity):
    TYPE_NAME = "maltego.FacebookObject"
    Config = MaltegoEntityConfig(
        value_property="facebook.object",
        display_name="Facebook Object",
        description="Facebook Object",
        display_property="facebook.object",
        category=EntityCategories.SOCIAL_NETWORK.value,
        display_name_plural="Facebook Objects",
        icon_resource="AffiliationFacebook",
        _visible=True,
        allowed_root=False,
    )
    object: str = MEF(
        name="facebook.object",
        display_name="Facebook Object",
        sample_value="Status Message",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Hashtag(MaltegoEntity):
    TYPE_NAME = "maltego.hashtag"
    Config = MaltegoEntityConfig(
        value_property="twitter.hashtag",
        display_name="Hashtag",
        description="Twitter hashtag",
        display_property="twitter.hashtag",
        category=EntityCategories.SOCIAL_NETWORK.value,
        display_name_plural="Hashtags",
        icon_resource="Hashtag",
    )
    hashtag: str = MEF(
        name="twitter.hashtag",
        display_name="Hashtag",
        sample_value="#maltego",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class Twit(MaltegoEntity):
    TYPE_NAME = "maltego.Twit"
    Config = MaltegoEntityConfig(
        value_property="content",
        display_property="content",
        display_name="Tweet",
        description="Tweet entity",
        category=EntityCategories.SOCIAL_NETWORK.value,
        display_name_plural="Tweets",
        icon_resource="AffiliationTwitter",
        _visible=True,
        allowed_root=False,
    )
    tweet: str = MEF(
        name="twit.name",
        display_name="Tweet",
        sample_value="Over 10,000 Maltego Community Edition users!",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    id: str = MEF(
        name="id",
        display_name="Tweet ID",
        sample_value="1577709014053437443",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    author: str = MEF(
        name="author",
        display_name="Author",
        sample_value="Maltego",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    author_uri: str = MEF(
        name="author_uri",
        display_name="Author URI",
        sample_value="http://twitter.com/MaltegoHQ",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    content: str = MEF(
        name="content",
        display_name="Content",
        sample_value="What is #SOCMINT? How is it different from #OSINT? Where to collect relevant information? Here comes the #Maltego Handbook for Social Media Investigation! Get everything you need to know about SOCMINT right now: https://t.co/OPDkvktpwA https://t.co/Xqdg6D2I4l",  # pylint: disable=line-too-long
        matching_rule=MATCHING_RULE_LOOSE,
    )
    imglink: str = MEF(
        name="imglink",
        display_name="Image Link",
        sample_value="https://pbs.twimg.com/profile_images/1554396389370724352/MlFGUv0i_400x400.png",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    pubdate: str = MEF(
        name="pubdate",
        display_name="Date published",
        sample_value="2022-10-05T17:15:16.000Z",
        matching_rule=MATCHING_RULE_LOOSE,
    )
