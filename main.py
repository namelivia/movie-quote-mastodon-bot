from movie_quote_mastodon_bot.factory import Factory
from movie_quote_mastodon_bot.config import Config
import sentry_sdk
import time
import os

if __name__ == "__main__":
    try:
        sentry_sdk.init(os.environ["SENTRY_URL"], traces_sample_rate=1.0)
    except Exception:
        pass
    config = Config(os.environ)
    while True:
        bot = Factory(config).build()
        bot.run()
        del bot
        time.sleep(config.get("idle_period"))
