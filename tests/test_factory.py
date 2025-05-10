from unittest import TestCase
from movie_quote_mastodon_bot.factory import Factory
from movie_quote_mastodon_bot.bot import Bot
import mock


class TestFactory(TestCase):
    @mock.patch("movie_quote_mastodon_bot.factory.Subs")
    @mock.patch("movie_quote_mastodon_bot.factory.TextClip")
    @mock.patch("movie_quote_mastodon_bot.factory.VideoClip")
    @mock.patch("movie_quote_mastodon_bot.factory.MastodonAPI")
    @mock.patch("movie_quote_mastodon_bot.factory.Gif")
    def test_building_bot(self, m_gif, m_mastodon, m_video_clip, m_text_clip, m_subs):
        config = mock.Mock()
        config.get.return_value = "config_value"
        factory = Factory(config)
        bot = factory.build()
        m_subs.assert_called_once_with("config_value", "config_value")
        m_text_clip.assert_called_once_with(
            "config_value", "config_value", "config_value"
        )
        m_video_clip.assert_called_once_with("config_value")
        m_mastodon.assert_called_once_with(
            "config_value",
            "config_value",
            "config_value",
            "config_value",
            "config_value",
            "config_value",
            "config_value",
        )
        m_gif.assert_called_once_with("config_value")
        self.assertIsInstance(bot, Bot)
