from unittest import TestCase
from movie_quote_mastodon_bot.video_clip import VideoClip
import mock


class TestVideoClip(TestCase):
    @mock.patch("movie_quote_mastodon_bot.video_clip.VideoFileClip")
    def test_generating_a_quote_video(self, m_video):
        video_uri = "/tmp/video"
        video_clip = VideoClip(video_uri)
        quote = mock.Mock()
        quote.start = 2
        quote.end = 10
        video_mock = mock.Mock()
        m_video.return_value = video_mock
        video_mock.subclip.return_value = video_mock
        video_mock.resize.return_value = video_mock
        self.assertEqual(video_mock, video_clip.generate_quote_video(quote))
        m_video.assert_called_once_with(video_uri)
        video_mock.subclip.assert_called_once_with("2", "10")
        video_mock.resize.assert_called_once_with(0.3)
