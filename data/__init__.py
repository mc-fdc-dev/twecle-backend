import toml

from typing import TypedDict


class Twitter(TypedDict):
    api_key: str
    api_key_secret: str


class Config(TypedDict):
    sanic: dict
    twitter: Twitter


with open("config.toml", "r") as f:
    CONFIG: Config = toml.load(f)
