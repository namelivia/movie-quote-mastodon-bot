from unittest import TestCase
from movie_quote_mastodon_bot.subs import Subs
import mock


class TestSubs(TestCase):
    @mock.patch("movie_quote_mastodon_bot.subs.srt.parse")
    @mock.patch("movie_quote_mastodon_bot.subs.random.choice")
    @mock.patch("movie_quote_mastodon_bot.subs.open")
    def test_getting_a_random_sub(self, m_open, m_choice, m_parse):
        filepath = "/tmp/subs"
        encoding = "utf-8"
        sub_list = ["sub1", "sub2"]
        file_mock = mock.Mock()
        m_open.return_value = file_mock
        file_contents_mock = mock.Mock()
        file_mock.read.return_value = file_contents_mock
        m_parse.return_value = sub_list
        m_choice.return_value = sub_list[0]
        subs = Subs(filepath, encoding)
        self.assertEqual(sub_list[0], subs.get_random())
        m_open.assert_called_once_with(filepath, encoding=encoding)
        file_mock.read.assert_called_once_with()
        m_parse.assert_called_once_with(file_contents_mock)
        m_choice.assert_called_once_with(sub_list)
