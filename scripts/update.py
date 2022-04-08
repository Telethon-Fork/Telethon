import requests

URL = "https://raw.githubusercontent.com/telegramdesktop/tdesktop/dev/Telegram/Resources/tl/api.tl"
get = requests.get(URL).content

open("telethon_generator/data/api.tl", "wb").write(get)
