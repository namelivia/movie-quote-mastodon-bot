from unittest import TestCase
from movie_quote_mastodon_bot.mastodon import MastodonAPI
import mock


class TestMastodon(TestCase):
    @mock.patch("movie_quote_mastodon_bot.mastodon.Mastodon")
    def test_posting_a_gif(self, m_api_factory):
        mastodon_api_mock = mock.Mock()
        m_api_factory.return_value = mastodon_api_mock
        client_id = "client_id"
        client_secret = "client_secret"
        api_base_url = "api_base_url"
        login = "login"
        password = "password"
        output_uri = "/tmp/output"
        mastodon = MastodonAPI(
            True,
            client_id,
            client_secret,
            api_base_url,
            login,
            password,
            output_uri,
        )
        m_api_factory.assert_called_once_with(
            client_id=client_id,
            client_secret=client_secret,
            api_base_url=api_base_url,
        )
        mastodon_api_mock.log_in.assert_called_once_with(login, password)
        text = "text"
        mastodon_api_mock.media_post.return_value = {"media": "dict"}
        self.assertIsNone(mastodon.post_gif(text))
        mastodon_api_mock.media_post.assert_called_once_with(
            output_uri, mime_type="image/gif"
        )
        mastodon_api_mock.status_post.assert_called_once_with(
            text, media_ids={"media": "dict"}
        )
