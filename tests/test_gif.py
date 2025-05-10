from unittest import TestCase
from movie_quote_mastodon_bot.gif import Gif
import mock


class TestGif(TestCase):
    @mock.patch("movie_quote_mastodon_bot.gif.CompositeVideoClip")
    def test_generating_composite_gif(self, m_composite_video_clip):
        composite_video_mock = mock.Mock()
        output_uri = "/tmp/output"
        gif = Gif(output_uri)
        video = mock.Mock()
        text = mock.Mock()
        m_composite_video_clip.return_value = composite_video_mock
        gif.generate_composite_gif(video, text)
        m_composite_video_clip.assert_called_once_with([video, text])
        composite_video_mock.write_gif.assert_called_once_with(
            output_uri, verbose=False, logger=None
        )
