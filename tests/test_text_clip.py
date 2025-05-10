from unittest import TestCase
from movie_quote_mastodon_bot.text_clip import TextClip
import mock
from datetime import datetime, timedelta


class TestTextClip(TestCase):
    @mock.patch("movie_quote_mastodon_bot.text_clip._TextClip")
    def test_generating_the_quote_text(self, m_text_clip):
        size = 20
        color = "red"
        font = "comicsans"
        text_clip = TextClip(size, color, font)
        quote = mock.Mock()
        quote.content = "some quote"
        quote.start = datetime.now()
        quote.end = quote.start + timedelta(0, 11)
        text_clip_mock = mock.Mock()
        m_text_clip.return_value = text_clip_mock
        text_clip_mock.set_position.return_value = text_clip_mock
        text_clip_mock.set_duration.return_value = text_clip_mock
        text_clip.generate_quote_text(quote)
        m_text_clip.assert_called_once_with(
            quote.content, fontsize=size, color=color, font=font
        )
        text_clip_mock.set_position.assert_called_once_with(("center", "bottom"))
        text_clip_mock.set_duration.assert_called_once_with(11)
