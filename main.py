from movie_quote_mastodon_bot.factory import Factory
from movie_quote_mastodon_bot.config import Config
import time
import os

if __name__ == "__main__":
    config = Config(os.environ)
    while True:
        bot = Factory(config).build()
        bot.run()
        del bot
        time.sleep(config.get("idle_period"))
