# Copyright (c) Maltego Technologies GmbH.
from maltego.categories import EntityCategories
from maltego.entities.personal import Person
from maltego.model.entity import MaltegoEntity
from maltego.model.entity import MaltegoEntityConfig
from maltego.model.entity.property import MEF
from maltego.model.types import MATCHING_RULE_LOOSE
from maltego.model.types import MATCHING_RULE_STRICT

__all__ = [
    "CryptocurrencyAddress",
    "BCHAddress",
    "BTCAddress",
    "DogecoinAddress",
    "ETHAddress",
    "LTCAddress",
    "CryptocurrencyBlock",
    "BCHBlock",
    "BTCBlock",
    "DogecoinBlock",
    "ETHBlock",
    "LTCBlock",
    "CryptocurrencyBlockHeight",
    "BCHBlockHeight",
    "BTCBlockHeight",
    "DogecoinBlockHeight",
    "ETHBlockHeight",
    "LTCBlockHeight",
    "CryptocurrencyTransaction",
    "BCHTransaction",
    "BTCTransaction",
    "DogecoinTransaction",
    "ETHTransaction",
    "LTCTransaction",
    "CryptocurrencyOwner",
]


class CryptocurrencyAddress(MaltegoEntity):
    TYPE_NAME = "maltego.CryptocurrencyAddress"
    Config = MaltegoEntityConfig(
        value_property="properties.cryptocurrencyaddress",
        display_name="Cryptocurrency Address",
        description="Cryptocurrency Address",
        display_property="properties.cryptocurrencyaddress",
        category=EntityCategories.CRYPTOCURRENCY.value,
        display_name_plural="Cryptocurrency Addresses",
        # overlays=[] TODO
        # overlay_image_property TODO
        icon_resource="CryptocurrencyAddress",
        _visible=True,
    )
    cryptocurrencyaddress: str = MEF(
        name="properties.cryptocurrencyaddress",
        display_name="Cryptocurrency Address",
        sample_value="1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX",
    )


class BCHAddress(CryptocurrencyAddress):
    TYPE_NAME = "maltego.BCHAddress"
    Config = MaltegoEntityConfig(
        display_name="Bitcoin Cash Address",
        description="An address in a Bitcoin Cash blockchain",
        display_name_plural="Bitcoin Cash Addresses",
        icon_resource="BCHAddress",
    )
    cryptocurrencyaddress: str = MEF(
        name="properties.cryptocurrencyaddress",
        display_name="Cryptocurrency Address",
        sample_value="qzumak2rvxksjgkjuxe2fe5jxatktlsnhy5sthr5p7",
        matching_rule=MATCHING_RULE_STRICT,
    )


class BTCAddress(CryptocurrencyAddress):
    TYPE_NAME = "maltego.BTCAddress"
    Config = MaltegoEntityConfig(
        display_name="Bitcoin Address",
        description="An address in a Bitcoin blockchain",
        display_name_plural="Bitcoin Addresses",
        icon_resource="BTCAddress",
    )
    cryptocurrencyaddress: str = MEF(
        name="properties.cryptocurrencyaddress",
        display_name="Cryptocurrency Address",
        sample_value="1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX",
        matching_rule=MATCHING_RULE_STRICT,
    )


class DogecoinAddress(CryptocurrencyAddress):
    TYPE_NAME = "maltego.DogecoinAddress"
    Config = MaltegoEntityConfig(
        display_name="Dogecoin Address",
        description="An address in a Dogecoin blockchain",
        display_name_plural="Dogecoin Addresses",
        icon_resource="DogecoinAddress",
    )
    cryptocurrencyaddress: str = MEF(
        name="properties.cryptocurrencyaddress",
        display_name="Cryptocurrency Address",
        sample_value="D8TbV6icHWUb5PkvjhbtC94cQUfBjgUye3",
        matching_rule=MATCHING_RULE_STRICT,
    )


class ETHAddress(CryptocurrencyAddress):
    TYPE_NAME = "maltego.ETHAddress"
    Config = MaltegoEntityConfig(
        display_name="Ethereum Address",
        description="An address in a Ethereum blockchain",
        display_name_plural="Ethereum Addresses",
        icon_resource="ETHAddress",
    )
    cryptocurrencyaddress: str = MEF(
        name="properties.cryptocurrencyaddress",
        display_name="Cryptocurrency Address",
        sample_value="0xa1e4380a3b1f749673e270229993ee55f35663b4",
        matching_rule=MATCHING_RULE_STRICT,
    )


class LTCAddress(CryptocurrencyAddress):
    TYPE_NAME = "maltego.LTCAddress"
    Config = MaltegoEntityConfig(
        display_name="Litecoin Address",
        description="An address in a Litecoin blockchain",
        display_name_plural="Litecoin Addresses",
        icon_resource="LTCAddress",
    )
    cryptocurrencyaddress: str = MEF(
        name="properties.cryptocurrencyaddress",
        display_name="Cryptocurrency Address",
        sample_value="Ler4HNAEfwYhBmGXcFP2Po1NpRUEiK8km2",
        matching_rule=MATCHING_RULE_STRICT,
    )


class CryptocurrencyBlock(MaltegoEntity):
    TYPE_NAME = "maltego.CryptocurrencyBlock"
    Config = MaltegoEntityConfig(
        value_property="properties.cryptocurrencyblock",
        display_name="Cryptocurrency Block",
        description="Cryptocurrency Block",
        display_property="properties.cryptocurrencyblock",
        category=EntityCategories.CRYPTOCURRENCY.value,
        display_name_plural="Cryptocurrency Blocks",
        # overlays=[] TODO
        # overlay_image_property TODO
        icon_resource="CryptocurrencyBlock",
        _visible=True,
    )
    cryptocurrencyblock: str = MEF(
        name="properties.cryptocurrencyblock",
        display_name="Cryptocurrency Block",
        sample_value="0000000000000000000000000000000000000000000000000000000000000000",
    )
    height: int = MEF(
        name="height",
        display_name="Block Height",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    previous_block_hash: str = MEF(
        name="previousBlockHash",
        display_name="Previous Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    next_block_hash: str = MEF(
        name="nextBlockHash",
        display_name="Next Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    merkle_root: str = MEF(
        name="merkleRoot",
        display_name="Merkle Root",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    nonce: str = MEF(
        name="nonce",
        display_name="Nonce",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class BCHBlock(CryptocurrencyBlock):
    TYPE_NAME = "maltego.BCHBlock"
    Config = MaltegoEntityConfig(
        display_name="Bitcoin Cash Block",
        description="A generic block in a Bitcoin Cash blockchain",
        display_name_plural="Bitcoin Cash Blockchain Blocks",
        icon_resource="BCHBlock",
    )
    cryptocurrencyblock: str = MEF(
        name="properties.cryptocurrencyblock",
        display_name="Cryptocurrency Block",
        sample_value="00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048",
        matching_rule=MATCHING_RULE_STRICT,
    )
    height: int = MEF(
        name="height",
        display_name="Block Height",
        sample_value=1,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    previous_block_hash: str = MEF(
        name="previousBlockHash",
        display_name="Previous Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    next_block_hash: str = MEF(
        name="nextBlockHash",
        display_name="Next Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    merkle_root: str = MEF(
        name="merkleRoot",
        display_name="Merkle Root",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    nonce: str = MEF(
        name="nonce",
        display_name="Nonce",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class BTCBlock(CryptocurrencyBlock):
    TYPE_NAME = "maltego.BTCBlock"
    Config = MaltegoEntityConfig(
        display_name="Bitcoin Block",
        description="A generic block in a Bitcoin blockchain",
        display_name_plural="Bitcoin Blockchain Blocks",
        icon_resource="BTCBlock",
    )
    cryptocurrencyblock: str = MEF(
        name="properties.cryptocurrencyblock",
        display_name="Cryptocurrency Block",
        sample_value="00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048",
        matching_rule=MATCHING_RULE_STRICT,
    )
    height: int = MEF(
        name="height",
        display_name="Block Height",
        sample_value=1,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    previous_block_hash: str = MEF(
        name="previousBlockHash",
        display_name="Previous Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    next_block_hash: str = MEF(
        name="nextBlockHash",
        display_name="Next Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    merkle_root: str = MEF(
        name="merkleRoot",
        display_name="Merkle Root",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    nonce: str = MEF(
        name="nonce",
        display_name="Nonce",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class DogecoinBlock(CryptocurrencyBlock):
    TYPE_NAME = "maltego.DogecoinBlock"
    Config = MaltegoEntityConfig(
        display_name="Dogecoin Block",
        description="A generic block in a Dogecoin blockchain",
        display_name_plural="Dogecoin Blockchain Blocks",
        icon_resource="DogecoinBlock",
    )
    cryptocurrencyblock: str = MEF(
        name="properties.cryptocurrencyblock",
        display_name="Cryptocurrency Block",
        sample_value="9ff299652aba8a4de7f8edfa42500de0e47525486674c23ad68d3147d19514a1",
        matching_rule=MATCHING_RULE_STRICT,
    )
    height: int = MEF(
        name="height",
        display_name="Block Height",
        sample_value=15,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    previous_block_hash: str = MEF(
        name="previousBlockHash",
        display_name="Previous Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    next_block_hash: str = MEF(
        name="nextBlockHash",
        display_name="Next Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    merkle_root: str = MEF(
        name="merkleRoot",
        display_name="Merkle Root",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    nonce: str = MEF(
        name="nonce",
        display_name="Nonce",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class ETHBlock(CryptocurrencyBlock):
    TYPE_NAME = "maltego.ETHBlock"
    Config = MaltegoEntityConfig(
        display_name="Ethereum Block",
        description="A generic block in a Ethereum blockchain",
        display_name_plural="Ethereum Blockchain Blocks",
        icon_resource="ETHBlock",
    )
    cryptocurrencyblock: str = MEF(
        name="properties.cryptocurrencyblock",
        display_name="Cryptocurrency Block",
        sample_value="0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd",
        matching_rule=MATCHING_RULE_STRICT,
    )
    height: int = MEF(
        name="height",
        display_name="Block Height",
        sample_value=46147,
        matching_rule=MATCHING_RULE_LOOSE,
    )
    nonce: str = MEF(
        name="nonce",
        display_name="Nonce",
        sample_value="0xba4f8ecd18aab215",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class LTCBlock(CryptocurrencyBlock):
    TYPE_NAME = "maltego.LTCBlock"
    Config = MaltegoEntityConfig(
        display_name="Litecoin Block",
        description="A generic block in a Litecoin blockchain",
        display_name_plural="Litecoin Blockchain Blocks",
        icon_resource="LTCBlock",
    )
    cryptocurrencyblock: str = MEF(
        name="properties.cryptocurrencyblock",
        display_name="Cryptocurrency Block",
        sample_value="12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2",
        matching_rule=MATCHING_RULE_STRICT,
    )
    height: int = MEF(
        name="height",
        display_name="Block Height",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    previous_block_hash: str = MEF(
        name="previousBlockHash",
        display_name="Previous Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    next_block_hash: str = MEF(
        name="nextBlockHash",
        display_name="Next Block Hash",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    merkle_root: str = MEF(
        name="merkleRoot",
        display_name="Merkle Root",
        matching_rule=MATCHING_RULE_LOOSE,
    )
    nonce: str = MEF(
        name="nonce",
        display_name="Nonce",
        matching_rule=MATCHING_RULE_LOOSE,
    )


class CryptocurrencyBlockHeight(MaltegoEntity):
    TYPE_NAME = "maltego.CryptocurrencyBlockHeight"
    Config = MaltegoEntityConfig(
        value_property="blockheight",
        display_name="Cryptocurrency Block Height",
        description="The incremental block number in the block chain, where the genesis block has a height of 0",
        display_property="blockheight",
        category=EntityCategories.CRYPTOCURRENCY.value,
        display_name_plural="Cryptocurrency Block Heights",
        icon_resource="Mine",
        _visible=True,
    )
    blockheight: int = MEF(
        name="blockheight",
        display_name="Block Height",
        sample_value=0,
        matching_rule=MATCHING_RULE_STRICT,
    )


class BCHBlockHeight(CryptocurrencyBlockHeight):
    TYPE_NAME = "maltego.BCHBlockHeight"
    Config = MaltegoEntityConfig(
        display_name="BitcoinCash Block Height",
        display_name_plural="BitcoinCash Block Heights",
    )


class BTCBlockHeight(CryptocurrencyBlockHeight):
    TYPE_NAME = "maltego.BTCBlockHeight"
    Config = MaltegoEntityConfig(
        display_name="Bitcoin Block Height",
        display_name_plural="Bitcoin Block Heights",
    )


class DogecoinBlockHeight(CryptocurrencyBlockHeight):
    TYPE_NAME = "maltego.DogecoinBlockHeight"
    Config = MaltegoEntityConfig(
        display_name="Dogecoin Block Height",
        display_name_plural="Dogecoin Block Heights",
    )


class ETHBlockHeight(CryptocurrencyBlockHeight):
    TYPE_NAME = "maltego.ETHBlockHeight"
    Config = MaltegoEntityConfig(
        display_name="Ethereum Block Height",
        display_name_plural="Ethereum Block Heights",
    )


class LTCBlockHeight(CryptocurrencyBlockHeight):
    TYPE_NAME = "maltego.LTCBlockHeight"
    Config = MaltegoEntityConfig(
        display_name="Litecoin Block Height",
        display_name_plural="Litecoin Block Heights",
    )


class CryptocurrencyTransaction(MaltegoEntity):
    TYPE_NAME = "maltego.CryptocurrencyTransaction"
    Config = MaltegoEntityConfig(
        value_property="properties.cryptocurrencytransaction",
        display_name="Cryptocurrency Transaction",
        description="Cryptocurrency Transaction",
        display_property="properties.cryptocurrencytransaction",
        category=EntityCategories.CRYPTOCURRENCY.value,
        display_name_plural="Cryptocurrency Transactions",
        # overlays=[] TODO
        # overlay_image_property TODO
        icon_resource="CryptocurrencyTransaction",
        _visible=True,
    )
    cryptocurrencytransaction: str = MEF(
        name="properties.cryptocurrencytransaction",
        display_name="Cryptocurrency Transaction",
        sample_value="e444306e6d73b2a7597d4af7f79cbd627a7fd4457b469da6e341d459d6da8777",
    )


class BCHTransaction(CryptocurrencyTransaction):
    TYPE_NAME = "maltego.BCHTransaction"
    Config = MaltegoEntityConfig(
        display_name="Bitcoin Cash Transaction",
        description="A transaction in a Bitcoin Cash blockchain",
        display_name_plural="Bitcoin Cash Transactions",
        icon_resource="BCHTransaction",
    )
    cryptocurrencytransaction: str = MEF(
        name="properties.cryptocurrencytransaction",
        display_name="Cryptocurrency Transaction",
        sample_value="0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098",
        matching_rule=MATCHING_RULE_STRICT,
    )


class BTCTransaction(CryptocurrencyTransaction):
    TYPE_NAME = "maltego.BTCTransaction"
    Config = MaltegoEntityConfig(
        display_name="Bitcoin Transaction",
        description="A transaction in a Bitcoin blockchain",
        display_name_plural="Bitcoin Transactions",
        icon_resource="BTCTransaction",
    )
    cryptocurrencytransaction: str = MEF(
        name="properties.cryptocurrencytransaction",
        display_name="Cryptocurrency Transaction",
        sample_value="e444306e6d73b2a7597d4af7f79cbd627a7fd4457b469da6e341d459d6da8777",
        matching_rule=MATCHING_RULE_STRICT,
    )


class DogecoinTransaction(CryptocurrencyTransaction):
    TYPE_NAME = "maltego.DogecoinTransaction"
    Config = MaltegoEntityConfig(
        display_name="Dogecoin Transaction",
        description="A transaction in a Dogecoin blockchain",
        display_name_plural="Dogecoin Transactions",
        icon_resource="DogecoinTransaction",
    )
    cryptocurrencytransaction: str = MEF(
        name="properties.cryptocurrencytransaction",
        display_name="Cryptocurrency Transaction",
        sample_value="395301a55288c2e9db2fffdaf6dbc2e09a4ebd0d78282e4e1a1c093b73bf69a4",
        matching_rule=MATCHING_RULE_STRICT,
    )


class ETHTransaction(CryptocurrencyTransaction):
    TYPE_NAME = "maltego.ETHTransaction"
    Config = MaltegoEntityConfig(
        display_name="Ethereum Transaction",
        description="A transaction in a Ethereum blockchain",
        display_name_plural="Ethereum Transactions",
        icon_resource="ETHTransaction",
    )
    cryptocurrencytransaction: str = MEF(
        name="properties.cryptocurrencytransaction",
        display_name="Cryptocurrency Transaction",
        sample_value="0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060",
        matching_rule=MATCHING_RULE_STRICT,
    )


class LTCTransaction(CryptocurrencyTransaction):
    TYPE_NAME = "maltego.LTCTransaction"
    Config = MaltegoEntityConfig(
        display_name="Litecoin Transaction",
        description="A transaction in a Litecoin blockchain",
        display_name_plural="Litecoin Transactions",
        icon_resource="LTCTransaction",
    )
    cryptocurrencytransaction: str = MEF(
        name="properties.cryptocurrencytransaction",
        display_name="Cryptocurrency Transaction",
        sample_value="97ddfbbae6be97fd6cdf3e7ca13232a3afff2353e29badfab7f73011edd4ced9",
        matching_rule=MATCHING_RULE_STRICT,
    )


class CryptocurrencyOwner(Person):
    TYPE_NAME = "maltego.CryptocurrencyOwner"

    Config = MaltegoEntityConfig(
        value_property="OwnerType",
        display_property="OwnerType",
        overlay_image_property="OwnerTypeIcon",
        display_name="Cryptocurrency Owner",
        category=EntityCategories.CRYPTOCURRENCY.value,
        display_name_plural="Cryptocurrency Owners",
        description="Owner of a Cryptocurrency Wallet",
        icon_resource="Businessman",
    )
    owner_type_icon: str = MEF(
        name="OwnerTypeIcon",
        display_name="Owner Type Icon",
        matching_rule=MATCHING_RULE_LOOSE,
        hidden=True,
    )

    owner_type: str = MEF(
        name="OwnerType",
        display_name="Owner Type",
        matching_rule=MATCHING_RULE_LOOSE,
    )
