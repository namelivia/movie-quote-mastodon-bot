from unittest import TestCase
from movie_quote_mastodon_bot.config import Config


class TestConfig(TestCase):
    def test_getting_a_configuration_values(self):
        source = {
            "IDLE_PERIOD": "3",
            "SUBS_URI": "/tmp/subs",
            "SUBS_ENCODING": "utf-8",
            "VIDEO_URI": "/tmp/video",
            "OUTPUT_URI": "/tmp/output",
            "MASTODON_ENABLED": "True",
            "MASTODON_CLIENT_ID": "mastodonclientid",
            "MASTODON_CLIENT_SECRET": "mastodonclientsecret",
            "MASTODON_API_BASE_URL": "mastodonapibaseurl",
            "MASTODON_LOGIN": "mastodonlogin",
            "MASTODON_PASSWORD": "mastodonpassword",
            "TEXT_SIZE": "20",
            "TEXT_COLOR": "red",
            "TEXT_FONT": "comic_sans",
        }
        config = Config(source)
        self.assertEqual("/tmp/subs", config.get("subs_uri"))
        self.assertEqual(3, config.get("idle_period"))
        self.assertEqual(20, config.get("text_size"))
        self.assertEqual(True, config.get("mastodon_enabled"))
