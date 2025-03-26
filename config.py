# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List

@dataclass
class BotConfig:
    TOKEN: str = "7510441533:AAHrqS5AWdHzLlNNlrg5FncL-YlmQjSs16k"
    ADMIN_IDS: List[int] = field(default_factory=lambda: [6236467772])
    DB_NAME: str = "code_selling_bot.db"
    ANNOUNCEMENT_CHANNEL: str = "@cooplink"

@dataclass
class Channels:
    REQUIRED: List[str] = field(default_factory=lambda: ["@cooplink", "@pythonnews_uzbekistan"])
    ANNOUNCEMENT: str = "@cooplink"

config = BotConfig()
channels = Channels()

BOT_TOKEN = config.TOKEN
ADMIN_IDS = config.ADMIN_IDS
DB_NAME = config.DB_NAME
ANNOUNCEMENT_CHANNEL = config.ANNOUNCEMENT_CHANNEL
REQUIRED_CHANNELS = channels.REQUIRED

