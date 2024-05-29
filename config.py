from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 27353035))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", 7071961434))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "Destroyer_Community")
UPDATE_CHNL = getenv("UPDATE_CHNL", "Shine_pfp")
OWNER_USERNAME = getenv("OWNER_USERNAME", "I_RITESH_I")

# Random Start Images
IMG = [
    "https://telegra.ph/file/f792be2c53ed1f54aa84a.jpg",
    "https://telegra.ph/file/13a1a6909216332c04b8e.jpg",
    "https://telegra.ph/file/9e3a13a651cbe877688ed.jpg",
    "https://telegra.ph/file/bec929d7f6c02064b6556.jpg",
    "https://telegra.ph/file/0db9f355e19331ea55a86.jpg",
    "https://telegra.ph/file/e80bc713c5705b0f0cfa4.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgQAAxkBAALRi2NZXUgjZCT775L5Nr0XrLbQ6XIpAAK_EQACpvFxHq2xh5JRVJNrKgQ",
    "CAACAgQAAxkBAALRjGNZXUs6YPggISBdtg4nXaU0vjNzAALqCwACbCIRU61ZQKi3F88DKgQ",
    "CAACAgQAAxkBAALRjWNZXUvETcfHR2Yi9ftTQLLP2uD8AAIVDAAC1SMQU-QrCHEcbz8rKgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]